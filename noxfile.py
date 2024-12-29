"""Nox sessions."""
import os
import shutil
import sys
from pathlib import Path
from textwrap import dedent

import nox
from nox.sessions import Session


PYTHON_VERSIONS = ["3.7", "3.8", "3.9", "3.10", "3.11", "3.12"]
nox.needs_version = ">= 2023.4.22"
nox.options.sessions = (
    "pre-commit",
    "ruff",
    "safety",
    "mypy",
    "tests",
    "docs-build",
    "build",
    "release",
)


def install_with_uv(session: Session, *args: str) -> None:
    """Install packages with uv."""
    session.install("uv")
    if args:
        session.run("uv", "pip", "install", *args, external=True)


def activate_virtualenv_in_precommit_hooks(session: Session) -> None:
    """Activate virtualenv in hooks installed by pre-commit."""
    assert session.bin is not None  # noqa: S101

    virtualenv = session.env.get("VIRTUAL_ENV")
    if virtualenv is None:
        return

    hookdir = Path(".git") / "hooks"
    if not hookdir.is_dir():
        return

    for hook in hookdir.iterdir():
        if hook.name.endswith(".sample") or not hook.is_file():
            continue

        text = hook.read_text()
        bindir = repr(session.bin)[1:-1]  # strip quotes
        if not (
            Path("A") == Path("a") and bindir.lower() in text.lower() or bindir in text
        ):
            continue

        lines = text.splitlines()
        if not (lines[0].startswith("#!") and "python" in lines[0].lower()):
            continue

        header = dedent(
            f"""\
            import os
            os.environ["VIRTUAL_ENV"] = {virtualenv!r}
            os.environ["PATH"] = os.pathsep.join((
                {session.bin!r},
                os.environ.get("PATH", ""),
            ))
            """
        )

        lines.insert(1, header)
        hook.write_text("\n".join(lines))


@nox.session(name="pre-commit")
def precommit(session: Session) -> None:
    """Lint using pre-commit."""
    args = session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    install_with_uv(
        session,
        "black",
        "flake8",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-rst-docstrings",
        "isort",
        "pep8-naming",
        "pre-commit",
        "pre-commit-hooks",
        "pyupgrade",
        "ruff",
    )
    session.run("pre-commit", *args)
    if args and args[0] == "install":
        activate_virtualenv_in_precommit_hooks(session)


@nox.session()
def ruff(session: Session) -> None:
    """Run ruff."""
    args = session.posargs or ["check", ".", "--fix"]
    install_with_uv(session, "ruff")
    session.run("ruff", *args)


@nox.session()
def safety(session: Session) -> None:
    """Scan dependencies for insecure packages."""
    with open("requirements.txt") as f:
        requirements = f.read()
    install_with_uv(session, "safety")
    session.run("safety", "check", "--full-report", requirements)


@nox.session()
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or ["photoshop", "tests"]
    install_with_uv(session, ".", "mypy", "types-all")
    session.run("mypy", *args)
    if not session.posargs:
        session.run("mypy", f"--python-executable={sys.executable}", "noxfile.py")


@nox.session(python=PYTHON_VERSIONS)
def tests(session: Session) -> None:
    """Run the test suite."""
    install_with_uv(session, ".", "coverage[toml]", "pytest", "pygments", "pytest-cov")
    try:
        session.run("coverage", "run", "--parallel", "-m", "pytest", *session.posargs)
    finally:
        if session.interactive:
            session.notify("coverage", posargs=[])


@nox.session()
def coverage(session: Session) -> None:
    """Produce the coverage report."""
    args = session.posargs or ["report"]

    install_with_uv(session, "coverage[toml]")

    if not session.posargs and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)


@nox.session(name="docs-build")
def docs_build(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "build"]
    install_with_uv(
        session,
        ".",
        "mkdocs",
        "mkdocs-git-revision-date-plugin",
        "mkdocs-material",
        "mkdocstrings-python",
        "mkdocs-pymdownx-material-extras",
        "mkdocs-same-dir",
        "mkdocs-include-markdown-plugin",
        "mkdocs-gen-files",
        "mkdocs-literate-nav",
        "mkdocs-git-revision-date-localized-plugin",
        "mkdocs-section-index",
        "mkdocs-git-authors-plugin",
        "mkdocs-autolinks-plugin",
        "mkdocs-minify-plugin",
        "stringcase",
    )

    build_dir = Path("site")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("mkdocs", "build")


@nox.session()
def docs(session: Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = session.posargs or ["serve"]
    install_with_uv(
        session,
        ".",
        "mkdocs",
        "mkdocs-git-revision-date-plugin",
        "mkdocs-material",
        "mkdocstrings-python",
        "mkdocs-pymdownx-material-extras",
        "mkdocs-same-dir",
        "mkdocs-include-markdown-plugin",
        "mkdocs-gen-files",
        "mkdocs-literate-nav",
        "mkdocs-git-revision-date-localized-plugin",
        "mkdocs-section-index",
        "mkdocs-git-authors-plugin",
        "mkdocs-autolinks-plugin",
        "mkdocs-minify-plugin",
        "stringcase",
    )

    if args[0] == "serve":
        session.run("mkdocs", "serve")
    elif args[0] == "build":
        session.run("mkdocs", "build")
    elif args[0] == "deploy":
        session.run("mkdocs", "gh-deploy", "--force")
    else:
        session.run("mkdocs", *args)


@nox.session()
def build(session: Session) -> None:
    """Build the package."""
    install_with_uv(session, "build")
    session.run("python", "-m", "build")


@nox.session()
def release(session: Session) -> None:
    """Release the package to PyPI."""
    if not session.posargs:
        session.error("Please provide a version number, e.g: nox -s release -- 1.0.0")
    
    version = session.posargs[0]
    
    # Install dependencies
    install_with_uv(session, "twine", "build")
    
    # Clean up previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    # Build the package
    session.run("python", "-m", "build")
    
    # Upload to PyPI
    session.run("twine", "check", "dist/*")
    session.run("twine", "upload", "dist/*")
