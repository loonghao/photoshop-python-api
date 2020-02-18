from photoshop._core import Photoshop
from photoshop.art_layer import ArtLayer
from photoshop.layers import Layers


class LayerSets(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return ArtLayer(self._layerSets[key])

    @property
    def _layerSets(self):
        return [layerset for layerset in self.app]

    @property
    def length(self):
        return len(self._layerSets)

    def add(self):
        self.app.add()

    def getByName(self, name):
        for layer in self._layerSets:
            if name == layer.name:
                return Layers(layer.layers)
