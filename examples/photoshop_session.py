"""Add slate information dynamically。"""

from datetime import datetime
import os

from photoshop import Session

file_path = os.path.join(os.path.dirname(__file__), "slate_template.psd")

with Session(file_path, "open") as adobe:
    layer_set = adobe.active_document.layerSets.getByName("template")
    data = {
        "project name": "test_project",
        "datetime": datetime.today().strftime('%Y-%m-%d')
    }
    for layer in layer_set.layers:
        if layer.kind == "TextLayer":
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    jpg_file = "d:/photoshop_slate.jpg"
    adobe.active_document.saveAs(jpg_file, adobe.JPEGSaveOptions())
    os.startfile(jpg_file)
    adobe.active_document.close()
