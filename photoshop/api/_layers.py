# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods
class Layers(Photoshop):
    """The layers collection in the document."""

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
            "item",
        )

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
        """Deletes all elements."""
        for layer in self.app:
            ArtLayer(layer).remove()

    def item(self, index):
        return ArtLayer(self.app.item(index))

    def __iter__(self):
        for layer in self._layers:
            yield ArtLayer(layer)

    def getByName(self, name: str) -> ArtLayer:
        """Get the first element in the collection with the provided name."""
        for layer in self.app:
            if layer.name == name:
                return ArtLayer(layer)
        raise PhotoshopPythonAPIError("X")
