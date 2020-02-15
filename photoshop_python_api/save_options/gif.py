# Import local modules
from photoshop_python_api._core import Photoshop


class GIFSaveOptions(Photoshop):
    object_name = "GIFSaveOptions"

    def __init__(self):
        super(GIFSaveOptions, self).__init__()
