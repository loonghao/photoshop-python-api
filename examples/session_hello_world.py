"""Add slate information dynamically."""

# Import built-in modules
import os
from tempfile import mkdtemp

# Import local modules
from photoshop import Session


with Session() as adobe:
    doc = adobe.app.documents.add(2000, 2000)
    text_color = adobe.SolidColor()
    text_color.rgb.red = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = adobe.LayerKind.TextLayer
    new_text_layer.textItem.contents = "Hello, World!"
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = adobe.JPEGSaveOptions(quality=1)
    jpg_file = os.path.join(mkdtemp("photoshop-python-api"), "hello_world.jpg")
    doc.saveAs(jpg_file, options, asCopy=True)
    adobe.app.doJavaScript(f'alert("save to jpg: {jpg_file}")')
