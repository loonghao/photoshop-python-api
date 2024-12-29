"""Example of exporting individual layers as PNG files.

This example demonstrates how to:
1. Export each layer of a document as a separate PNG file
2. Handle layer visibility during export
3. Manage layer selection and activation
4. Configure export settings for PNG format

Key concepts:
- Layer iteration
- Visibility management
- PNG export settings
- File naming conventions
- Layer selection
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Store original layer visibilities
    layer_visibilities = []
    for layer in doc.layers:
        layer_visibilities.append(layer.visible)
        layer.visible = False
    
    try:
        # Export each layer individually
        for i, layer in enumerate(doc.layers):
            # Show only current layer
            layer.visible = True
            
            # Configure PNG save options
            options = ps.PNGSaveOptions()
            options.interlaced = False
            
            # Generate unique filename for each layer
            file_path = os.path.join(
                os.path.dirname(__file__),
                f"layer_{i}_{layer.name}.png"
            )
            
            # Save the file
            doc.saveAs(file_path, options, True)
            
            # Hide the layer again
            layer.visible = False
    
    finally:
        # Restore original layer visibilities
        for layer, visibility in zip(doc.layers, layer_visibilities):
            layer.visible = visibility
