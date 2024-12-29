"""Example of converting between smart objects and regular layers.

This example demonstrates how to:
1. Convert layers to smart objects
2. Convert smart objects back to regular layers
3. Manage smart object properties
4. Handle smart object conversions

Key concepts:
- Smart Objects
- Layer conversion
- Smart Object properties
- Layer types
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create a new layer
    layer = doc.artLayers.add()
    layer.name = "Test Layer"
    
    # Convert to smart object
    layer.convertToSmartObject()
    ps.echo("Layer converted to Smart Object")
    
    # Check if it's a smart object
    if layer.kind == ps.LayerKind.SmartObject:
        ps.echo("Layer is now a Smart Object")
        
        # Convert back to regular layer
        layer.rasterize(ps.RasterizeType.EntireLayer)
        ps.echo("Smart Object converted back to regular layer")
