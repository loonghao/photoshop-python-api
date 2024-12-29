"""Example of rotating layers in Photoshop.

This example demonstrates how to:
1. Rotate layers by specific angles
2. Apply different rotation methods
3. Handle layer transformations
4. Preserve layer properties during rotation

Key concepts:
- Layer rotation
- Transform operations
- Angle calculations
- Layer positioning
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    layer = doc.activeLayer
    
    # Store original bounds
    bounds = layer.bounds
    
    # Calculate center point
    center_x = (bounds[0] + bounds[2]) / 2
    center_y = (bounds[1] + bounds[3]) / 2
    
    # Rotate layer by 45 degrees
    layer.rotate(45.0, ps.AnchorPosition.MiddleCenter)
    
    # Create new layer and rotate it
    new_layer = doc.artLayers.add()
    new_layer.name = "Rotated Layer"
    
    # Rotate new layer by 90 degrees
    new_layer.rotate(90.0, ps.AnchorPosition.MiddleCenter)
    
    # Move layer to original center
    new_layer.translate(center_x - new_layer.bounds[0],
                       center_y - new_layer.bounds[1])
