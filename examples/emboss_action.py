"""Example of applying emboss effect in Photoshop.

This script demonstrates how to:
1. Create a sample document
2. Create a solid color fill layer
3. Apply emboss effect
4. Save the result
"""

from __future__ import annotations

import os
from tempfile import mkdtemp
from typing import Any

from photoshop import Session

def create_sample_document(ps: Session) -> Any:
    """Create a sample document to work with.
    
    Args:
        ps: Photoshop session instance
        
    Returns:
        The created document
    """
    # Create new document
    doc = ps.app.documents.add(
        width=800,
        height=600,
        resolution=72,
        name="Emboss Example",
    )
    return doc

def create_color_fill_layer(ps: Session, color: tuple[int, int, int]) -> None:
    """Create a solid color fill layer with specified RGB values.
    
    Args:
        ps: Photoshop session instance
        color: Tuple of (red, green, blue) values (0-255)
    """
    js_code = f"""
    try {{
        // Create solid color fill layer
        var doc = app.activeDocument;
        var layer = doc.artLayers.add();
        
        // Create color
        var solidColor = new SolidColor();
        solidColor.rgb.red = {color[0]};
        solidColor.rgb.green = {color[1]};
        solidColor.rgb.blue = {color[2]};
        
        // Fill layer with color
        doc.selection.selectAll();
        doc.selection.fill(solidColor);
        doc.selection.deselect();
        
        "success"
    }} catch(e) {{
        e.message
    }}
    """
    result = ps.app.doJavaScript(js_code)
    if result == "success":
        print("Created color fill layer")
    else:
        print(f"Error creating color fill layer: {result}")

def apply_emboss_effect(ps: Session) -> None:
    """Apply emboss effect to the current layer.
    
    Args:
        ps: Photoshop session instance
    """
    js_code = """
    try {
        // Get the active layer
        var doc = app.activeDocument;
        var layer = doc.activeLayer;
        
        // Apply emboss effect
        var desc = new ActionDescriptor();
        var ref = new ActionReference();
        ref.putProperty(charIDToTypeID("Prpr"), stringIDToTypeID("layerEffects"));
        ref.putEnumerated(charIDToTypeID("Lyr "), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
        desc.putReference(charIDToTypeID("null"), ref);
        
        var edesc = new ActionDescriptor();
        var effects = new ActionDescriptor();
        var bevl = new ActionDescriptor();
        
        bevl.putEnumerated(stringIDToTypeID("bevelStyle"), stringIDToTypeID("bevelStyle"), stringIDToTypeID("emboss"));
        bevl.putEnumerated(stringIDToTypeID("bevelTechnique"), stringIDToTypeID("bevelTechnique"), stringIDToTypeID("softMatte"));
        bevl.putUnitDouble(stringIDToTypeID("depth"), charIDToTypeID("#Prc"), 100);
        bevl.putUnitDouble(stringIDToTypeID("size"), charIDToTypeID("#Pxl"), 10);
        bevl.putUnitDouble(stringIDToTypeID("angle"), charIDToTypeID("#Ang"), 45);
        bevl.putUnitDouble(stringIDToTypeID("altitude"), charIDToTypeID("#Ang"), 30);
        bevl.putBoolean(stringIDToTypeID("useGlobalLight"), true);
        bevl.putUnitDouble(stringIDToTypeID("soften"), charIDToTypeID("#Pxl"), 0);
        
        effects.putObject(stringIDToTypeID("bevelEmboss"), stringIDToTypeID("bevelEmboss"), bevl);
        edesc.putObject(stringIDToTypeID("layerEffects"), stringIDToTypeID("layerEffects"), effects);
        desc.putObject(charIDToTypeID("T   "), stringIDToTypeID("layerEffects"), edesc);
        
        executeAction(charIDToTypeID("setd"), desc, DialogModes.NO);
        
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js_code)
    if result == "success":
        print("Applied emboss effect")
    else:
        print(f"Error applying emboss effect: {result}")

def main() -> None:
    """Create a document with embossed effect.
    
    This function demonstrates how to:
    1. Create a sample document
    2. Create a solid color fill layer
    3. Apply emboss effect
    4. Save the result
    """
    with Session() as ps:
        try:
            # Create sample document
            doc = create_sample_document(ps)
            print("Created sample document")
            
            # Create color fill layer
            create_color_fill_layer(ps, (100, 150, 200))
            
            # Apply emboss effect
            apply_emboss_effect(ps)
            
            # Save the document
            temp_dir = mkdtemp()
            output_path = os.path.join(temp_dir, "emboss_example.psd")
            doc.saveAs(output_path, ps.PhotoshopSaveOptions())
            print(f"\nDocument saved to: {output_path}")
        
        finally:
            if doc:
                try:
                    doc.close()
                except Exception as e:
                    print(f"Warning: Error while closing document - {e}")

if __name__ == "__main__":
    main()
