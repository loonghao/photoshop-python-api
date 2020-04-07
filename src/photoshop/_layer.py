from photoshop._core import Photoshop
from photoshop.enumerations import AnchorPosition
from photoshop.enumerations import LayerKind


class Layer(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def kind(self):
        return LayerKind(self.adobe.activeDocument.activeLayer.kind)

    @kind.setter
    def kind(self, value):
        self.adobe.activeDocument.activeLayer.kind = value
        # Convert current layer to ArtLayer.
        self.app = self.adobe.activeDocument.activeLayer

    @property
    def allLocked(self):
        return self.app.allLocked

    @property
    def blendMode(self):
        return self.app.blendMode

    @property
    def bounds(self):
        return self.app.bounds

    @property
    def boundsNoEffects(self):
        return self.app.boundsNoEffects

    @property
    def id(self):
        return self.app.id

    @property
    def itemIndex(self):
        return self.app.itemIndex

    @property
    def linkedLayers(self):
        return self.app.linkedLayers

    @property
    def name(self):
        return self.app.name

    @name.setter
    def name(self, text):
        self.app.name = text

    @property
    def opacity(self):
        return self.app.opacity

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.eval_javascript("app.activeDocument.activeLayer.typename")

    @property
    def visible(self):
        return self.app.visible

    @property
    def xmpMetadata(self):
        return self.app.xmpMetadata

    @property
    def isBackgroundLayer(self):
        return self.app.isBackgroundLayer

    def duplicate(self):
        self.app.duplicate()

    def link(self, layer):
        self.app.link(layer)

    def move(self):
        self.app.move()

    def moveToEnd(self, layerSet):
        self.app.moveToEnd(layerSet)

    def remove(self):
        """Deletes this object."""
        self.app.remove()

    def removeAll(self):
        """Deletes all elements."""
        self.app.removeAll()

    def resize(self, horizontal, vertical, anchor=AnchorPosition.MiddleCenter):
        """Scales the object.

        Args:
            horizontal (int): The amount to scale the object horizontally
                (as a percentage).
            vertical (int): The amount to scale the object vertically
                (as a percentage).
            anchor (): The point to resize about.

        """
        self.app.resize(horizontal, vertical, anchor)

    def rotate(self, angle):
        self.app.rotate(angle)

    def translate(self, x, y):
        self.app.translate(x, y)

    def unlink(self):
        self.app.unlink()
