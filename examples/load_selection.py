"""Selection management in Photoshop.

This script demonstrates how to:
1. Create and manage selections
2. Save selections to alpha channels
3. Load selections from alpha channels
4. Combine selections using different modes
5. Get selection information and bounds
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple, Union

from photoshop import Session
from photoshop.api import SelectionType

class SelectionMode(Enum):
    """Selection combination modes."""
    NEW = SelectionType.ReplaceSelection
    ADD = SelectionType.ExtendSelection
    SUBTRACT = SelectionType.DiminishSelection
    INTERSECT = SelectionType.IntersectSelection

@dataclass
class SelectionInfo:
    """Selection information."""
    bounds: Tuple[float, float, float, float]  # left, top, right, bottom
    solid: bool  # True if selection is solid
    feather_radius: float  # Feather radius in pixels
    
    @property
    def width(self) -> float:
        """Get selection width."""
        return self.bounds[2] - self.bounds[0]
    
    @property
    def height(self) -> float:
        """Get selection height."""
        return self.bounds[3] - self.bounds[1]
    
    @property
    def area(self) -> float:
        """Get selection area."""
        return self.width * self.height
    
    def __str__(self) -> str:
        """Get string representation."""
        info = [
            f"Bounds: ({self.bounds[0]:.1f}, {self.bounds[1]:.1f}, {self.bounds[2]:.1f}, {self.bounds[3]:.1f})",
            f"Width: {self.width:.1f} pixels",
            f"Height: {self.height:.1f} pixels",
            f"Area: {self.area:.1f} square pixels",
            f"Solid: {'Yes' if self.solid else 'No'}",
            f"Feather Radius: {self.feather_radius:.1f} pixels",
        ]
        return "\n".join(info)

class SelectionManager:
    """Class for managing Photoshop selections."""
    
    def __init__(self, session: Session) -> None:
        """Initialize selection manager.
        
        Args:
            session: Photoshop session
        """
        self.session = session
        self.doc = None
        self._ensure_pixels_units()
    
    def _ensure_pixels_units(self) -> None:
        """Ensure ruler units are set to pixels."""
        if self.session.app.preferences.rulerUnits is not self.session.Units.Pixels:
            self.session.app.preferences.rulerUnits = self.session.Units.Pixels
    
    def _ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists
        """
        try:
            if len(self.session.app.documents) < 1:
                print("Error: No document is open")
                return False
            self.doc = self.session.app.activeDocument
            return True
        except Exception as e:
            print(f"Error checking document: {e}")
            return False
    
    def _get_safe_property(self, obj: any, prop: str, default: any = None) -> any:
        """Safely get object property.
        
        Args:
            obj: Object to get property from
            prop: Property name
            default: Default value if property not found
            
        Returns:
            Property value or default
        """
        try:
            value = getattr(obj, prop)
            # Handle callable properties
            if callable(value):
                try:
                    value = value()
                except:
                    value = default
            return value
        except Exception:
            return default
    
    def create_selection(self, 
                        bounds: Union[List[Tuple[float, float]], Tuple[float, float, float, float]],
                        mode: SelectionMode = SelectionMode.NEW,
                        feather: float = 0,
                        anti_alias: bool = True) -> bool:
        """Create a selection.
        
        Args:
            bounds: Selection bounds. Can be list of points or (left, top, right, bottom)
            mode: Selection mode
            feather: Feather radius in pixels
            anti_alias: Use anti-aliasing
            
        Returns:
            bool: True if successful
        """
        try:
            if not self._ensure_document_exists():
                return False
            
            # Convert bounds if needed
            if isinstance(bounds, tuple) and len(bounds) == 4:
                left, top, right, bottom = bounds
                bounds = [
                    (left, top),
                    (right, top),
                    (right, bottom),
                    (left, bottom),
                ]
            
            # Create selection
            self.doc.selection.select(bounds, mode.value, feather, anti_alias)
            return True
            
        except Exception as e:
            print(f"Error creating selection: {e}")
            return False
    
    def save_to_channel(self, name: str = None) -> Optional[str]:
        """Save current selection to alpha channel.
        
        Args:
            name: Channel name (optional)
            
        Returns:
            str: Channel name if successful, None otherwise
        """
        try:
            if not self._ensure_document_exists():
                return None
            
            # Create new channel
            channel = self.doc.channels.add()
            
            # Store selection
            self.doc.selection.store(channel)
            
            # Try to set name if provided
            try:
                if name:
                    channel.name = name
            except:
                pass  # Ignore name setting errors
            
            return channel.name
            
        except Exception as e:
            print(f"Error saving selection to channel: {e}")
            return None
    
    def load_from_channel(self, 
                         channel_name: str,
                         mode: SelectionMode = SelectionMode.NEW,
                         invert: bool = False) -> bool:
        """Load selection from alpha channel.
        
        Args:
            channel_name: Channel name
            mode: Selection mode
            invert: Invert selection
            
        Returns:
            bool: True if successful
        """
        try:
            if not self._ensure_document_exists():
                return False
            
            # Find channel
            channel = None
            for ch in self.doc.channels:
                if ch.name == channel_name:
                    channel = ch
                    break
            
            if not channel:
                print(f"Error: Channel '{channel_name}' not found")
                return False
            
            # Load selection
            self.doc.selection.load(channel, mode.value, invert)
            return True
            
        except Exception as e:
            print(f"Error loading selection from channel: {e}")
            return False
    
    def get_info(self) -> Optional[SelectionInfo]:
        """Get selection information.
        
        Returns:
            SelectionInfo if selection exists, None otherwise
        """
        try:
            if not self._ensure_document_exists():
                return None
            
            # Check if selection exists and get bounds
            bounds = self._get_safe_property(self.doc.selection, "bounds")
            if not bounds:
                return None
            
            # Get other properties safely
            solid = bool(self._get_safe_property(self.doc.selection, "solid", False))
            feather = float(self._get_safe_property(self.doc.selection, "feather", 0))
            
            # Create info object
            return SelectionInfo(
                bounds=bounds,
                solid=solid,
                feather_radius=feather,
            )
            
        except Exception as e:
            print(f"Error getting selection info: {e}")
            return None
    
    def deselect(self) -> bool:
        """Deselect current selection.
        
        Returns:
            bool: True if successful
        """
        try:
            if not self._ensure_document_exists():
                return False
            
            self.doc.selection.deselect()
            return True
            
        except Exception as e:
            print(f"Error deselecting: {e}")
            return False

def main() -> None:
    """Selection management example."""
    try:
        with Session() as ps:
            # Create document
            doc = ps.app.documents.add(320, 240)
            manager = SelectionManager(ps)
            
            # Create first selection
            print("\n=== Creating First Selection ===")
            offset = 50
            bounds1 = (
                offset, offset,
                doc.width - offset, doc.height - offset,
            )
            manager.create_selection(bounds1, feather=2)
            
            # Save to channel
            channel_name = manager.save_to_channel("Selection 1")
            print(f"Saved to channel: {channel_name}")
            
            # Get selection info
            info = manager.get_info()
            if info:
                print("\nSelection Info:")
                print(info)
            
            # Create second selection
            print("\n=== Creating Second Selection ===")
            bounds2 = (0, 75, doc.width, 150)
            manager.create_selection(bounds2)
            
            # Combine with first selection
            print("\n=== Combining Selections ===")
            manager.load_from_channel(channel_name, mode=SelectionMode.ADD)
            
            # Get final selection info
            info = manager.get_info()
            if info:
                print("\nFinal Selection Info:")
                print(info)
            
    except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
