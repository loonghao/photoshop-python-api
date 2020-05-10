"""Add slate information dynamically.

- Open template.
- Update info.
- Save as jpg.
- Close current document.

"""

import os
from datetime import datetime

from photoshop import Session

import examples._psd_files as psd  # Import from examples.

PSD_FILE = psd.get_psd_files()
print(PSD_FILE)
slate_template = PSD_FILE["slate_template.psd"]
with Session(slate_template, action="open", auto_close=True) as ps:
    layer_set = ps.active_document.layerSets.getByName("template")

    data = {
        "project name": "test_project",
        "datetime": datetime.today().strftime("%Y-%m-%d"),
    }
    for layer in layer_set.layers:
        if layer.kind == "TextLayer":
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    jpg_file = "d:/photoshop_slate.jpg"
    ps.active_document.saveAs(jpg_file, ps.JPEGSaveOptions())
    os.startfile(jpg_file)
