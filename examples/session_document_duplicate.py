"""Action for duplicate current active document."""
# Import local modules
from __future__ import annotations

from photoshop import Session

with Session(action="document_duplicate") as ps:
    ps.echo(ps.active_document.name)
