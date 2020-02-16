# Import local modules
from photoshop._core import Photoshop


class TiffSaveOptions(Photoshop):
    object_name = 'TiffSaveOptions'

    def __int__(self):
        super().__init__()
