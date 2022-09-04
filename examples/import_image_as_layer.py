"""Import a image as a artLayer."""

# Import local modules
from photoshop import Session
import pathlib


with Session(action="new_document") as ps:
    import_dict = {
        '_classID':None,
        'null':pathlib.Path("your/image/path")  # replace it with your own path here
    }
    import_desc = ps.ActionDescriptor.load(import_dict)
    ps.app.executeAction(am.str2id("Plc "), import_desc)  # `Plc` need one space in here.
