# Import local modules
from photoshop_python_api.core import Core


class ArtLayers(Core):
    def __init__(self):
        super(ArtLayers, self).__init__()

    @property
    def art_layers(self):
        return self.ps.ActiveDocument.ArtLayers

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
