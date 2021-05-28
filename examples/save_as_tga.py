# Import built-in modules
import os
from tempfile import mkdtemp

# Import local modules
from photoshop import Session


with Session(action="new_document") as ps:
    doc = ps.active_document
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    text_color.rgb.red = 0
    text_color.rgb.blue = 0
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = "Hello, World!"
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    tga_file = os.path.join(mkdtemp("photoshop-python-api"), "test.tga")
    doc.saveAs(tga_file, ps.TargaSaveOptions(), asCopy=True)
    os.startfile(tga_file)
