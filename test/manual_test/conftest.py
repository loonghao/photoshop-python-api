"""Shared skip handling for the manual tests.

Every module here drives a real Photoshop instance, so none of it can run on a
machine without Photoshop installed. The guard below skips this directory in
that case instead of letting collection fail with a COM error.
"""

# Import future modules
from __future__ import annotations

# Import built-in modules
import os

from pathlib import Path

# Import third-party modules
import pytest

MANUAL_TEST_DIR = Path(__file__).parent.resolve()


def photoshop_is_available() -> bool:
    """Return True when a Photoshop automation object can actually be driven.

    Creating the Application object is not enough: automation also fails when
    Photoshop is running but busy (a modal dialog, for instance), which surfaces
    as a COMError on any property access. Touching a cheap property proves the
    instance is responsive.
    """
    if os.name != "nt":
        return False
    try:
        # Import local modules
        from photoshop.api import Application

        Application().preferences
    except Exception:  # noqa: BLE001 - missing, busy or unreachable Photoshop
        return False
    return True


def _is_manual_test(item: pytest.Item) -> bool:
    """Return True when the collected item lives under this directory."""
    item_path = item.path.resolve()
    return item_path == MANUAL_TEST_DIR or MANUAL_TEST_DIR in item_path.parents


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Skip this directory's tests when no Photoshop instance is available.

    ``items`` is session-wide: pytest calls this hook once per conftest with
    every item collected anywhere in the run, not just the ones below this
    directory. Marking it unconditionally therefore also silences the headless
    tests in the rest of the suite, which is how the Import Test lane went green
    without executing a single test body. The marker is applied only to the
    items this conftest actually owns.
    """
    manual_items = [item for item in items if _is_manual_test(item)]
    if not manual_items:
        # Nothing here was collected, so don't pay for the availability probe.
        return
    if photoshop_is_available():
        return
    skip = pytest.mark.skip(reason="Photoshop is not installed on this machine")
    for item in manual_items:
        item.add_marker(skip)
