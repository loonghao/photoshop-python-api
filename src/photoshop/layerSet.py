from photoshop._core import Photoshop
from photoshop.layers import Layers
from photoshop.artlayers import ArtLayers


class LayerSet(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def name(self):
        return self.app.name

    @property
    def artLayers(self):
        return ArtLayers(self.app.artLayers)

    @property
    def enabledChannels(self):
        return self.app.enabledChannels

    @property
    def layerSets(self):
        return self.app.layerSets

    @property
    def layers(self):
        return Layers(self.app.layers)

    @property
    def parent(self):
        return self.app.parent

    def add(self):
        self.app.add()

    def merge(self):
        self.app.merge()

    def __iter__(self):
        for layer in self.app:
            yield layer

    @property
    def isBackgroundLayer(self):
        index = "app.activeDocument.layers.length-1"
        layers = "app.activeDocument.layers"
        layer = self.eval_javascript(f"{layers}({index}).name")
        return bool(layer == self.app.name)
