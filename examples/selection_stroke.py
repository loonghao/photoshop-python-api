"""Example of creating and modifying selection strokes in Photoshop.

This example demonstrates how to:
1. Create selections with specific shapes
2. Apply strokes to selections
3. Configure stroke options
4. Work with stroke colors and widths

Key concepts:
- Selection creation
- Stroke application
- Stroke customization
- Color management
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create a rectangular selection
    doc.selection.select([
        [100, 100],
        [400, 100],
        [400, 300],
        [100, 300]
    ])
    
    # Create stroke color
    stroke_color = ps.SolidColor()
    stroke_color.rgb.red = 255
    stroke_color.rgb.green = 0
    stroke_color.rgb.blue = 0
    
    # Apply stroke to selection
    doc.selection.stroke(
        stroke_color,  # Color to use
        width=2,      # Stroke width in pixels
        location=ps.StrokeLocation.Inside,
        blendMode=ps.ColorBlendMode.Normal,
        opacity=100
    )
    
    # Create circular selection
    doc.selection.selectElliptical(
        left=200,
        top=200,
        width=200,
        height=200
    )
    
    # Change stroke color
    stroke_color.rgb.blue = 255
    
    # Apply different stroke
    doc.selection.stroke(
        stroke_color,
        width=5,
        location=ps.StrokeLocation.Center,
        blendMode=ps.ColorBlendMode.Normal,
        opacity=75
    )
    
    # Clear selection
    doc.selection.deselect()
