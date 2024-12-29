"""Add event for Photoshop start application.

This example demonstrates how to add an event listener that triggers when Photoshop starts.
Every time Photoshop is launched, it will display an alert message saying "Start Application Event".

This is equivalent to manually setting up an event in Photoshop through:
File > Scripts > Script Events Manager

Example:
    ```python
    with Session() as ps:
        root = Path(mkdtemp())
        jsx_file = root / "event.jsx"
        jsx_file.write_text('alert("Start Application event.")')
        ps.app.notifiers.add(ps.EventID.Notify, str(jsx_file))
    ```

Note:
    The event will persist even after the script finishes running.
    To remove the event, use the Script Events Manager in Photoshop.
"""

# Import built-in modules
from __future__ import annotations

from pathlib import Path
from tempfile import mkdtemp

# Import local modules
from photoshop import Session

# Create a new Photoshop session
with Session() as ps:
    # Create a temporary directory to store the JSX script
    root = Path(mkdtemp())
    jsx_file = root / "event.jsx"

    # Write the JavaScript code that will be executed when Photoshop starts
    jsx_file.write_text('alert("Start Application event.")')

    # Add the event notifier to Photoshop
    # EventID.Notify is triggered when Photoshop starts
    ps.app.notifiers.add(ps.EventID.Notify, str(jsx_file))

    # Confirm the event was added successfully
    ps.echo("Add event done.")
