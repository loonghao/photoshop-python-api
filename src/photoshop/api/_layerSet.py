from ._artlayers import ArtLayers
from ._core import Photoshop
from ._layers import Layers
from ._artlayer import ArtLayer
from .enumerations import AnchorPosition


class LayerSet(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def allLocked(self):
        return self.app.allLocked

    @allLocked.setter
    def allLocked(self, value):
        self.app.allLocked = value

    @property
    def artLayers(self):
        return ArtLayers(self.app.artLayers)

    @property
    def blendMode(self):
        return self.app.blendMode

    @property
    def bounds(self):
        """ The bounding rectangle of the layer set."""
        return self.app.bounds

    @property
    def enabledChannels(self):
        return self.app.enabledChannels

    @property
    def layers(self):
        return Layers(self.app.layers)

    @property
    def layerSets(self):
        # pylint: disable=import-outside-toplevel
        from ._layerSets import LayerSets
        return LayerSets(self.app.layerSets)

    @property
    def linkedLayers(self):
        """The layers linked to this layerSet object."""
        return self.app.linkedLayers or []

    @property
    def name(self):
        return self.app.name

    @name.setter
    def name(self, value):
        self.app.name = value

    @property
    def opacity(self):
        return round(self.app.opacity)

    @opacity.setter
    def opacity(self, value):
        self.app.opacity = value

    @property
    def parent(self):
        return self.app.parent

    @property
    def visible(self):
        return self.app.visible

    @visible.setter
    def visible(self, value):
        self.app.visible = value

    def duplicate(self, relativeObject=None, insertionLocation=None):
        return LayerSet(self.app.duplicate(relativeObject, insertionLocation))

    def link(self, with_layer):
        self.app.link(with_layer)

    def add(self):
        self.app.add()

    def merge(self):
        return ArtLayer(self.app.merge())

    def move(self, relativeObject, insertionLocation):
        self.app.move(relativeObject, insertionLocation)

    def remove(self):
        layer = f'app.activeDocument.layerSets.getByName("{self.app.name}")'
        self.eval_javascript(f'{layer}.remove()')

    def resize(self, horizontal=None, vertical=None,
               anchor: AnchorPosition = None):
        self.app.resize(horizontal, vertical, anchor)

    def __iter__(self):
        for layer in self.app:
            yield layer
