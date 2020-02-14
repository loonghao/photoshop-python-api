# Import local modules
from photoshop_python_api._core import Photoshop


class ArtLayer(Photoshop):
    def __init__(self):
        super(ArtLayer, self).__init__()

    @property
    def _artLayer(self):
        return self.app.ArtLayer

    @property
    def fillOpacity(self):
        return self.app.artLayer.fillOpacity

    @property
    def length(self):
        return self.art_layers.length

    @property
    def parent(self):
        return self.art_layers.parent

    @property
    def typename(self):
        return self.art_layers.Typename

    def add(self):
        return self.art_layers.add()

    def get_by_name(self, name):
        return self.art_layers.getByName(name)

    def remove_all(self):
        return self.art_layers.RemoveAll()
