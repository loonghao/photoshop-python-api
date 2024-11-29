"""Add event for Photoshop start application.

In the current example, every time we start photoshop it will
alert "Start Application Event".

Just like you manually in Script> Script Events Manager to enable the event.

"""
# Import built-in modules
import os
from tempfile import mkdtemp

from photoshop import Session
# Import local modules


with Session() as ps:
    root = mkdtemp()
    jsx_file = os.path.join(root, "event.jsx")
    with open(jsx_file, "w") as f:
        f.write('alert("Start Application event.")')
    ps.app.notifiers.add(ps.EventID.Notify, jsx_file)
    print("Add event done.")
