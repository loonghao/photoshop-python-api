"""Tests for the llms.txt generator's drift comparison."""

# Import future modules

# Import built-in modules
import importlib.util
import sys

from pathlib import Path

# Import third-party modules
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "generate_llms.py"


def load_generator():
    """Import scripts/generate_llms.py, which is outside the package tree."""
    spec = importlib.util.spec_from_file_location("generate_llms", SCRIPT_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["generate_llms"] = module
    spec.loader.exec_module(module)
    return module


generator = load_generator()


def test_header_version_line_is_stripped():
    """A changed header version is not drift: releases change the tag, not content."""
    old = "# Title\n\nVersion: 0.1.0\nPackage: x\n\n## Body\n\ntext\n"
    new = "# Title\n\nVersion: 0.2.0\nPackage: x\n\n## Body\n\ntext\n"

    assert generator.without_version_line(old) == generator.without_version_line(new)


def test_body_version_line_is_kept():
    """A `Version: ` line in the body is content and must still count as drift.

    llms-full.txt embeds the README and the example scripts. If body lines
    starting with `Version: ` were stripped too, a real content change there
    would slip past the gate unnoticed.
    """
    old = "# Title\n\nVersion: 0.1.0\n\n## Body\n\ntext\n"
    new = "# Title\n\nVersion: 0.1.0\n\n## Body\n\nVersion: 9.9.9\ntext\n"

    assert generator.without_version_line(old) != generator.without_version_line(new)


def test_body_version_line_change_is_detected_end_to_end(monkeypatch, tmp_path):
    """A version line added to embedded content still fails the real --check path.

    Drives `is_current` against a temp tree so the assertion covers the
    comparison the CLI actually performs, not just the helper.
    """
    committed = "# Title\n\nVersion: 0.1.0\n\n## Body\n\ntext\n"
    (tmp_path / "llms.txt").write_text(committed, encoding="utf-8")

    monkeypatch.setattr(generator, "OUTPUT_DIR", tmp_path)

    # Same file with only the header version bumped: still current.
    header_only = "# Title\n\nVersion: 0.2.0\n\n## Body\n\ntext\n"
    assert generator.is_current("llms.txt", header_only)

    # A `Version: ` line appearing in the body: drift, so it must fail.
    with_body_line = "# Title\n\nVersion: 0.2.0\n\n## Body\n\nVersion: 9.9.9\ntext\n"
    assert not generator.is_current("llms.txt", with_body_line)


def test_only_one_header_version_line_is_stripped():
    """Only the header run is touched; the rest of the document is untouched."""
    text = "# Title\n\nVersion: 0.1.0\nPackage: x\n\n## A\n\nVersion: keep\n\n## B\n\nend\n"

    result = generator.without_version_line(text)

    assert "Version: 0.1.0" not in result
    assert "Version: keep" in result
    assert result.endswith("## B\n\nend")


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # No body at all: the whole document is header, so the line goes.
        ("Version: 1.0.0\nPackage: x\n", "Package: x"),
        # Empty input stays empty.
        ("", ""),
    ],
)
def test_edge_cases(text, expected):
    """Degenerate documents do not raise and behave predictably."""
    assert generator.without_version_line(text) == expected
