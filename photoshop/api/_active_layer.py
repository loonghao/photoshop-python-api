# Import local modules
from photoshop.api._core import Photoshop


class ActiveLayer(Photoshop):
    def __int__(self):
        super().__init__()

    @property
    def name(self) -> str:
        return self.active_layer.Typename

    def add(self):
        self.app.ActiveDocument.ArtLayers.Add()
