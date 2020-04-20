"""Toggle the proof color.

Like operating in the menu:
**View** > **Proof Colors** (Ctrl + Y)

"""
from photoshop import Session

with Session() as ps:
    ps.app.runMenuItem(ps.app.stringIDToTypeID("toggleProofColors"))
