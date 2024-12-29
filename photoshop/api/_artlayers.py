# Import third-party modules
from __future__ import annotations

from typing import Any, Union, overload

from comtypes import ArgumentError

# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._collection_base import CollectionBase
from photoshop.api.errors import PhotoshopPythonAPIError


class ArtLayers(CollectionBase[ArtLayer]):
    """The collection of art layer objects in the document.
    
    This class represents a collection of art layers in a Photoshop document.
    It provides methods to:
    - Add new layers
    - Access layers by index or name
    - Remove layers
    - Iterate over layers
    """
    
    @overload
    def __getitem__(self, key: int) -> ArtLayer:
        """Get layer by index."""
    
    @overload
    def __getitem__(self, key: str) -> ArtLayer:
        """Get layer by name."""
    
    def __getitem__(self, key: Union[int, str]) -> ArtLayer:
        """Access a given ArtLayer using dictionary key lookup.
        
        Args:
            key: Either an integer index or a string name of the layer
            
        Returns:
            ArtLayer: The requested art layer
            
        Raises:
            PhotoshopPythonAPIError: If the layer could not be found
            TypeError: If the key type is not int or str
        """
        try:
            if isinstance(key, str):
                return self.getByName(key)
            if isinstance(key, int):
                return self._wrap_item(self.app[key])
            raise TypeError(f"Key must be int or str, not {type(key)}")
        except (ArgumentError, IndexError):
            name_str = f'named "{key}"' if isinstance(key, str) else f"at index {key}"
            raise PhotoshopPythonAPIError(f"Could not find an artLayer {name_str}")

    def add(self) -> ArtLayer:
        """Add a new art layer to the document.
        
        Returns:
            ArtLayer: The newly created art layer
        """
        return self._wrap_item(self.app.add())

    def getByName(self, name: str) -> ArtLayer:
        """Get the first art layer with the specified name.
        
        Args:
            name: The name of the layer to find
            
        Returns:
            ArtLayer: The art layer with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no layer with the specified name is found
        """
        for layer in self:
            if layer.name == name:
                return layer
        raise PhotoshopPythonAPIError(f'Could not find an artLayer named "{name}"')

    def removeAll(self) -> None:
        """Delete all art layers in the collection."""
        for layer in self:
            layer.remove()

    def _wrap_item(self, item: Any) -> ArtLayer:
        """Wrap a COM art layer object in an ArtLayer instance.
        
        Args:
            item: The COM art layer object to wrap
            
        Returns:
            ArtLayer: The wrapped art layer
        """
        return ArtLayer(item)
