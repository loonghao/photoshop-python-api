"""Add slate information dynamically.

- Open template.
- Update info.
- Save as jpg.
- Close current document.

"""
# Import built-in modules
import os
from datetime import datetime
from tempfile import mkdtemp

import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import third-party modules
# Import local modules


PSD_FILE = psd.get_psd_files()
slate_template = PSD_FILE["slate_template.psd"]
with Session(slate_template, action="open", auto_close=True) as ps:
    layer_set = ps.active_document.layerSets.getByName("template")

    data = {
        "project name": "test_project",
        "datetime": datetime.today().strftime("%Y-%m-%d"),
    }
    for layer in layer_set.layers:
        if layer.kind == ps.LayerKind.TextLayer:
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    jpg_file = os.path.join(mkdtemp("photoshop-python-api"), "slate.jpg")
    ps.active_document.saveAs(jpg_file, ps.JPEGSaveOptions())
    print(f"Save jpg to {jpg_file}")
    os.startfile(jpg_file)
