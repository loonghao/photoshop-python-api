"""Do a photoshop action."""
# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as api:
    api.app.doAction(action="Frame Channel - 50 pixel")
