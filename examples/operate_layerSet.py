"""Layer set (group) management in Photoshop.

This script demonstrates how to:
1. Create and remove layer sets
2. Manage layer set properties
3. Handle layer set hierarchy
4. Move layers between sets
5. Merge layer sets
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Union

import photoshop.api as ps
from photoshop import Session

class LayerSetBlendMode(Enum):
    """Layer set blend modes."""
    NORMAL = 2  # Normal
    MULTIPLY = 4  # Multiply
    SCREEN = 9  # Screen
    OVERLAY = 10  # Overlay
    SOFT_LIGHT = 11  # Soft Light
    HARD_LIGHT = 12  # Hard Light
    COLOR_DODGE = 13  # Color Dodge
    COLOR_BURN = 14  # Color Burn

@dataclass
class LayerSetInfo:
    """Layer set information."""
    name: str  # Layer set name
    opacity: float = 100.0  # Opacity (0-100)
    visible: bool = True  # Visibility
    blend_mode: LayerSetBlendMode = LayerSetBlendMode.NORMAL  # Blend mode
    color: Optional[tuple[int, int, int]] = None  # Color label (RGB)

class LayerSetManager:
    """Class for managing Photoshop layer sets."""
    
    def __init__(self, doc: ps.Document) -> None:
        """Initialize layer set manager.
        
        Args:
            doc: Photoshop document
        """
        self.doc = doc
    
    def list_layer_sets(self, parent: Optional[ps.LayerSet] = None) -> List[str]:
        """List layer sets.
        
        Args:
            parent: Parent layer set, None for root level
            
        Returns:
            List of layer set names
        """
        try:
            sets = parent.layerSets if parent else self.doc.layerSets
            return [str(layer_set.name) for layer_set in sets]
            
        except Exception as e:
            print(f"Error listing layer sets: {e}")
            return []
    
    def get_layer_set(self, 
                     name: str,
                     parent: Optional[ps.LayerSet] = None) -> Optional[ps.LayerSet]:
        """Get layer set by name.
        
        Args:
            name: Layer set name
            parent: Parent layer set, None for root level
            
        Returns:
            Layer set if found, None otherwise
        """
        try:
            sets = parent.layerSets if parent else self.doc.layerSets
            for layer_set in sets:
                if str(layer_set.name) == name:
                    return layer_set
            return None
            
        except Exception as e:
            print(f"Error getting layer set '{name}': {e}")
            return None
    
    def create_layer_set(self, 
                        info: LayerSetInfo,
                        parent: Optional[ps.LayerSet] = None) -> Optional[ps.LayerSet]:
        """Create new layer set.
        
        Args:
            info: Layer set information
            parent: Parent layer set, None for root level
            
        Returns:
            Created layer set if successful, None otherwise
        """
        try:
            # Create layer set
            sets = parent.layerSets if parent else self.doc.layerSets
            layer_set = sets.add()
            
            # Set properties
            try:
                layer_set.name = info.name
            except Exception:
                pass
            
            try:
                layer_set.opacity = info.opacity
            except Exception:
                pass
            
            try:
                layer_set.visible = info.visible
            except Exception:
                pass
            
            try:
                layer_set.blendMode = info.blend_mode.value
            except Exception:
                pass
            
            return layer_set
            
        except Exception as e:
            print(f"Error creating layer set: {e}")
            return None
    
    def duplicate_layer_set(self,
                          source: Union[str, ps.LayerSet],
                          new_name: str) -> Optional[ps.LayerSet]:
        """Duplicate layer set.
        
        Args:
            source: Source layer set or name
            new_name: New layer set name
            
        Returns:
            Duplicated layer set if successful, None otherwise
        """
        try:
            # Get source layer set
            if isinstance(source, str):
                source = self.get_layer_set(source)
            
            if not source:
                return None
            
            # Duplicate layer set
            duplicate = source.duplicate()
            
            # Set name
            try:
                duplicate.name = new_name
            except Exception:
                pass
            
            return duplicate
            
        except Exception as e:
            print(f"Error duplicating layer set: {e}")
            return None
    
    def merge_layer_set(self, 
                       target: Union[str, ps.LayerSet]) -> Optional[ps.ArtLayer]:
        """Merge layer set.
        
        Args:
            target: Target layer set or name
            
        Returns:
            Merged layer if successful, None otherwise
        """
        try:
            # Get target layer set
            if isinstance(target, str):
                target = self.get_layer_set(target)
            
            if not target:
                return None
            
            # Merge layer set
            return target.merge()
            
        except Exception as e:
            print(f"Error merging layer set: {e}")
            return None
    
    def move_to_layer_set(self,
                         layer: Union[ps.ArtLayer, ps.LayerSet],
                         target: Union[str, ps.LayerSet]) -> bool:
        """Move layer to layer set.
        
        Args:
            layer: Layer to move
            target: Target layer set or name
            
        Returns:
            True if successful
        """
        try:
            # Get target layer set
            if isinstance(target, str):
                target = self.get_layer_set(target)
            
            if not target:
                return False
            
            # Move layer
            layer.move(target, ps.ElementPlacement.PlaceInside)
            return True
            
        except Exception as e:
            print(f"Error moving layer: {e}")
            return False

def main() -> None:
    """Layer set management example."""
    try:
        # Initialize Photoshop
        with Session(action="new_document") as pss:
            doc = pss.active_document
            manager = LayerSetManager(doc)
            
            print("\n=== Layer Set Operations ===")
            
            # Create layer set
            print("\nCreating layer set:")
            layer_set1 = manager.create_layer_set(LayerSetInfo(
                name="Group 1",
                opacity=80,
                blend_mode=LayerSetBlendMode.OVERLAY,
            ))
            if layer_set1:
                print(f"Created layer set: {layer_set1.name}")
            
            # Create nested layer set
            print("\nCreating nested layer set:")
            layer_set2 = manager.create_layer_set(
                LayerSetInfo(name="Nested Group"),
                parent=layer_set1,
            )
            if layer_set2:
                print(f"Created nested layer set: {layer_set2.name}")
            
            # List layer sets
            print("\nLayer sets at root level:")
            sets = manager.list_layer_sets()
            for set_name in sets:
                print(f"- {set_name}")
            
            # Create art layer
            print("\nCreating and moving art layer:")
            layer = doc.artLayers.add()
            if manager.move_to_layer_set(layer, layer_set2):
                print("Moved layer to nested group")
            
            # Duplicate layer set
            print("\nDuplicating layer set:")
            dup_set = manager.duplicate_layer_set(layer_set1, "Group 1 Copy")
            if dup_set:
                print(f"Duplicated layer set: {dup_set.name}")
            
            # Merge layer set
            print("\nMerging layer set:")
            merged = manager.merge_layer_set(dup_set)
            if merged:
                print(f"Merged layer set into: {merged.name}")
            
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
