# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layer import ArtLayer


class ArtLayers(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return [layer for layer in self.app]

    @property
    def length(self):
        return len(self._layers)

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(self):
        """Adds an element."""
        return ArtLayer(self.app.add())

    def getByName(self, name):
        return self.app.getByName(name)

    def removeAll(self):
        return self.app.removeAll()

    def link(self, layer):
        self.app.link(layer)
