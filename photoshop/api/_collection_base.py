"""Base class for all collection-like objects in Photoshop API.

This module provides a base class that implements common collection functionality
for Photoshop objects, making them more Pythonic by supporting operations like
len(), iteration, and indexing.
"""

from __future__ import annotations
from typing import Any, Iterator, TypeVar, Generic

from photoshop.api._core import Photoshop

T = TypeVar("T")

class CollectionBase(Photoshop, Generic[T]):
    """Base class for all collection-like objects.
    
    This class provides common collection functionality and makes Photoshop
    collection objects more Pythonic by implementing:
    - len() support via __len__
    - iteration support via __iter__
    - indexing support via __getitem__
    
    Args:
        parent: The parent object that owns this collection
    """

    def __init__(self, parent: Any) -> None:
        """Initialize the collection base.
        
        Args:
            parent: The parent object that owns this collection
        """
        super().__init__(parent=parent)
        self._flag_as_method("add", "item")

    def __len__(self) -> int:
        """Get the number of items in the collection.
        
        Returns:
            int: The number of items in the collection
        """
        return self.app.count

    def __iter__(self) -> Iterator[T]:
        """Iterate over items in the collection.
        
        Yields:
            The next item in the collection
        """
        for item in self.app:
            yield self._wrap_item(item)

    def __getitem__(self, key: int) -> T:
        """Get an item by index.
        
        Args:
            key: The index of the item to get

        Returns:
            The item at the specified index
        
        Raises:
            IndexError: If the index is out of range
        """
        return self._wrap_item(self.app[key])

    def _wrap_item(self, item: Any) -> T:
        """Wrap a COM object in the appropriate Python class.
        
        This method should be overridden by subclasses to wrap COM objects
        in the appropriate Python class.
        
        Args:
            item: The COM object to wrap
            
        Returns:
            The wrapped item
        """
        raise NotImplementedError("Subclasses must implement _wrap_item")
