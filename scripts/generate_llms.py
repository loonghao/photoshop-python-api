"""Generate llms.txt and llms-full.txt for this repository.

``llms.txt`` is a short, curated index that points a language model at the
documents worth reading; ``llms-full.txt`` concatenates the same content
inline so a model can consume it in one request without fetching anything.

Both files are generated, never hand-edited. The ``llms-txt`` job in
``.github/workflows/release.yml`` regenerates them and opens a pull request
whenever the result differs from what is committed.

Run it locally with::

    python scripts/generate_llms.py

Pass ``--check`` to exit non-zero when the committed files are stale. The
``Python package`` workflow runs that on every pull request, so drift fails
the build; the ``llms-txt`` job only opens a pull request to report it.

``--check`` deliberately ignores the ``Version:`` line on both sides. The
version is the newest git tag, so it changes the moment a release lands while
the committed file still carries the previous release; counting that as drift
would turn ``main`` and every pull request red from each release until the
bot's docs pull request is merged by hand. Version lag is converged by the
``llms-txt`` job instead, which opens a pull request for it. Every other line
-- README, examples, module index -- still fails the check.
"""

# Import future modules
from __future__ import annotations

# Import built-in modules
import argparse
import re
import subprocess
import sys

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT

PACKAGE_NAME = "photoshop-python-api"
PROJECT_TITLE = "photoshop-python-api"
PROJECT_URL = "https://github.com/loonghao/photoshop-python-api"
DOCS_URL = "https://photoshop-python-api.readthedocs.io/en/master/"
PYPI_URL = "https://pypi.org/project/photoshop-python-api/"

README = REPO_ROOT / "README.md"
EXAMPLES_DIR = REPO_ROOT / "examples"
PACKAGE_DIR = REPO_ROOT / "photoshop"
DOCS_DIR = REPO_ROOT / "docs"

# Sections of the README that are navigation furniture rather than content.
# Everything before the first real heading is the badge block.
BADGE_BLOCK = re.compile(r"\A.*?<!-- ALL-CONTRIBUTORS-BADGE:END -->\s*</p>\s*", re.DOTALL)

# Trailing sections of the README that are not useful to a model solving a task.
# Matched on the first alphanumeric word of the heading so emoji suffixes such as
# "Contributors ✨" still match.
README_DROP_HEADINGS = {
    "contributors",
    "contributing",
    "credits",
    "license",
    "acknowledgements",
    "acknowledgments",
}

MAX_EXAMPLES_IN_FULL = 40
MAX_EXAMPLE_BYTES = 6000


@dataclass(frozen=True)
class Link:
    """One entry in the llms.txt index."""

    title: str
    url: str
    description: str


def read(path: Path) -> str:
    """Return the text of a file, or an empty string when it is absent."""
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def heading_level(line: str) -> int | None:
    """Return the Markdown heading level of a line, or None if it is not one."""
    match = re.match(r"^(#{1,6})\s+\S", line)
    return len(match.group(1)) if match else None


def strip_badges(text: str) -> str:
    """Remove the HTML badge block that opens the README."""
    return BADGE_BLOCK.sub("", text, count=1).lstrip()


def drop_trailing_sections(text: str, dropped: set[str]) -> str:
    """Return the text with the named top-level sections removed.

    A section runs from its ``##`` heading to the next heading of the same or
    higher level. Only level-2 headings are matched so nested content stays.
    """
    lines = text.splitlines()
    kept: list[str] = []
    skipping = False
    for line in lines:
        level = heading_level(line)
        if level is not None and level <= 2:
            title = line.lstrip("#").strip().lower()
            # Headings carry emoji ("Contributors ✨", "🛠️ Development Guide"),
            # so match on the leading word rather than the whole string.
            first_word = re.search(r"[a-z]+", title)
            skipping = bool(first_word) and first_word.group(0) in dropped
        if not skipping:
            kept.append(line)
    return "\n".join(kept)


def compact_blank_runs(text: str) -> str:
    """Collapse runs of blank lines and drop trailing whitespace."""
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def clean_readme() -> str:
    """Return the README body without badges and without contributor boilerplate."""
    text = strip_badges(read(README))
    text = drop_trailing_sections(text, README_DROP_HEADINGS)
    return compact_blank_runs(text)


def first_paragraph(text: str) -> str:
    """Return the first prose paragraph of a Markdown document."""
    for block in re.split(r"\n\s*\n", text):
        candidate = block.strip()
        if not candidate or candidate.startswith(("#", "```", "|", "<", "---")):
            continue
        return " ".join(candidate.split())
    return ""


def example_files() -> list[Path]:
    """Return the example scripts, sorted by name."""
    if not EXAMPLES_DIR.is_dir():
        return []
    return sorted(p for p in EXAMPLES_DIR.glob("*.py") if p.is_file())


