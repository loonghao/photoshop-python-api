"""Toggle the proof color.

Like operating in the menu:
**View** > **Proof Colors** (Ctrl + Y)

"""
# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as ps:
    ps.app.runMenuItem(ps.app.stringIDToTypeID("toggleProofColors"))
