"""Replace the image of the current active layer with a new image."""


from photoshop import Session

with Session() as ps:
    replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
    desc = ps.ActionDescriptor
    idnull = ps.app.charIDToTypeID("null")
    desc.putPath(idnull, "your/image/path.jpg")
    ps.app.executeAction(replace_contents, desc)
