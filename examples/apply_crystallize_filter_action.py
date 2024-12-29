"""Demonstrate how to apply the Crystallize filter using Photoshop's native filter commands.

This example shows how to:
1. Use Photoshop's native filter commands to apply filters
2. Work with layer sets and art layers
3. Apply the Crystallize filter

The script applies the Crystallize filter to the last art layer in the last layer set
of the document.
"""

# Import third-party modules
from __future__ import annotations

# Import local modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session
from photoshop.api.errors import PhotoshopPythonAPIError

# Get sample PSD file path
PSD_FILE = psd.get_psd_files()

# Open the PSD file in Photoshop
with Session(PSD_FILE["layer_comps.psd"], "open") as ps:
    app = ps.app
    active_document = ps.active_document

    # Get all layer sets (groups) in the document
    layer_sets = active_document.layerSets
    ps.echo(f"The total amount of current layerSet (Group) is {len(layer_sets)}.")

    # Get the last layer set
    last_layer_set_index = len(layer_sets) - 1
    last_layer_set = layer_sets[last_layer_set_index]
    art_layers = last_layer_set.artLayers
    ps.echo(f"The total amount of art layers in the last layer set is {len(art_layers)}.")

    # Find a layer set with art layers
    current_layer_set_index = last_layer_set_index
    while len(art_layers) == 0 and current_layer_set_index > 0:
        current_layer_set_index -= 1
        current_layer_set = layer_sets[current_layer_set_index]
        art_layers = current_layer_set.artLayers
        ps.echo(f"Checking layer set {current_layer_set.name}: {len(art_layers)} art layers")

    if len(art_layers) == 0:
        raise PhotoshopPythonAPIError("No art layers found in any layer set")

    # Set the last art layer in the current layer set as active
    last_art_layer_index = len(art_layers) - 1
    last_art_layer = art_layers[last_art_layer_index]
    active_document.activeLayer = last_art_layer
    ps.echo(f"Selected layer: {last_art_layer.name}")

    def apply_crystallize(cell_size: int = 10) -> None:
        """Apply the Crystallize filter to the active layer.
        
        Args:
            cell_size: The size of the crystallize cells (1-300).
        """
        # Apply the Crystallize filter using JavaScript
        js_code = f"""
        try {{
            // Get the active document and layer
            var doc = app.activeDocument;
            var layer = doc.activeLayer;
            
            // Create a reference to the current layer
            var ref = new ActionReference();
            ref.putProperty(charIDToTypeID("Prpr"), charIDToTypeID("Lefx"));
            ref.putEnumerated(charIDToTypeID("Lyr "), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
            
            // Create a descriptor for the Crystallize filter
            var desc = new ActionDescriptor();
            desc.putReference(charIDToTypeID("null"), ref);
            
            // Set the cell size
            var filterDesc = new ActionDescriptor();
            filterDesc.putInteger(charIDToTypeID("ClSz"), {cell_size});
            
            // Apply the filter
            executeAction(charIDToTypeID("Crst"), filterDesc, DialogModes.NO);
        }} catch (e) {{
            alert("Error: " + e);
        }}
        """
        app.doJavaScript(js_code)

    # Apply the Crystallize filter with cell size 25
    try:
        apply_crystallize(25)
        ps.echo("Apply crystallize filter done.")
    except Exception as e:
        ps.echo(f"Error: {e!s}")
        # Try alternative method using native filter
        js_code = """
        try {
            var desc = new ActionDescriptor();
            var ref = new ActionReference();
            ref.putClass(charIDToTypeID("Crst"));
            desc.putReference(charIDToTypeID("null"), ref);
            desc.putInteger(charIDToTypeID("ClSz"), 25);
            executeAction(charIDToTypeID("Crst"), desc, DialogModes.NO);
        } catch (e) {
            alert("Error: " + e);
        }
        """
        app.doJavaScript(js_code)
        ps.echo("Apply crystallize filter done (alternative method).")
