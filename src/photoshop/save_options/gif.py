# Import local modules
from photoshop._core import Photoshop


class GIFSaveOptions(Photoshop):
    object_name = 'GIFSaveOptions'

    def __init__(self):
        super().__init__()
