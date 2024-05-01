"""A trim example."""
# Import third-party modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import local modules


PSD_FILE = psd.get_psd_files()
example_file = PSD_FILE["trim.psd"]
with Session(example_file, action="open") as ps:
    ps.active_document.trim(ps.TrimType.TopLeftPixel, True, True, True, True)
