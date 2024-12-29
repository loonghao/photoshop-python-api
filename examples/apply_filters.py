"""Apply various filters to an image.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyFilters.py.

Example of applying various filters to a Photoshop document.
"""

# Import third-party modules
from __future__ import annotations

import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session
from photoshop.api.enumerations import SelectionType, NoiseDistribution

PSD_FILE = psd.get_psd_files()

with Session() as ps:
    app = ps.app
    # We don't want any Photoshop dialogs displayed during automated execution
    app.displayDialogs = ps.DialogModes.DisplayNoDialogs

    PS_PIXELS = 1
    start_ruler_units = app.preferences.rulerUnits
    if start_ruler_units is not PS_PIXELS:
        app.preferences.rulerUnits = PS_PIXELS

    file_name = PSD_FILE["layer_comps.psd"]
    doc_ref = app.open(file_name)
    
    # Get the first layer set that has art layers
    layer_sets = doc_ref.layerSets
    target_layer_set = None
    target_art_layer = None
    
    for layer_set in layer_sets:
        if len(layer_set.artLayers) > 0:
            target_layer_set = layer_set
            target_art_layer = layer_set.artLayers[0]  # Get the first art layer
            break
    
    if target_art_layer is None:
        raise Exception("No art layers found in any layer set")
    
    # Set the active layer
    doc_ref.activeLayer = target_art_layer
    ps.echo(f"Current active layer: {target_art_layer.name}")
    
    # Create different selection areas for different effects
    sel_area1 = ((0, 0), (100, 0), (100, 100), (0, 100))
    sel_area2 = ((120, 20), (210, 20), (210, 110), (120, 110))
    sel_area3 = ((220, 20), (310, 20), (310, 110), (220, 110))
    sel_area4 = ((0, 120), (100, 120), (100, 210), (0, 210))
    
    try:
        # Apply Gaussian Blur to first area
        doc_ref.selection.select(sel_area1, SelectionType.ReplaceSelection, 0, False)
        target_art_layer.applyGaussianBlur(2.5)
        ps.echo("Applied Gaussian Blur")
        
        # Apply Add Noise to second area
        doc_ref.selection.select(sel_area2, SelectionType.ReplaceSelection, 0, False)
        target_art_layer.applyAddNoise(15.0, NoiseDistribution.GaussianNoise, True)
        ps.echo("Applied Add Noise")
        
        # Apply Diffuse Glow to third area
        doc_ref.selection.select(sel_area3, SelectionType.ReplaceSelection, 0, False)
        target_art_layer.applyDiffuseGlow(9, 12, 15)
        ps.echo("Applied Diffuse Glow")
        
        # Apply Glass Effect to fourth area
        doc_ref.selection.select(sel_area4, SelectionType.ReplaceSelection, 0, False)
        # Apply Glass Effect using JavaScript
        js_code = """
        try {
            var desc = new ActionDescriptor();
            desc.putInteger(charIDToTypeID("Dstn"), 7);    // Distortion
            desc.putInteger(charIDToTypeID("Smth"), 3);    // Smoothness
            desc.putInteger(charIDToTypeID("Scl "), 7);    // Scaling
            desc.putBoolean(charIDToTypeID("Invr"), false); // Invert
            desc.putInteger(charIDToTypeID("TxtT"), 1);    // Texture Type
            executeAction(charIDToTypeID("GlsE"), desc, DialogModes.NO);
        } catch (e) {
            alert("Error: " + e);
        }
        """
        app.doJavaScript(js_code)
        ps.echo("Applied Glass Effect")
        
        # Apply Crystallize filter to a new area
        sel_area5 = ((120, 120), (210, 120), (210, 210), (120, 210))
        doc_ref.selection.select(sel_area5, SelectionType.ReplaceSelection, 0, False)
        
        # Apply Crystallize filter using JavaScript
        js_code = """
        try {
            var desc = new ActionDescriptor();
            desc.putInteger(charIDToTypeID("ClSz"), 15);  // Cell size 15
            executeAction(charIDToTypeID("Crst"), desc, DialogModes.NO);
        } catch (e) {
            alert("Error: " + e);
        }
        """
        app.doJavaScript(js_code)
        ps.echo("Applied Crystallize filter")
        
        # Apply Motion Blur to a new area
        sel_area6 = ((220, 120), (310, 120), (310, 210), (220, 210))
        doc_ref.selection.select(sel_area6, SelectionType.ReplaceSelection, 0, False)
        
        # Apply Motion Blur using JavaScript
        js_code = """
        try {
            var desc = new ActionDescriptor();
            desc.putInteger(charIDToTypeID("Angl"), 45);    // Angle
            desc.putInteger(charIDToTypeID("Dst "), 20);    // Distance
            executeAction(charIDToTypeID("MtnB"), desc, DialogModes.NO);
        } catch (e) {
            alert("Error: " + e);
        }
        """
        app.doJavaScript(js_code)
        ps.echo("Applied Motion Blur")
        
    except Exception as e:
        ps.echo(f"Error: {e!s}")
    finally:
        # Deselect all
        doc_ref.selection.deselect()
        ps.echo("All filters applied successfully.")

        # Set ruler units back the way we found it
        if start_ruler_units is not PS_PIXELS:
            app.preferences.rulerUnits = start_ruler_units
