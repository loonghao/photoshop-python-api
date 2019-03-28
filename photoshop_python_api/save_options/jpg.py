# Import local modules
from photoshop_python_api._core import Photoshop


class _JPEGSaveOptions(Photoshop):
    object_name = 'JPEGSaveOptions'

    def __init__(self):
        super(_JPEGSaveOptions, self).__init__()


JPEGSaveOptions = _JPEGSaveOptions().app
