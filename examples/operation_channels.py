"""A examples to show you how to operation active document channels."""

from photoshop import Session

with Session() as ps:
    doc = ps.active_document
    print(len(doc.channels))
    doc.channels.add()
    doc.channels.removeAll()
    channel = doc.channels.getByName("Red")
    print(channel.name)
    channel.remove()
