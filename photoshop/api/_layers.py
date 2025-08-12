# Import local modules
from typing import Any, Iterator

from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api._layer import Layer
from photoshop.api._layerSet import LayerSet


# pylint: disable=too-many-public-methods
class Layers(Photoshop):
    """The layers collection in the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method("add", "item", "removeAll")

    def _get_appropriate_layer(self, layer: Any) -> ArtLayer | LayerSet:
        try:
            layer.layers
            return LayerSet(layer)
        except NameError:
            return ArtLayer(layer)

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, key: int) -> ArtLayer | LayerSet:
        for idx, layer in enumerate(self.app):
            if idx == key:
                return self._get_appropriate_layer(layer)
        raise KeyError(f"Key '{key}' was not found in {type(self)}.")

    @property
    def length(self) -> int:
        return len(list(self.app))

    def removeAll(self) -> None:
        """Deletes all elements."""
        self.app.removeAll()

    def item(self, index: int) -> Layer:
        return self[index]

    def __iter__(self) -> Iterator[ArtLayer | LayerSet]:
        for layer in self.app:
            yield self._get_appropriate_layer(layer)

    def getByName(self, name: str) -> ArtLayer | LayerSet | None:
        """Get the first element in the collection with the provided name."""
        for layer in self.app:
            if layer.name == name:
                return self._get_appropriate_layer(layer)
        return None
