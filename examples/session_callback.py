"""Example of using callbacks with Photoshop sessions.

This example demonstrates how to:
1. Set up session callbacks
2. Handle Photoshop events
3. Manage callback execution
4. Process event data

Key concepts:
- Event handling
- Callbacks
- Session management
- Event processing
"""

# Import local modules
from photoshop import Session


def on_close():
    """Callback function for session close event."""
    print("Session is closing")


with Session(callback=on_close) as ps:
    ps.echo("Working in session...")
