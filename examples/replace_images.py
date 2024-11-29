"""Replace the image of the current active layer with a new image."""
# Import third-party modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import local modules


PSD_FILE = psd.get_psd_files()


with Session(PSD_FILE["replace_images.psd"], action="open") as ps:
    active_layer = ps.active_document.activeLayer
    bounds = active_layer.bounds
    print(f"current layer {active_layer.name}: {bounds}")
    input_file = PSD_FILE["red_100x200.png"]
    replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
    desc = ps.ActionDescriptor
    idnull = ps.app.charIDToTypeID("null")
    desc.putPath(idnull, input_file)
    ps.app.executeAction(replace_contents, desc)

    # replaced image.
    active_layer = ps.active_document.activeLayer
    current_bounds = active_layer.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]

    current_width = current_bounds[2] - current_bounds[0]
    current_height = current_bounds[3] - current_bounds[1]
    new_size = width / current_width * 100
    active_layer.resize(new_size, new_size, ps.AnchorPosition.MiddleCenter)
    print(f"current layer {active_layer.name}: {current_bounds}")
