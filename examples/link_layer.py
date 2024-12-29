"""Example of linking layers in Photoshop.

This example demonstrates how to:
1. Link multiple layers together
2. Manage linked layers
3. Check layer link status
4. Modify linked layer properties

Key concepts:
- Layer linking
- Group operations
- Layer management
- Link status
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create test layers
    layer1 = doc.artLayers.add()
    layer1.name = "Layer 1"
    
    layer2 = doc.artLayers.add()
    layer2.name = "Layer 2"
    
    layer3 = doc.artLayers.add()
    layer3.name = "Layer 3"
    
    # Link layers
    layer1.link(layer2)
    layer2.link(layer3)
    
    # Check link status
    ps.echo(f"Layer 1 linked: {layer1.linked}")
    ps.echo(f"Layer 2 linked: {layer2.linked}")
    ps.echo(f"Layer 3 linked: {layer3.linked}")
    
    # Move linked layers together
    layer1.translate(100, 100)
