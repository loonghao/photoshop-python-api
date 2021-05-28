"""Action for create new document and print new document name."""
# Import local modules
from photoshop import Session


with Session(action="new_document") as ps:
    ps.echo(ps.active_document.name)
