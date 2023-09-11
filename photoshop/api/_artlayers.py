# Import third-party modules
from comtypes import ArgumentError

# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods
class ArtLayers(Photoshop):
    """The collection of art layer objects in the document."""

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
        )

    @property
    def _layers(self):
        return list(self.app)

    def __len__(self):
        return self.length

    def __iter__(self):
        for layer in self.app:
            yield layer

    def __getitem__(self, key: str):
        """Access a given ArtLayer using dictionary key lookup."""
        try:
            return ArtLayer(self.app[key])
        except ArgumentError:
            raise PhotoshopPythonAPIError(f'Could not find an artLayer named "{key}"')

    @property
    def length(self):
        return len(self._layers)

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(self):
        """Adds an element."""
        return ArtLayer(self.app.add())

    def getByIndex(self, index: int):
        """Access ArtLayer using list index lookup."""
        return ArtLayer(self._layers[index])

    def getByName(self, name: str) -> ArtLayer:
        """Get the first element in the collection with the provided name.

        Raises:
            PhotoshopPythonAPIError: Could not find a artLayer.
        """
        for layer in self.app:
            if layer.name == name:
                return ArtLayer(layer)
        raise PhotoshopPythonAPIError(f'Could not find an artLayer named "{name}"')

    def removeAll(self):
        """Deletes all elements."""
        for layer in self.app:
            ArtLayer(layer).remove()
