"""Demonstrate how to add and update slate information in a Photoshop template.

This example shows how to:
1. Open a PSD template file
2. Update text layers with dynamic information
3. Save the result as a JPG file
4. Display the saved file

The script uses a template PSD file that contains text layers within a layer set
named "template". It updates specific text layers with dynamic content like
project name and current date.

Example:
    ```python
    with Session(template_file, action="open") as ps:
        layer_set = ps.active_document.layerSets.getByName("template")
        for layer in layer_set.layers:
            if layer.kind == ps.LayerKind.TextLayer:
                layer.textItem.contents = dynamic_data[layer.textItem.contents]
    ```

Note:
    - Requires a PSD template file with text layers in a layer set named "template"
    - Text layers should have placeholder text matching keys in the data dictionary
    - The script uses os.startfile which is Windows-specific
"""

# Import built-in modules
from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path
from tempfile import mkdtemp

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session

# Get path to template PSD file
PSD_FILE = psd.get_psd_files()
slate_template = PSD_FILE["slate_template.psd"]

# Open template file in Photoshop
with Session(slate_template, action="open", auto_close=True) as ps:
    # Get the layer set named "template"
    layer_set = ps.active_document.layerSets.getByName("template")

    # Prepare dynamic data for text layers
    data = {
        "project name": "test_project",
        "datetime": datetime.now(tz=timezone.utc).strftime("%Y-%m-%d"),
    }
    
    # Update text layers with dynamic content
    for layer in layer_set.layers:
        if layer.kind == ps.LayerKind.TextLayer:
            layer.textItem.contents = data[layer.textItem.contents.strip()]

    # Save the document as JPG in a temporary directory
    jpg_file = Path(mkdtemp("photoshop-python-api")) / "slate.jpg"
    ps.active_document.saveAs(str(jpg_file), ps.JPEGSaveOptions())
    ps.echo(f"Save jpg to {jpg_file}")
    
    # Open the saved JPG file (Windows-specific)
    # Note: os.startfile is Windows-specific, consider using a cross-platform solution
    os.startfile(str(jpg_file))
