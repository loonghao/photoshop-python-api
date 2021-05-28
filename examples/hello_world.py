# Import built-in modules
import os
from tempfile import mkdtemp

# Import local modules
import photoshop.api as ps


def hello_world():
    app = ps.Application()
    doc = app.documents.add()
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = "Hello, World!"
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = ps.JPEGSaveOptions(quality=5)
    jpg_file = os.path.join(mkdtemp("photoshop-python-api"), "hello_world.jpg")
    doc.saveAs(jpg_file, options, asCopy=True)
    os.startfile(jpg_file)


if __name__ == "__main__":
    hello_world()
