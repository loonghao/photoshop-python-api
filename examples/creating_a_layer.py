"""Example of creating and manipulating layers in Photoshop.

This script demonstrates various layer operations:
1. Creating different types of layers (normal, text, shape)
2. Setting layer properties (opacity, blend mode)
3. Working with layer groups
4. Applying layer effects
"""

# Import built-in modules
from __future__ import annotations
import os
from tempfile import mkdtemp

# Import local modules
from photoshop import Session
from photoshop.api import enumerations

def create_sample_document(ps, width=800, height=600, name="Layer Example"):
    """Create a sample document for layer operations.

    Args:
        ps: Photoshop session object
        width: Document width in pixels
        height: Document height in pixels
        name: Document name
    """
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=72.0,
        name=name,
        mode=enumerations.NewDocumentMode.NewRGB,
        initialFill=enumerations.DocumentFill.White,
    )
    return doc

def create_background_layer(ps, document, color=(222, 0, 0)):
    """Create a background layer with specified color.

    Args:
        ps: Photoshop session object
        document: Target document
        color: RGB color tuple
    """
    # Create color object
    fill_color = ps.SolidColor()
    fill_color.rgb.red = color[0]
    fill_color.rgb.green = color[1]
    fill_color.rgb.blue = color[2]

    # Add background layer
    layer = document.artLayers.add()
    layer.name = "Background"

    # Fill layer with color
    document.selection.selectAll()
    document.selection.fill(fill_color)
    document.selection.deselect()

    return layer

def create_text_layer(ps, document, text="Sample Text", position=(100, 100)):
    """Create a text layer with specified text and position.

    Args:
        ps: Photoshop session object
        document: Target document
        text: Text content
        position: (x, y) position tuple
    """
    # Add text layer
    text_layer = document.artLayers.add()
    text_layer.kind = enumerations.LayerKind.TextLayer
    text_layer.name = "Text Layer"

    # Set text properties
    text_item = text_layer.textItem
    text_item.contents = text
    text_item.position = position
    text_item.size = 48  # Point size

    # Set text color using JavaScript
    js_code = """
    try {
        var doc = app.activeDocument;
        var layer = doc.layers.getByName("Text Layer");
        var color = new SolidColor();
        color.rgb.red = 255;
        color.rgb.green = 255;
        color.rgb.blue = 255;
        layer.textItem.color = color;
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js_code)
    if result != "success":
        print(f"Warning: Text color setting failed - {result}")

    return text_layer

def create_shape_layer(ps, document):
    """Create a shape layer with a rectangle.

    Args:
        ps: Photoshop session object
        document: Target document
    """
    # Draw rectangle using JavaScript
    js_code = """
    try {
        var doc = app.activeDocument;
        
        // Create a new shape layer
        var layer = doc.artLayers.add();
        layer.name = "Shape Layer";
        
        // Set layer properties
        var color = new SolidColor();
        color.rgb.red = 0;
        color.rgb.green = 255;
        color.rgb.blue = 0;
        
        // Create rectangle shape
        var startRulerUnits = app.preferences.rulerUnits;
        var startTypeUnits = app.preferences.typeUnits;
        app.preferences.rulerUnits = Units.PIXELS;
        app.preferences.typeUnits = TypeUnits.PIXELS;
        
        // Create shape
        var shapeRef = [
            [300, 200],
            [500, 200],
            [500, 400],
            [300, 400]
        ];
        
        // Create the shape
        doc.selection.select(shapeRef);
        doc.selection.fill(color);
        doc.selection.deselect();
        
        // Restore preferences
        app.preferences.rulerUnits = startRulerUnits;
        app.preferences.typeUnits = startTypeUnits;
        
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js_code)
    if result != "success":
        print(f"Warning: Shape creation failed - {result}")
        return None

    # Get the created layer
    shape_layer = document.artLayers.getByName("Shape Layer")
    return shape_layer

def create_layer_group(document, name="Layer Group"):
    """Create a layer group.

    Args:
        document: Target document
        name: Group name
    """
    group = document.layerSets.add()
    group.name = name
    return group

