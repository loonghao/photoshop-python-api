# Import local modules
from photoshop.api._core import Photoshop


class ActiveLayer(Photoshop):
    """The selected layer."""

    def __int__(self):
        super().__init__()

    @property
    def name(self) -> str:
        """The name of the layer."""
        return self.active_layer.Typename

    def add(self):
        """Adds an element."""
        self.app.ActiveDocument.ArtLayers.Add()
