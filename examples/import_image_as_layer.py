"""Import a image as a artLayer."""

# Import built-in modules
import pathlib

# Import local modules
from photoshop import Session
import photoshop.api.action_manager as am


def importfile(app, path: pathlib.WindowsPath, position: (float, float), size: (float, float)):  # noqa
    px, py = position
    sx, sy = size
    import_dict = {
        "null": path,
        "freeTransformCenterState": am.Enumerated(type="quadCenterState", value="QCSAverage"),
        "offset": {
            "horizontal": am.UnitDouble(unit="distanceUnit", double=px),
            "vertical": am.UnitDouble(unit="distanceUnit", double=py),
            "_classID": "offset",
        },
        "width": am.UnitDouble(unit="percentUnit", double=sx),
        "height": am.UnitDouble(unit="percentUnit", double=sy),
        "_classID": None,
    }
    import_desc = ps.ActionDescriptor.load(import_dict)
    app.executeAction(am.str2id("placeEvent"), import_desc)


with Session(action="new_document") as ps:
    importfile(ps.app, pathlib.Path("your/image/path"), (-100, 456), (4470, 4463))
