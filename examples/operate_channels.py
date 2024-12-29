"""A examples to show you how to operate active document channels."""

# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as ps:
    doc = ps.active_document
    print(len(doc.channels))
    doc.channels.add()
    doc.channels.removeAll()
    channel = doc.channels.getByName("Red")
    print(channel.name)
    channel.remove()
