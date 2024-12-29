"""The collection of layer sets in the document."""

# Import third-party modules
from __future__ import annotations

from typing import Any, Union, overload

from comtypes import ArgumentError

# Import local modules
from photoshop.api._collection_base import CollectionBase
from photoshop.api._layerSet import LayerSet
from photoshop.api.errors import PhotoshopPythonAPIError


class LayerSets(CollectionBase[LayerSet]):
    """The collection of layer sets in the document.
    
    This class represents all the layer sets (layer groups) in a Photoshop document.
    It provides methods to:
    - Add new layer sets
    - Access layer sets by index or name
    - Remove layer sets
    - Iterate over layer sets
    """

    @overload
    def __getitem__(self, key: int) -> LayerSet:
        """Get layer set by index."""

    @overload
    def __getitem__(self, key: str) -> LayerSet:
        """Get layer set by name."""

    def __getitem__(self, key: Union[int, str]) -> LayerSet:
        """Access a given LayerSet using dictionary key lookup.
        
        Args:
            key: Either an integer index or a string name of the layer set
            
        Returns:
            LayerSet: The requested layer set
            
        Raises:
            PhotoshopPythonAPIError: If the layer set could not be found
            TypeError: If the key type is not int or str
        """
        try:
            if isinstance(key, str):
                # Use COM object's item method to get by name
                return self._wrap_item(self.app.item(key))
            if isinstance(key, int):
                return self._wrap_item(self.app[key])
            raise TypeError(f"Key must be int or str, not {type(key)}")
        except (ArgumentError, IndexError):
            name_str = f'named "{key}"' if isinstance(key, str) else f"at index {key}"
            raise PhotoshopPythonAPIError(f"Could not find a layer set {name_str}")

    def add(self) -> LayerSet:
        """Add a new layer set to the document.
        
        Returns:
            LayerSet: The newly created layer set
        """
        return self._wrap_item(self.app.add())

    def item(self, key: Union[int, str]) -> LayerSet:
        """Get a layer set by its index or name.
        
        Args:
            key: Either an integer index or a string name of the layer set
            
        Returns:
            LayerSet: The layer set at the specified index or with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If the layer set could not be found
        """
        try:
            return self._wrap_item(self.app.item(key))
        except ArgumentError:
            name_str = f'named "{key}"' if isinstance(key, str) else f"at index {key}"
            raise PhotoshopPythonAPIError(f"Could not find a layer set {name_str}")

    def removeAll(self) -> None:
        """Delete all layer sets in the collection."""
        self.app.removeAll()

    def getByName(self, name: str) -> LayerSet:
        """Get the first layer set with the specified name.
        
        Args:
            name: The name of the layer set to find
            
        Returns:
            LayerSet: The layer set with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no layer set with the specified name is found
        """
        try:
            return self._wrap_item(self.app.item(name))
        except ArgumentError:
            raise PhotoshopPythonAPIError(f'Could not find a layer set named "{name}"')

    def _wrap_item(self, item: Any) -> LayerSet:
        """Wrap a COM layer set object in a LayerSet instance.
        
        Args:
            item: The COM layer set object to wrap
            
        Returns:
            LayerSet: The wrapped layer set
        """
        return LayerSet(item)
