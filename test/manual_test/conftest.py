"""Shared skip handling for the manual tests.

Every module here drives a real Photoshop instance, so none of it can run on a
machine without Photoshop installed. The guard below skips the whole directory
in that case instead of letting collection fail with a COM error.
"""

# Import future modules
from __future__ import annotations

# Import built-in modules
import os

# Import third-party modules
import pytest


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


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Skip every collected test when no Photoshop instance is available."""
    if photoshop_is_available():
        return
    skip = pytest.mark.skip(reason="Photoshop is not installed on this machine")
    for item in items:
        item.add_marker(skip)