def example_description(path: Path) -> str:
    """Return a one-line description of an example script from its docstring."""
    text = read(path)
    match = re.search(r'"""(.*?)"""', text, re.DOTALL)
    if match:
        summary = first_paragraph(match.group(1))
        if summary:
            return summary
    # Fall back to the module name: the file names are already descriptive.
    return path.stem.replace("_", " ")


def public_modules() -> list[str]:
    """Return the dotted module names of the installed package, sorted."""
    if not PACKAGE_DIR.is_dir():
        return []
    modules: list[str] = []
    for path in sorted(PACKAGE_DIR.rglob("*.py")):
        relative = path.relative_to(PACKAGE_DIR)
        parts = list(relative.parts)
        if parts[-1] == "__init__.py":
            parts = parts[:-1]
        else:
            parts[-1] = parts[-1][: -len(".py")]
        if not parts:
            continue
        modules.append("photoshop." + ".".join(parts) if parts != ["photoshop"] else "photoshop")
    return sorted(set(modules))


def version() -> str:
    """Return the newest released version, falling back to pyproject.

    This reads the most recent tag, which is the version that has *already*
    been published rather than the one a pending release is about to cut: the
    ``llms-txt`` job runs ahead of release-please, so no tag for the upcoming
    version exists yet. The generated files therefore carry the last released
    version until the release lands and the job runs again.
    """
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().lstrip("v")
    except OSError:
        pass
    pyproject = read(REPO_ROOT / "pyproject.toml")
    match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.MULTILINE)
    return match.group(1) if match else "unknown"


def render_index(links: Iterable[Link]) -> str:
    """Render the llms.txt index body."""
    lines = [
        f"# {PROJECT_TITLE}",
        "",
        "> A Python API for controlling Adobe Photoshop on Windows through COM",
        "> automation. It wraps Photoshop's COM interface so scripts can open",
        "> documents, drive layers, export images and run Photoshop actions from",
        "> plain Python.",
        "",
        f"Version: {version()}",
        f"Package: {PYPI_URL}",
        f"Source: {PROJECT_URL}",
        f"Full documentation: {DOCS_URL}",
        "",
        "## Getting started",
        "",
        "Install with `pip install photoshop-python-api`. It requires Windows and",
        "a locally installed Adobe Photoshop. `photoshop.Session` is the entry",
        "point: it opens Photoshop if it is not running, gives you the active",
        "document, and exposes the API's classes and constants as attributes.",
        "",
        "```python",
        "from photoshop import Session",
        "",
        "with Session(action='new_document') as ps:",
        "    doc = ps.active_document",
        "    text_color = ps.SolidColor()",
        "    text_color.rgb.green = 255",
        "    new_text_layer = doc.artLayers.add()",
        "    new_text_layer.kind = ps.LayerKind.TextLayer",
        "    new_text_layer.textItem.contents = 'Hello, World!'",
        "    new_text_layer.textItem.position = [160, 167]",
        "    new_text_layer.textItem.size = 40",
        "    new_text_layer.textItem.color = text_color",
        "    options = ps.JPEGSaveOptions(quality=5)",
        "    jpg = 'd:/hello_world.jpg'",
        "    doc.saveAs(jpg, options, asCopy=True)",
        "```",
        "",
        "## Table of contents",
        "",
    ]

    for link in links:
        summary = f" — {link.description}" if link.description else ""
        lines.append(f"- [{link.title}]({link.url}){summary}")

    lines += [
        "",
        "## Conventions",
        "",
        "- All modules live under the `photoshop` package; `photoshop.api` exposes",
        "  the COM wrapper classes and `photoshop.api.enumerations` the constants.",
        "- The quickest route to a working script is `photoshop.Session`, which",
        "  exposes the API's classes and constants as attributes on the session",
        "  object so `import photoshop.api as ps` is not needed for every name.",
        "- Enumeration members use Photoshop's own names, so `ps.LayerKind.TextLayer`",
        "  maps to the constant Photoshop calls `LayerKind.TextLayer`.",
        "- Every example under `examples/` is runnable as a standalone script when",
        "  Photoshop is installed.",
        "",
        "## Optional",
        "",
        f"- [Changelog]({PROJECT_URL}/blob/main/CHANGELOG.md) — release history.",
        f"- [Issue tracker]({PROJECT_URL}/issues) — known problems and questions.",
        "",
    ]
    return "\n".join(lines)


