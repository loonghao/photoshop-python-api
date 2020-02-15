# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layer import ArtLayer


class ArtLayers(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def length(self):
        return self.app.length

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(self):
        """Adds an element."""
        return ArtLayer(self.app.add())

    def get_by_name(self, name):
        return self.artLayers.getByName(name)

    def remove_all(self):
        return self.artLayers.RemoveAll()
