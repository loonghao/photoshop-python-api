# Import local modules
from photoshop._core import Photoshop


class PDFSaveOptions(Photoshop):
    object_name = "PDFSaveOptions"

    def __init__(self):
        super().__init__()
