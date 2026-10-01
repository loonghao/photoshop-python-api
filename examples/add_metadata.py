"""Add metadata to current active document."""


from __future__ import annotations
# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session(action="new_document") as ps:
    doc = ps.active_document
    doc.info.author = os.getenv("USERNAME")
    doc.info.provinceState = "Beijing"
    doc.info.title = "My Demo"
    print("Print all metadata of current active document.")
    print(doc.info)
