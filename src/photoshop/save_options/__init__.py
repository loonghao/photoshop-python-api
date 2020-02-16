from photoshop.save_options.gif import GIFSaveOptions
from photoshop.save_options.jpg import JPEGSaveOptions
from photoshop.save_options.pdf import PDFSaveOptions
from photoshop.save_options.png import ExportOptionsSaveForWeb
from photoshop.save_options.png import PNGSaveOptions
from photoshop.save_options.psd import PhotoshopSaveOptions
from photoshop.save_options.tif import TiffSaveOptions

# Do not save changes.
DONOTSAVECHANGES = 2
# Ask the user whether to save.
PROMPTTOSAVECHANGES = 1
# Save changes.
SAVECHANGES = 3

__all__ = [
    'GIFSaveOptions',
    'JPEGSaveOptions',
    'PDFSaveOptions',
    'ExportOptionsSaveForWeb',
    'PNGSaveOptions',
    'PhotoshopSaveOptions',
    'TiffSaveOptions',
]
