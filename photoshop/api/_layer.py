from typing import TYPE_CHECKING

from photoshop.api._core import Photoshop
from photoshop.api.enumerations import AnchorPosition, BlendMode, ElementPlacement
from photoshop.api.protocols import XMPMetadata

if TYPE_CHECKING:
    from photoshop.api._document import Document
    from photoshop.api._layerSet import LayerSet


class Layer(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "delete",
            "duplicate",
            "link",
            "move",
            "moveToEnd",
            "resize",
            "rotate",
            "translate",
            "unlink",
        )

    @property
    def allLocked(self) -> bool:
        return self.app.allLocked

    @allLocked.setter
    def allLocked(self, value: bool) -> None:
        self.app.allLocked = value

    @property
    def blendMode(self) -> BlendMode:
        return BlendMode(self.app.blendMode)

    @blendMode.setter
    def blendMode(self, mode: BlendMode) -> None:
        self.app.blendMode = mode

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        """The bounding rectangle of the layer."""
        return self.app.bounds

    @property
    def boundsNoEffects(self) -> tuple[float, float, float, float]:
        """Bounding rectangle of the Layer not including effects."""
        return self.app.boundsNoEffects

    @property
    def id(self) -> int:
        return self.app.id

    @property
    def itemIndex(self) -> int:
        return self.app.itemIndex

    @property
    def linkedLayers(self) -> list["Layer"]:
        """Get all layers linked to this layer.

        Returns:
            list: Layer objects"""
        return [Layer(layer) for layer in self.app.linkedLayers]

    @property
    def name(self) -> str:
        return self.app.name

    @name.setter
    def name(self, text: str) -> None:
        self.app.name = text

    @property
    def opacity(self) -> float:
        """The layer's master opacity (as a percentage). Range: 0.0 to 100.0."""
        return round(self.app.opacity)

    @opacity.setter
    def opacity(self, value: float) -> None:
        self.app.opacity = value

    @property
    def parent(self) -> "Document | LayerSet":
        """The layers's container."""
        parent = self.app.parent
        try:
            parent.resolution
            from photoshop.api._document import Document

            return Document(parent)
        except NameError:
            from photoshop.api._layerSet import LayerSet

            return LayerSet(parent)

    @property
    def visible(self) -> bool:
        return self.app.visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self.app.visible = value

    @property
    def xmpMetadata(self) -> XMPMetadata:
        return self.app.xmpMetadata

    def duplicate(
        self,
        relativeObject: "Layer | None" = None,
        insertionLocation: ElementPlacement | None = None,
    ) -> "Layer":
        """Duplicates the layer.

        Args:
            relativeObject: Layer or LayerSet.
            insertionLocation: The location to insert the layer.

        Returns:
            Layer: The duplicated layer.
        """
        return Layer(self.app.duplicate(relativeObject, insertionLocation))

    def link(self, with_layer: "Layer") -> None:
        self.app.link(with_layer)

    def move(
        self, relativeObject: "Layer | LayerSet", insertionLocation: ElementPlacement
    ) -> None:
        self.app.move(relativeObject, insertionLocation)

    def moveToEnd(self, layer_set: "LayerSet") -> None:
        self.app.moveToEnd(layer_set)

    def remove(self) -> None:
        """Removes this layer from the document."""
        self.app.delete()

    def resize(
        self, horizontal: float, vertical: float, anchor: AnchorPosition
    ) -> None:
        """Scales the object."""
        self.app.resize(horizontal, vertical, anchor)

    def rotate(self, angle: float, anchor: AnchorPosition) -> None:
        return self.app.rotate(angle, anchor)

    def translate(self, deltaX: float, deltaY: float) -> None:
        return self.app.translate(deltaX, deltaY)

    def unlink(self) -> None:
        """Unlink this layer from any linked layers."""
        self.app.unlink()
