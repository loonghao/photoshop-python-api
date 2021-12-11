"""Do a photoshop action."""
from photoshop import Session

with Session() as api:
    api.app.doAction(action="Frame Channel - 50 pixel")
