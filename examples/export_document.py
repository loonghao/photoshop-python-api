# Import built-in modules
import os
from tempfile import mkdtemp

import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import third-party modules
# Import local modules


PSD_FILE = psd.get_psd_files()

if __name__ == "__main__":
    psd_file = PSD_FILE["export_layers_as_png.psd"]
    with Session(psd_file, action="open", auto_close=True) as ps:
        opts = ps.ExportOptionsSaveForWeb()

        png_file = os.path.join(mkdtemp(), "test.png")
        active_document = ps.app.activeDocument
        active_document.exportDocument(png_file, ps.ExportType.SaveForWeb, opts)
        os.startfile(png_file)
