# Import local modules
from photoshop_python_api._core import Photoshop


class PDFSaveOptions(Photoshop):
    object_name = "PDFSaveOptions"

    def __init__(self):
        super(PDFSaveOptions, self).__init__()
