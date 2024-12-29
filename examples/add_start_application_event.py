"""Add event for Photoshop start application.

In the current example, every time we start photoshop it will
alert "Start Application Event".

Just like you manually in Script> Script Events Manager to enable the event.

"""

# Import built-in modules
from __future__ import annotations

import os
from tempfile import mkdtemp
from pathlib import Path

# Import local modules
from photoshop import Session

with Session() as ps:
    root = Path(mkdtemp())
    jsx_file = root / "event.jsx"
    jsx_file.write_text('alert("Start Application event.")')
    ps.app.notifiers.add(ps.EventID.Notify, str(jsx_file))
    ps.echo("Add event done.")
