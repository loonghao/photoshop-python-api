from photoshop._core import Photoshop
from photoshop.artlayer import ArtLayer
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
        return self.app.layers

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(self):
        self.app.add()

    def merge(self):
        self.app.merge()
