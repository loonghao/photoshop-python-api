# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._artlayers import ArtLayers
from photoshop.api._core import Photoshop
from photoshop.api._layers import Layers
from photoshop.api.enumerations import AnchorPosition
from photoshop.api.enumerations import BlendMode


class LayerSet(Photoshop):
    """A group of layer objects, which can include art layer objects and other (nested) layer set objects.

    A single command or set of commands manipulates all layers in a layer set object.

    """

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "merge",
            "duplicate",
            "add",
            "delete",
            "link",
            "move",
            "resize",
            "rotate",
            "translate",
            "unlink",
        )

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
        return BlendMode(self.app.blendMode)

    @property
    def bounds(self):
        """The bounding rectangle of the layer set."""
        return self.app.bounds

    @property
    def enabledChannels(self):
        return self.app.enabledChannels

    @enabledChannels.setter
    def enabledChannels(self, value):
        self.app.enabledChannels = value

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
    def name(self) -> str:
        return self.app.name

    @name.setter
    def name(self, value):
        """The name of this layer set."""
        self.app.name = value

    @property
    def opacity(self):
        """The master opacity of the set."""
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
        """Adds an element."""
        self.app.add()

    def merge(self) -> ArtLayer:
        """Merges the layer set."""
        return ArtLayer(self.app.merge())

    def move(self, relativeObject, insertionLocation):
        self.app.move(relativeObject, insertionLocation)

    def remove(self):
        """Remove this layer set from the document."""
        self.app.delete()

    def resize(self, horizontal=None, vertical=None, anchor: AnchorPosition = None):
        self.app.resize(horizontal, vertical, anchor)

    def rotate(self, angle, anchor=None):
        self.app.rotate(angle, anchor)

    def translate(self, delta_x, delta_y):
        """Moves the position relative to its current position."""
        self.app.translate(delta_x, delta_y)

    def unlink(self):
        """Unlinks the layer set."""
        self.app.unlink()

    def __iter__(self):
        for layer in self.app:
            yield layer
