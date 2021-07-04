# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop


# pylint: disable=too-many-public-methods
class Layers(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return list(self.app)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        item = self._layers[key]
        return ArtLayer(item)

    @property
    def length(self):
        return len(self._layers)

    def removeAll(self):
        return [layer.name for layer in self.app]

    def item(self, index):
        return ArtLayer(self.app.item(index))

    def __iter__(self):
        for layer in self._layers:
            yield ArtLayer(layer)
