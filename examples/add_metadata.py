"""Add metadata to current active document."""
# Import built-in modules
import os

from photoshop import Session
# Import local modules


with Session(action="new_document") as ps:
    doc = ps.active_document
    doc.info.author = os.getenv("USERNAME")
    doc.info.provinceState = "Beijing"
    doc.info.title = "My Demo"
    print("Print all metadata of current active document.")
    ps.echo(doc.info)