def render_full(links: Iterable[Link]) -> str:
    """Render the llms-full.txt body: every source document concatenated."""
    parts: list[str] = [
        f"# {PROJECT_TITLE} — full reference",
        "",
        f"Version: {version()}",
        f"Source: {PROJECT_URL}",
        f"Documentation: {DOCS_URL}",
        "",
        "This file concatenates the repository's documentation and example code so",
        "it can be consumed in a single request. It is generated by",
        "`scripts/generate_llms.py`; edit the sources, not this file.",
        "",
        "---",
        "",
        "## README",
        "",
        clean_readme(),
        "",
        "---",
        "",
    ]

    if links:
        parts += ["---", "", "## Contents", ""]
        for link in links:
            summary = f" — {link.description}" if link.description else ""
            parts.append(f"- [{link.title}]({link.url}){summary}")
        parts.append("")

    examples = example_files()
    if examples:
        parts += ["---", "", "## Examples", ""]
        parts.append(
            "Each example is a standalone script. Constants come from"
            " `photoshop.api.enumerations` and classes from `photoshop.api`."
        )
        parts.append("")
        for path in examples[:MAX_EXAMPLES_IN_FULL]:
            body = read(path)
            if len(body.encode("utf-8")) > MAX_EXAMPLE_BYTES:
                body = body.encode("utf-8")[:MAX_EXAMPLE_BYTES].decode("utf-8", "ignore")
                body += "\n\n# ... truncated ...\n"
            parts += [
                f"### {path.name}",
                "",
                example_description(path),
                "",
                "```python",
                body.strip(),
                "```",
                "",
            ]
        if len(examples) > MAX_EXAMPLES_IN_FULL:
            remaining = len(examples) - MAX_EXAMPLES_IN_FULL
            parts += [f"({remaining} further examples are in `examples/`.)", ""]

    modules = public_modules()
    if modules:
        parts += ["---", "", "## Module index", ""]
        parts.append("Public modules in the `photoshop` package:")
        parts.append("")
        for name in modules:
            parts.append(f"- `{name}`")
        parts.append("")

    return "\n".join(parts)


def build_links() -> list[Link]:
    """Return the curated index entries pointing at this repository's content."""
    links = [
        Link(
            "Getting started",
            f"{PROJECT_URL}/blob/main/README.md",
            "installation, requirements and supported Photoshop versions",
        ),
        Link(
            "API reference",
            DOCS_URL,
            "generated reference for every wrapper class",
        ),
        Link(
            "Examples",
            f"{PROJECT_URL}/tree/main/examples",
            f"{len(example_files())} runnable scripts covering common tasks",
        ),
    ]

    docs_index = DOCS_DIR / "index.md"
    if docs_index.is_file():
        links.append(Link("Documentation source", f"{PROJECT_URL}/tree/main/docs", "the MkDocs site sources"))

    return links


def without_version_line(text: str) -> str:
    """Return `text` with every ``Version:`` line removed.

    Used only when comparing, never when writing. The stamped version comes
    from the newest git tag, so it changes the moment a release lands, while
    the committed file still carries the previous release's version. Treating
    that as drift would turn `main` and every pull request red from each
    release until the bot's docs pull request is merged by hand.

    The version is still regenerated and still committed: the `llms-txt` job
    opens a pull request for it, which is how it converges. This function only
    keeps the drift *gate* from firing on version lag alone.
    """
    return "\n".join(line for line in text.splitlines() if not line.startswith("Version: "))


def is_current(name: str, expected: str) -> bool:
    """Return True when the committed `name` matches `expected`, ignoring version."""
    committed = read(OUTPUT_DIR / name)
    if not committed:
        return False
    return without_version_line(committed) == without_version_line(expected)


def write_if_changed(path: Path, content: str) -> bool:
    """Write `content` to `path` when it differs; return True when it changed.

    Newlines are written as LF explicitly. Without it the output would follow
    the platform default, so a maintainer on Windows and the CI job on Linux
    would produce different bytes for the same content and undo each other.
    Git normalises the result on commit either way.
    """
    if path.is_file() and read(path) == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    """Generate both files, or verify them under ``--check``."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero when the committed files are out of date",
    )
    args = parser.parse_args()

    links = build_links()
    index_text = render_index(links)
    full_text = render_full(links)

    if args.check:
        # Ignores the `Version:` line on both sides: version lag is converged by
        # the llms-txt bot pull request, not by failing the build. Anything else
        # — README, examples, module index — still fails here.
        stale = [
            name
            for name, text in (("llms.txt", index_text), ("llms-full.txt", full_text))
            if not is_current(name, text)
        ]
        if stale:
            joined = ", ".join(stale)
            print(f"::error::{joined} are out of date; run scripts/generate_llms.py")
            return 1
        print("llms.txt and llms-full.txt are up to date")
        return 0

    changed = [
        name
        for name, text in (("llms.txt", index_text), ("llms-full.txt", full_text))
        if write_if_changed(OUTPUT_DIR / name, text)
    ]
    if changed:
        print("Updated: " + ", ".join(changed))
    else:
        print("No changes: llms.txt and llms-full.txt are current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
