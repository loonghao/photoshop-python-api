"""Enable Generator features."""
from photoshop import Session

with Session() as ps:
    plugin_name = "generator-assets-dummy-menu"
    generatorDesc = ps.ActionDescriptor
    generatorDesc.putString(ps.app.stringIDToTypeID("name"), plugin_name)
    ps.app.executeAction(ps.app.stringIDToTypeID("generateAssets"),
                         generatorDesc)
