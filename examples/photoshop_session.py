"""Add slate information dynamically。"""

import os
from datetime import datetime

from photoshop import Session

import examples._psd_files as psd  # Import from examples.

PSD_FILE = psd.get_psd_files()
file_path = PSD_FILE["slate_template.psd"]

with Session(file_path, action="open", auto_close=True) as ps:
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
