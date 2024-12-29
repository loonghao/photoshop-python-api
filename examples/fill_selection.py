"""Example of filling selections in Photoshop.

This example demonstrates how to:
1. Create and modify selections
2. Fill selections with colors
3. Work with selection options
4. Apply different fill methods

Key concepts:
- Selection tools
- Fill operations
- Color fills
- Selection modification
- Fill opacity and blending
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create a rectangular selection
    doc.selection.select([
        [100, 100],
        [300, 100],
        [300, 200],
        [100, 200]
    ])
    
    # Create fill color
    fill_color = ps.SolidColor()
    fill_color.rgb.red = 255
    fill_color.rgb.green = 0
    fill_color.rgb.blue = 0
    
    # Fill the selection
    doc.selection.fill(fill_color)
    
    # Deselect
    doc.selection.deselect()
    
    # Create another selection and fill with opacity
    doc.selection.select([
        [150, 150],
        [350, 150],
        [350, 250],
        [150, 250]
    ])
    
    fill_color.rgb.blue = 255
    doc.selection.fill(fill_color, ps.ColorBlendMode.Normal, 50)
    
    # Clear selection
    doc.selection.deselect()
