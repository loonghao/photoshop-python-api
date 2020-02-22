import photoshop as ps

# Get photoshop instance.
app = ps.Application()
# Get current active document.
doc = app.activeDocument

# Add a solid color.
textColor = ps.SolidColor()
textColor.rgb.red = 43.0
textColor.rgb.green = 197.0
textColor.rgb.blue = 0.0

# Create empty layer.
new_text_layer = doc.artLayers.add()
# Set empty layer type to text layer
new_text_layer.kind = ps.LayerKind.TextLayer
# Set current text layer contents to "Hello, World!".
new_text_layer.textItem.contents = 'Hello, World!'
# Change current text layer position.
new_text_layer.textItem.position = [160, 167]
# Change current text layer text size.
new_text_layer.textItem.size = 36
# Change current text layer color.
new_text_layer.textItem.color = textColor
