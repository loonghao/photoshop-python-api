"""Action for duplicate current active document."""
from photoshop import Session

with Session(action="document_duplicate") as ps:
    ps.echo(ps.active_document.name)
