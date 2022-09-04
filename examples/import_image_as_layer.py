"""Import a image as a artLayer."""

# Import built-in modules
import pathlib

# Import local modules
from photoshop import Session
import photoshop.api.action_manager as am


with Session(action="new_document") as ps:
    # replace it with your own path here
    import_dict = {"_classID": None, "null": pathlib.Path("your/image/path")}
    import_desc = ps.ActionDescriptor.load(import_dict)
    ps.app.executeAction(am.str2id("Plc "), import_desc)
    # length of charID should always be 4, if not, pad with spaces
