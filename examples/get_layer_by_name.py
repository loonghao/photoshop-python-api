# Import third-party modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import local modules


PSD_FILE = psd.get_psd_files()

psd_file = PSD_FILE["export_layers_as_png.psd"]
with Session(psd_file, action="open", auto_close=True) as ps:
    art_layer = ps.active_document.artLayers.getByName("blue")
    assert art_layer.name == "blue"
