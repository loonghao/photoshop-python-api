"""Example of working with layer sets (groups) in Photoshop.

This example demonstrates how to:
1. Create and manage layer groups
2. Add layers to groups
3. Organize layer hierarchy
4. Handle group properties

Key concepts:
- Layer groups
- Layer organization
- Group properties
- Layer hierarchy
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create a new layer group
    main_group = doc.layerSets.add()
    main_group.name = "Main Group"
    
    # Create a nested group
    sub_group = main_group.layerSets.add()
    sub_group.name = "Sub Group"
    
    # Add layers to groups
    layer1 = main_group.artLayers.add()
    layer1.name = "Layer in Main"
    
    layer2 = sub_group.artLayers.add()
    layer2.name = "Layer in Sub"
    
    # Set group properties
    main_group.visible = True
    main_group.opacity = 80
    
    # List layers in groups
    for layer in main_group.layers:
        ps.echo(f"Layer in main group: {layer.name}")
        
    for layer in sub_group.layers:
        ps.echo(f"Layer in sub group: {layer.name}")
    
    # Move a layer between groups
    layer1.move(sub_group, ps.ElementPlacement.INSIDE)
