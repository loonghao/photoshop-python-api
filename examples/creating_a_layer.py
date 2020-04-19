"""
Let’s get the current document and create a new layer “Background” and fill it
with red color. In order to use the Fill tool we will first select the entire
layer and then fill it with a color.

"""

from photoshop import Session

with Session() as ps:
    document = ps.active_document
    # Create color object of color red.
    fillColor = ps.SolidColor()
    fillColor.rgb.red = 222
    fillColor.rgb.green = 0
    fillColor.rgb.blue = 0
    # Add a new layer called Background.
    layer = document.artLayers.add()
    layer.name = "Background"
    # Select the entire layer.
    document.selection.selectAll()
    # Fill the selection with color.
    document.selection.fill(fillColor)
    # Deselect.
    document.selection.deselect()
