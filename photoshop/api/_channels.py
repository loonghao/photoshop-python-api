# Import local modules
from __future__ import annotations

from typing import Any

from photoshop.api._channel import Channel
from photoshop.api._collection_base import CollectionBase
from photoshop.api.errors import PhotoshopPythonAPIError


class Channels(CollectionBase[Channel]):
    """The collection of channel objects in the document.
    
    This class represents a collection of channels in a Photoshop document.
    It provides methods to:
    - Add new channels
    - Access channels by index or name
    - Remove channels
    - Iterate over channels
    """

    def add(self) -> Channel:
        """Add a new channel to the document.
        
        Returns:
            Channel: The newly created channel
        """
        return self._wrap_item(self.app.add())

    def removeAll(self) -> None:
        """Delete all channels in the collection."""
        self.app.removeAll()

    def getByName(self, name: str) -> Channel:
        """Get the first channel with the specified name.
        
        Args:
            name: The name of the channel to find
            
        Returns:
            Channel: The channel with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no channel with the specified name is found
        """
        for channel in self:
            if channel.name == name:
                return channel
        raise PhotoshopPythonAPIError(f'Could not find a channel named "{name}"')

    def _wrap_item(self, item: Any) -> Channel:
        """Wrap a COM channel object in a Channel instance.
        
        Args:
            item: The COM channel object to wrap
            
        Returns:
            Channel: The wrapped channel
        """
        return Channel(item)
