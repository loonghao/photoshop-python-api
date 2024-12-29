"""Example of moving layers to different positions in the layer stack.

This example demonstrates how to:
1. Move layers within the layer stack
2. Change layer order
3. Handle layer positioning
4. Work with layer groups

Key concepts:
- Layer ordering
- Layer movement
- Stack manipulation
- Layer hierarchy
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create some test layers
    layer1 = doc.artLayers.add()
    layer1.name = "Layer 1"
    
    layer2 = doc.artLayers.add()
    layer2.name = "Layer 2"
    
    layer3 = doc.artLayers.add()
    layer3.name = "Layer 3"
    
    # Move layer1 to the end (bottom) of the stack
    layer1.move(doc.layers[-1], ps.ElementPlacement.PlaceAfter)
    
    # Move layer3 to the beginning (top) of the stack
    layer3.move(doc.layers[0], ps.ElementPlacement.PlaceBefore)
    
    # Move layer2 between layer1 and layer3
    layer2.move(layer1, ps.ElementPlacement.PlaceBefore)
