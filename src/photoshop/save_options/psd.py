# Import local modules
from photoshop._core import Photoshop


class PhotoshopSaveOptions(Photoshop):

    def __int__(self):
        super().__init__()
        # If true, the alpha channels are saved.
        self.AlphaChannels = False
        # If true, the annotations are save
        self.AnnotationsProperty = False
        self.Layers = True
