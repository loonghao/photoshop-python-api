import photoshop as ps


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
    jpg = "d:/hello_world.jpg"
    doc.saveAs(jpg, options, asCopy=True)
    app.doJavaScript(f'alert("save to jpg: {jpg}")')


if __name__ == "__main__":
    hello_world()
