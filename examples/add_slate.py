"""Add slate information dynamically.

- Open template.
- Update info.
- Save as jpg.
- Close current document.

"""

from datetime import datetime
import os

from photoshop import Session

slate_template = os.path.join(os.path.dirname(__file__), "slate_template.psd")
with Session(slate_template, action="open", auto_close=True) as ps:
    layer_set = ps.active_document.layerSets.getByName("template")

    data = {
        "project name": "test_project",
        "datetime": datetime.today().strftime('%Y-%m-%d')
    }
    for layer in layer_set.layers:
        if layer.kind == "TextLayer":
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    jpg_file = "d:/photoshop_slate.jpg"
    ps.active_document.saveAs(jpg_file, ps.JPEGSaveOptions())
    os.startfile(jpg_file)
