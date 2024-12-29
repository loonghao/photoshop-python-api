"""Add slate information dynamically.

- Open template.
- Update info.
- Save as jpg.
- Close current document.

"""

# Import built-in modules
from __future__ import annotations

import os
from datetime import datetime
from tempfile import mkdtemp
from pathlib import Path
from datetime import timezone

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session

PSD_FILE = psd.get_psd_files()
slate_template = PSD_FILE["slate_template.psd"]
with Session(slate_template, action="open", auto_close=True) as ps:
    layer_set = ps.active_document.layerSets.getByName("template")

    data = {
        "project name": "test_project",
        "datetime": datetime.now(tz=timezone.utc).strftime("%Y-%m-%d"),
    }
    for layer in layer_set.layers:
        if layer.kind == ps.LayerKind.TextLayer:
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    jpg_file = Path(mkdtemp("photoshop-python-api")) / "slate.jpg"
    ps.active_document.saveAs(str(jpg_file), ps.JPEGSaveOptions())
    ps.echo(f"Save jpg to {jpg_file}")
    # Note: os.startfile is Windows-specific, consider using a cross-platform solution
    os.startfile(str(jpg_file))
