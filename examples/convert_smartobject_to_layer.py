"""Example of converting a smart object to a regular layer in Photoshop.

This script demonstrates how to:
1. Create a smart object from a regular layer
2. Convert a smart object back to a regular layer
3. Handle multiple selected layers
4. Provide visual feedback about the conversion process

Module Attributes:
    None

Module Classes:
    None

Module Functions:
    create_sample_document() -> None
    convert_to_smart_object() -> None
    convert_to_layer() -> None
    main() -> None
"""

# Import local modules
from __future__ import annotations
import time

from photoshop import Session
from photoshop.api.enumerations import NewDocumentMode, DocumentFill, LayerKind

def create_sample_document(ps) -> None:
    """Create a sample document with multiple layers.
    
    Args:
        ps: Photoshop session object
    """
    # Create a new document
    doc = ps.app.documents.add(
        width=500,
        height=300,
        resolution=72,
        name="Smart Object Demo",
        mode=NewDocumentMode.NewRGB,
        initialFill=DocumentFill.White,
    )
    
    # Create some sample layers
    colors = [
        ("Red Layer", (255, 0, 0)),
        ("Green Layer", (0, 255, 0)),
        ("Blue Layer", (0, 0, 255)),
    ]
    
    for name, (r, g, b) in colors:
        # Create a new layer
        layer = doc.artLayers.add()
        layer.name = name
        
        # Set layer fill color
        color = ps.SolidColor()
        color.rgb.red = r
        color.rgb.green = g
        color.rgb.blue = b
        
        # Create a rectangle selection
        doc.selection.select([
            [100, 100],
            [400, 100],
            [400, 200],
            [100, 200],
        ])
        
        # Fill the selection with color
        ps.app.foregroundColor = color
        doc.selection.fill(ps.app.foregroundColor)
        doc.selection.deselect()
    
    print("Created sample document with three colored layers")

def convert_to_smart_object(ps) -> bool:
    """Convert selected layers to a smart object using JavaScript.
    
    Args:
        ps: Photoshop session object
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    js = """
    try {
        var idnewPlacedLayer = stringIDToTypeID("newPlacedLayer");
        executeAction(idnewPlacedLayer, undefined, DialogModes.NO);
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js)
    success = result == "success"
    print(f"Smart Object conversion: {'Successful' if success else 'Failed'}")
    return success

def convert_to_layer(ps) -> None:
    """Convert smart object back to regular layer using JavaScript.
    
    Args:
        ps: Photoshop session object
    """
    js = """
    try {
        var idplacedLayerConvertToLayers = stringIDToTypeID("placedLayerConvertToLayers");
        executeAction(idplacedLayerConvertToLayers, undefined, DialogModes.NO);
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js)
    print(f"Regular Layer conversion: {'Successful' if result == 'success' else 'Failed - ' + str(result)}")

def main() -> None:
    """Run the example script.
    
    This function demonstrates the complete workflow:
    1. Create a sample document with multiple layers
    2. Convert layers to smart object
    3. Convert smart object back to regular layer
    
    Returns:
        None
    """
    with Session() as ps:
        # Step 1: Create sample document
        create_sample_document(ps)
        
        # Step 2: Select all layers except background
        doc = ps.active_document
        for layer in doc.artLayers:
            if layer.name != "Background":
                layer.selected = True
        print("\nSelected all non-background layers")
        
        # Step 3: Convert to Smart Object
        print("\nConverting to Smart Object...")
        if convert_to_smart_object(ps):
            # Wait a moment to ensure Photoshop has processed the smart object
            time.sleep(0.5)
            
            # Step 4: Convert back to regular layer
            print("\nConverting back to regular layer...")
            convert_to_layer(ps)
        
        print("\nProcess completed! Check the layers panel in Photoshop.")
        print("The document contains the following layers:")
        for i, layer in enumerate(doc.artLayers, 1):
            print(f"{i}. {layer.name} ({LayerKind(layer.kind).name})")

if __name__ == "__main__":
    main()
