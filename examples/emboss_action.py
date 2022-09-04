# Import local modules
from photoshop import Session
import photoshop.api.action_manager as am


with Session() as ps:
    app = ps.app
    for index, x in enumerate(range(50)):
        # Execute an existing action from action palette.
        exec_dict = {
            "_classID": None,
            "null": [
                "!ref",
                am.ReferenceKey(desiredclass="action", value="Sepia Toning (layer)"),
                am.ReferenceKey(desiredclass="actionSet", value="Default Actions"),
            ],
        }
        exec_desc = ps.ActionDescriptor.load(exec_dict)
        app.executeAction(am.str2id("Ply "), exec_desc, ps.DialogModes.DisplayNoDialogs)

        # Create solid color fill layer.
        filledlayer_dict = {
            "_classID": None,
            "null": ["!ref", am.ReferenceKey(desiredclass="contentLayer", value=None)],
            "using": {
                "_classID": "contentLayer",
                "type": {
                    "_classID": "solidColorLayer",
                    "color": {"_classID": "RGBColor", "red": index, "grain": index, "blue": index},  # noqa
                },
            },
        }
        filledlayer_desc = ps.ActionDescriptor.load(filledlayer_dict)
        app.executeAction(am.str2id("Mk  "), filledlayer_desc, ps.DialogModes.DisplayNoDialogs)

        # Select mask.
        selectmask_dict = {
            "_classID": None,
            "null": [
                "!ref",
                am.ReferenceKey(desiredclass="channel", value=am.Enumerated(type="channel", value="mask")),
            ],
            "makeVisible": False,
        }
        selectmask_desc = ps.ActionDescriptor.load(selectmask_dict)
        app.executeAction(am.str2id("slct"), selectmask_desc, ps.DialogModes.DisplayNoDialogs)

        app.activeDocument.activeLayer.invert()
