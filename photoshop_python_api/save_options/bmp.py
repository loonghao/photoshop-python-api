# Import local modules
from photoshop_python_api._core import Photoshop


class BMPSaveOptions(Photoshop):
    object_name = "BMPSaveOptions"

    def __init__(self):
        super(BMPSaveOptions, self).__init__()
