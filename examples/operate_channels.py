"""Channel management in Photoshop.

This script demonstrates how to:
1. Create and remove channels
2. Select and modify channels
3. Blend channels
4. Work with alpha channels
5. Handle channel operations
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

import photoshop.api as ps
from photoshop import Session

class ChannelType(Enum):
    """Channel types."""
    RGB = auto()  # RGB channels
    ALPHA = auto()  # Alpha channels
    SPOT = auto()  # Spot color channels
    MASK = auto()  # Layer mask channels

@dataclass
class ChannelInfo:
    """Channel information."""
    name: str  # Channel name
    type: ChannelType  # Channel type
    visible: bool = True  # Channel visibility
    color: Optional[tuple[int, int, int]] = None  # Channel color (RGB)
    opacity: float = 100.0  # Channel opacity (0-100)

class ChannelManager:
    """Class for managing Photoshop channels."""
    
    def __init__(self, doc: ps.Document) -> None:
        """Initialize channel manager.
        
        Args:
            doc: Photoshop document
        """
        self.doc = doc
    
    def list_channels(self) -> List[str]:
        """List all channels.
        
        Returns:
            List of channel names
        """
        try:
            return [str(channel.name) for channel in self.doc.channels]
            
        except Exception as e:
            print(f"Error listing channels: {e}")
            return []
    
    def get_channel(self, name: str) -> Optional[ps.Channel]:
        """Get channel by name.
        
        Args:
            name: Channel name
            
        Returns:
            Channel if found, None otherwise
        """
        try:
            for channel in self.doc.channels:
                if str(channel.name) == name:
                    return channel
            return None
            
        except Exception as e:
            print(f"Error getting channel '{name}': {e}")
            return None
    
    def create_alpha_channel(self, info: ChannelInfo) -> Optional[ps.Channel]:
        """Create new alpha channel.
        
        Args:
            info: Channel information
            
        Returns:
            Created channel if successful, None otherwise
        """
        try:
            # Create channel
            channel = self.doc.channels.add()
            
            # Set properties (some properties may not be settable)
            try:
                if hasattr(channel, "kind"):
                    channel.kind = "alpha"  # Set as alpha channel
            except Exception:
                pass
            
            try:
                if hasattr(channel, "visible"):
                    channel.visible = info.visible
            except Exception:
                pass
            
            try:
                if hasattr(channel, "opacity"):
                    channel.opacity = info.opacity
            except Exception:
                pass
            
            return channel
            
        except Exception as e:
            print(f"Error creating channel: {e}")
            return None
    
    def duplicate_channel(self, 
                         source_name: str,
                         target_name: str) -> Optional[ps.Channel]:
        """Duplicate channel.
        
        Args:
            source_name: Source channel name
            target_name: Target channel name
            
        Returns:
            Duplicated channel if successful, None otherwise
        """
        try:
            # Get source channel
            source = self.get_channel(source_name)
            if not source:
                print(f"Source channel '{source_name}' not found")
                return None
            
            # Create new channel
            target = self.create_alpha_channel(ChannelInfo(
                name=target_name,
                type=ChannelType.ALPHA,
            ))
            
            if not target:
                return None
            
            # Copy channel data (this may require JavaScript)
            # TODO: Implement channel data copying
            
            return target
            
        except Exception as e:
            print(f"Error duplicating channel: {e}")
            return None
    
    def remove_channel(self, name: str) -> bool:
        """Remove channel.
        
        Args:
            name: Channel name
            
        Returns:
            True if successful
        """
        try:
            channel = self.get_channel(name)
            if channel:
                channel.remove()
                return True
            return False
            
        except Exception as e:
            print(f"Error removing channel: {e}")
            return False
    
    def remove_all_channels(self) -> bool:
        """Remove all channels.
        
        Returns:
            True if successful
        """
        try:
            self.doc.channels.removeAll()
            return True
            
        except Exception as e:
            print(f"Error removing all channels: {e}")
            return False
    
    def select_channel(self, name: str) -> bool:
        """Select channel.
        
        Args:
            name: Channel name
            
        Returns:
            True if successful
        """
        try:
            channel = self.get_channel(name)
            if channel:
                self.doc.activeChannels = [channel]
                return True
            return False
            
        except Exception as e:
            print(f"Error selecting channel: {e}")
            return False

def main() -> None:
    """Channel management example."""
    try:
        # Initialize Photoshop
        with Session() as pss:
            doc = pss.active_document
            manager = ChannelManager(doc)
            
            print("\n=== Channel Operations ===")
            
            # List channels
            print("\nExisting channels:")
            channels = manager.list_channels()
            for channel in channels:
                print(f"- {channel}")
            
            # Create new channel
            print("\nCreating new alpha channel:")
            new_channel = manager.create_alpha_channel(ChannelInfo(
                name="Alpha 1",
                type=ChannelType.ALPHA,
            ))
            if new_channel:
                print("Created new alpha channel")
            
            # List updated channels
            print("\nUpdated channels:")
            channels = manager.list_channels()
            for channel in channels:
                print(f"- {channel}")
            
            # Select a channel
            if channels:
                print(f"\nSelecting channel '{channels[0]}':")
                if manager.select_channel(channels[0]):
                    print(f"Selected channel: {channels[0]}")
            
            # Remove channel
            print("\nRemoving alpha channel:")
            if manager.remove_channel("Alpha 1"):
                print("Removed alpha channel")
            
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
