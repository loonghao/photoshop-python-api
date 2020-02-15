from photoshop_python_api import LayerKind
from photoshop_python_api.application import Application
from photoshop_python_api.save_options import JPEGSaveOptions
from photoshop_python_api.solid_color import SolidColor


def hello_world():
    app = Application()
    doc = app.documents.add()
    new_doc = doc.artLayers.add()
    text_color = SolidColor()
    text_color.rgb.red = 225
    text_color.rgb.green = 0
    text_color.rgb.blue = 0
    new_text_layer = new_doc
    new_text_layer.kind = LayerKind.BRIGHTNESSCONTRAST
    new_text_layer.textItem.contents = 'Hello, World!'
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = JPEGSaveOptions()
    options.quality = 10
    # # save to jpg
    jpg = 'd:/hello_world.jpg'
    doc.saveAs(jpg, options, as_copy=True)
    app.eval_javascript(f'alert("save to jpg: {jpg}")')


if __name__ == '__main__':
    hello_world()
