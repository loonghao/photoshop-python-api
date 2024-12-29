"""Example of executing Photoshop actions.

This example demonstrates how to:
1. Play recorded Photoshop actions
2. Work with action sets
3. Handle action execution
4. Manage action parameters

Key concepts:
- Action playback
- Action sets
- Action execution
- Automation
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Play default Photoshop action
    ps.app.doAction("action_name", "set_name")
