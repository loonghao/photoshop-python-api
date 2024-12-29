# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as ps:
    # Print the current tool.
    ps.echo(ps.app.currentTool)

    # Set current tool to `typeCreateOrEditTool`.
    ps.app.currentTool = "typeCreateOrEditTool"
