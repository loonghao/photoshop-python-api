"""Import a image as a artLayer."""

# Import local modules
from photoshop import Session


with Session(action="new_document") as ps:
    desc = ps.ActionDescriptor
    desc.putPath(ps.app.charIDToTypeID("null"), "your/image/path")
    event_id = ps.app.charIDToTypeID("Plc ")  # `Plc` need one space in here.
    ps.app.executeAction(ps.app.charIDToTypeID("Plc "), desc)
