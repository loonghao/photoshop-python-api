"""Create a new document."""

# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as ps:
    ps.app.preferences.rulerUnits = ps.Units.Pixels
    ps.app.documents.add(1920, 1080, name="my_new_document")
