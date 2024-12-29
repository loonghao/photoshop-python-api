# Import local modules
from __future__ import annotations

from photoshop.api._artlayer import ArtLayer
from photoshop.api._collection_base import CollectionBase
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods
class Layers(CollectionBase[ArtLayer]):
    """The layers collection in the document."""

    def removeAll(self) -> None:
        """Deletes all elements."""
        for layer in self:
            layer.remove()

    def item(self, index: int) -> ArtLayer:
        """Get layer by index.
        
        Args:
            index: The index of the layer to get
            
        Returns:
            ArtLayer: The layer at the specified index
        """
        return self._wrap_item(self.app.item(index))

    def getByName(self, name: str) -> ArtLayer:
        """Get the first element in the collection with the provided name.
        
        Args:
            name: The name of the layer to find
            
        Returns:
            ArtLayer: The first layer with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no layer with the specified name is found
        """
        for layer in self:
            if layer.name == name:
                return layer
        raise PhotoshopPythonAPIError(f'Could not find a layer named "{name}"')

    def _wrap_item(self, item: Any) -> ArtLayer:
        """Wrap a COM layer object in an ArtLayer instance.
        
        Args:
            item: The COM layer object to wrap
            
        Returns:
            ArtLayer: The wrapped layer
        """
        return ArtLayer(item)
