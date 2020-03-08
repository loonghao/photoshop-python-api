"""Add slate information dynamically。"""

from datetime import datetime
import os

import photoshop as ps

app = ps.Application()
app.load(os.path.join(os.path.dirname(__file__), "slate_template.psd"))
layer_set = app.activeDocument.layerSets.getByName("template")

data = {
    "project name": "test_project",
    "datetime": datetime.today().strftime('%Y-%m-%d')
}
for layer in layer_set.layers:
    if layer.kind == "TextLayer":
        layer.textItem.contents = data[layer.textItem.contents.strip()]

doc = app.activeDocument

jpg_file = "d:/photoshop_slate.jpg"

doc.saveAs(jpg_file, ps.JPEGSaveOptions())

doc.close()

os.startfile(jpg_file)
