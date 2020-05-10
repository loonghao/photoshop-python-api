# Import local modules
from .._core import Photoshop


class PDFSaveOptions(Photoshop):
    object_name = "PDFSaveOptions"

    def __init__(self):
        super().__init__()
