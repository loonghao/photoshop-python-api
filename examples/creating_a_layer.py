"""Example of creating and manipulating layers in Photoshop.

This example demonstrates how to:
1. Create different types of layers
2. Set layer properties and attributes
3. Organize layers in the document
4. Apply basic layer effects

Key concepts:
- Layer creation
- Layer types (art layers, text layers)
- Layer properties
- Layer organization
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create a new art layer
    new_layer = doc.artLayers.add()
    
    # Set layer properties
    new_layer.name = "New Art Layer"
    new_layer.opacity = 75
    new_layer.visible = True
    
    # Create a text layer
    text_layer = doc.artLayers.add()
    text_layer.kind = ps.LayerKind.TextLayer
    
    # Configure text properties
    text_item = text_layer.textItem
    text_item.contents = "Sample Text"
    text_item.size = 72
    text_item.position = [100, 100]
    
    # Move layers in stack
    new_layer.move(text_layer, ps.ElementPlacement.PlaceAfter)
