from photoshop._core import Photoshop
from photoshop.artlayer import ArtLayer


class Layers(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return [layer for layer in self.app]

    def __getitem__(self, key):
        return ArtLayer(self._layers[key])

    def __len__(self):
        return self.length

    @property
    def length(self):
        return len(self._layers)

    def removeAll(self):
        print([layer.name for layer in self.app])

    def item(self, index):
        return ArtLayer(self.app.item(index))
