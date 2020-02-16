# Import local modules
from photoshop._core import Photoshop


class EPSSaveOptions(Photoshop):
    object_name = 'EPSSaveOptions'

    def __init__(self):
        super().__init__()