def apply_layer_style(ps, layer):
    """Apply some layer styles.

    Args:
        ps: Photoshop session object
        layer: Target layer
    """
    # Apply drop shadow using JavaScript
    js_code = """
    try {
        var doc = app.activeDocument;
        var layer = doc.activeLayer;
        
        // Create drop shadow
        var idsetd = charIDToTypeID("setd");
        var desc = new ActionDescriptor();
        var idnull = charIDToTypeID("null");
        var ref = new ActionReference();
        var idPrpr = charIDToTypeID("Prpr");
        var idLefx = charIDToTypeID("Lefx");
        ref.putProperty(idPrpr, idLefx);
        ref.putEnumerated(charIDToTypeID("Lyr "), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
        desc.putReference(idnull, ref);
        var idT = charIDToTypeID("T   ");
        var desc2 = new ActionDescriptor();
        var idScl = charIDToTypeID("Scl ");
        desc2.putUnitDouble(idScl, charIDToTypeID("#Prc"), 100);
        var idDrSh = charIDToTypeID("DrSh");
        var desc3 = new ActionDescriptor();
        var idenab = charIDToTypeID("enab");
        desc3.putBoolean(idenab, true);
        var idMd = charIDToTypeID("Md  ");
        var idBlnM = charIDToTypeID("BlnM");
        var idMltp = charIDToTypeID("Mltp");
        desc3.putEnumerated(idMd, idBlnM, idMltp);
        var idClr = charIDToTypeID("Clr ");
        var desc4 = new ActionDescriptor();
        var idRd = charIDToTypeID("Rd  ");
        desc4.putDouble(idRd, 0);
        var idGrn = charIDToTypeID("Grn ");
        desc4.putDouble(idGrn, 0);
        var idBl = charIDToTypeID("Bl  ");
        desc4.putDouble(idBl, 0);
        var idRGBC = charIDToTypeID("RGBC");
        desc3.putObject(idClr, idRGBC, desc4);
        var idOpct = charIDToTypeID("Opct");
        desc3.putUnitDouble(idOpct, charIDToTypeID("#Prc"), 75);
        var iduglg = charIDToTypeID("uglg");
        desc3.putBoolean(iduglg, true);
        var idlagl = charIDToTypeID("lagl");
        desc3.putDouble(idlagl, 120);
        var idDstn = charIDToTypeID("Dstn");
        desc3.putUnitDouble(idDstn, charIDToTypeID("#Pxl"), 10);
        var idCkmt = charIDToTypeID("Ckmt");
        desc3.putUnitDouble(idCkmt, charIDToTypeID("#Pxl"), 0);
        var idblur = charIDToTypeID("blur");
        desc3.putUnitDouble(idblur, charIDToTypeID("#Pxl"), 10);
        var idNose = charIDToTypeID("Nose");
        desc3.putUnitDouble(idNose, charIDToTypeID("#Prc"), 0);
        var idAntA = charIDToTypeID("AntA");
        desc3.putBoolean(idAntA, false);
        desc2.putObject(idDrSh, idDrSh, desc3);
        var idLefx = charIDToTypeID("Lefx");
        desc.putObject(idT, idLefx, desc2);
        executeAction(idsetd, desc, DialogModes.NO);
        "success"
    } catch(e) {
        e.message
    }
    """
    # Make sure the layer is active
    ps.app.activeDocument.activeLayer = layer

    # Apply the style
    result = ps.app.doJavaScript(js_code)
    if result != "success":
        print(f"Warning: Layer style application failed - {result}")

def main():
    """Run the example script."""
    with Session() as ps:
        try:
            # Create new document
            doc = create_sample_document(ps)
            print("Created new document")

            # Create background layer
            bg_layer = create_background_layer(ps, doc)
            print("Created background layer")

            # Create layer group
            group = create_layer_group(doc, "Content")
            print("Created layer group")

            # Create text layer
            text_layer = create_text_layer(ps, doc)
            text_layer.move(group, enumerations.ElementPlacement.PlaceInside)
            print("Created text layer")

            # Create shape layer
            shape_layer = create_shape_layer(ps, doc)
            shape_layer.move(group, enumerations.ElementPlacement.PlaceInside)
            print("Created shape layer")

            # Apply layer styles
            apply_layer_style(ps, text_layer)
            print("Applied layer styles")

            # Save the document
            temp_dir = mkdtemp()
            output_path = os.path.join(temp_dir, "layer_example.psd")
            doc.saveAs(output_path, ps.PhotoshopSaveOptions())
            print(f"\nDocument saved to: {output_path}")

        finally:
            if doc:
                doc.close()

if __name__ == "__main__":
    main()
