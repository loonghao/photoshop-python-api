"""Do a photoshop action."""
from photoshop import Session

with Session() as api:
    api.app.doAction(action_name="Frame Channel - 50 pixel")
