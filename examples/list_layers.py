from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

import photoshop.api as ps
from photoshop.api._artlayer import ArtLayer
from photoshop.api._layerSet import LayerSet

class LayerType(Enum):
    """Layer types."""
    NORMAL = "ArtLayer"
    GROUP = "LayerSet"
    TEXT = "TextLayer"
    ADJUSTMENT = "AdjustmentLayer"
    SMART_OBJECT = "SmartObject"

class LayerSortBy(Enum):
    """Layer sorting options."""
    NAME = "name"
    TYPE = "type"
    VISIBLE = "visible"
    OPACITY = "opacity"
    POSITION = "position"

@dataclass
class LayerInfo:
    """Layer information."""
    name: str
    type: LayerType
    visible: bool
    opacity: float
    blend_mode: str
    locked: bool
    linked: bool
    parent: Optional[str] = None  # Parent group name
    bounds: Optional[tuple] = None  # Layer bounds (left, top, right, bottom)
    
    def __str__(self) -> str:
        """Get string representation."""
        info = [
            f"Name: {self.name}",
            f"Type: {self.type.name}",
            f"Visible: {'Yes' if self.visible else 'No'}",
            f"Opacity: {self.opacity}%",
            f"Blend Mode: {self.blend_mode}",
            f"Locked: {'Yes' if self.locked else 'No'}",
            f"Linked: {'Yes' if self.linked else 'No'}",
        ]
        if self.parent:
            info.append(f"Parent Group: {self.parent}")
        if self.bounds:
            info.append(f"Bounds: {self.bounds}")
        return "\n".join(info)

class LayerManager:
    """Class for managing Photoshop layers."""
    
    def __init__(self, app: ps.Application) -> None:
        """Initialize layer manager.
        
        Args:
            app: Photoshop application instance
        """
        self.app = app
        self.doc = None
        self.cache: Dict[str, LayerInfo] = {}  # Cache layer info
    
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
            return getattr(obj, prop)
        except Exception:
            return default
    
    def ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists
        """
        try:
            if len(self.app.documents) < 1:
                print("Error: No document is open")
                return False
            self.doc = self.app.activeDocument
            return True
        except Exception as e:
            print(f"Error checking document: {e}")
            return False
    
    def get_layer_type(self, layer: Union[ArtLayer, LayerSet]) -> LayerType:
        """Get layer type.
        
        Args:
            layer: Layer object
            
        Returns:
            Layer type
        """
        try:
            typename = self._get_safe_property(layer, "typename", "Unknown")
            if typename == "ArtLayer":
                # Check for specific art layer types
                kind = self._get_safe_property(layer, "kind", None)
                if kind == ps.LayerKind.TextLayer:
                    return LayerType.TEXT
                if kind in [ps.LayerKind.HueSaturation, ps.LayerKind.Levels]:
                    return LayerType.ADJUSTMENT
                if kind == ps.LayerKind.SmartObject:
                    return LayerType.SMART_OBJECT
                return LayerType.NORMAL
            if typename == "LayerSet":
                return LayerType.GROUP
            return LayerType.NORMAL
        except Exception:
            return LayerType.NORMAL
    
    def get_layer_info(self, layer: Union[ArtLayer, LayerSet], 
                      parent: str = None) -> LayerInfo:
        """Get layer information.
        
        Args:
            layer: Layer object
            parent: Parent group name
            
        Returns:
            Layer information
        """
        try:
            # Get layer properties safely
            info = LayerInfo(
                name=self._get_safe_property(layer, "name", "Untitled"),
                type=self.get_layer_type(layer),
                visible=self._get_safe_property(layer, "visible", True),
                opacity=self._get_safe_property(layer, "opacity", 100),
                blend_mode=self._get_safe_property(layer, "blendMode", "normal"),
                locked=self._get_safe_property(layer, "allLocked", False),
                linked=self._get_safe_property(layer, "linked", False),
                parent=parent,
                bounds=self._get_safe_property(layer, "bounds", None),
            )
            
            # Cache info
            self.cache[info.name] = info
            return info
            
        except Exception as e:
            print(f"Error getting layer info for {layer.name}: {e}")
            return LayerInfo(
                name=self._get_safe_property(layer, "name", "Unknown"),
                type=LayerType.NORMAL,
                visible=True,
                opacity=100,
                blend_mode="normal",
                locked=False,
                linked=False,
            )
    
    def list_layers(self, include_hidden: bool = True,
                   sort_by: LayerSortBy = None,
                   reverse: bool = False) -> List[LayerInfo]:
        """List all layers in document.
        
        Args:
            include_hidden: Include hidden layers
            sort_by: Sort criteria
            reverse: Reverse sort order
            
        Returns:
            List of layer information
        """
        try:
            if not self.ensure_document_exists():
                return []
            
            layers = []
            
            def process_layer_set(layer_set: LayerSet, parent: str = None):
                """Process layer set and its children."""
                # Process art layers in set
                for layer in layer_set.artLayers:
                    if include_hidden or layer.visible:
                        info = self.get_layer_info(layer, parent)
                        layers.append(info)
                
                # Process nested layer sets
                for nested_set in layer_set.layerSets:
                    if include_hidden or nested_set.visible:
                        info = self.get_layer_info(nested_set, parent)
                        layers.append(info)
                        process_layer_set(nested_set, info.name)
            
            # Process root level layers
            for layer in self.doc.artLayers:
                if include_hidden or layer.visible:
                    info = self.get_layer_info(layer)
                    layers.append(info)
            
            # Process root level layer sets
            for layer_set in self.doc.layerSets:
                if include_hidden or layer_set.visible:
                    info = self.get_layer_info(layer_set)
                    layers.append(info)
                    process_layer_set(layer_set, info.name)
            
            # Sort layers
            if sort_by:
                if sort_by == LayerSortBy.NAME:
                    layers.sort(key=lambda x: x.name, reverse=reverse)
                elif sort_by == LayerSortBy.TYPE:
                    layers.sort(key=lambda x: x.type.name, reverse=reverse)
                elif sort_by == LayerSortBy.VISIBLE:
                    layers.sort(key=lambda x: x.visible, reverse=reverse)
                elif sort_by == LayerSortBy.OPACITY:
                    layers.sort(key=lambda x: x.opacity, reverse=reverse)
            
            return layers
            
        except Exception as e:
            print(f"Error listing layers: {e}")
            return []
    
    def find_layers(self, 
                   name_pattern: str = None,
                   layer_type: LayerType = None,
                   visible_only: bool = False,
                   parent_group: str = None) -> List[LayerInfo]:
        """Find layers matching criteria.
        
        Args:
            name_pattern: Layer name pattern
            layer_type: Layer type
            visible_only: Only visible layers
            parent_group: Parent group name
            
        Returns:
            List of matching layers
        """
        try:
            layers = self.list_layers(include_hidden=not visible_only)
            filtered = []
            
            for layer in layers:
                # Apply filters
                if name_pattern and name_pattern.lower() not in layer.name.lower():
                    continue
                    
                if layer_type and layer.type != layer_type:
                    continue
                    
                if visible_only and not layer.visible:
                    continue
                    
                if parent_group and layer.parent != parent_group:
                    continue
                
                filtered.append(layer)
            
            return filtered
            
        except Exception as e:
            print(f"Error finding layers: {e}")
            return []
    
    def print_layer_list(self, layers: List[LayerInfo], 
                        detailed: bool = False,
                        indent: bool = True) -> None:
        """Print layer list.
        
        Args:
            layers: List of layers
            detailed: Show detailed information
            indent: Indent nested layers
        """
        if not layers:
            print("\nNo layers found")
            return
        
        print(f"\nFound {len(layers)} layer(s):")
        
        def get_indent(layer: LayerInfo) -> str:
            """Get layer indentation."""
            if not indent or not layer.parent:
                return ""
            return "  " * len(layer.parent.split("/"))
        
        for i, layer in enumerate(layers, 1):
            if detailed:
                print(f"\n{get_indent(layer)}{i}. {layer}")
            else:
                print(f"{get_indent(layer)}{i}. {layer.name} ({layer.type.name})")

def main() -> None:
    """List layers example."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        manager = LayerManager(app)
        
        # List all layers
        print("\n=== All Layers ===")
        layers = manager.list_layers(sort_by=LayerSortBy.NAME)
        manager.print_layer_list(layers, detailed=True)
        
        # Find text layers
        print("\n=== Text Layers ===")
        text_layers = manager.find_layers(layer_type=LayerType.TEXT)
        manager.print_layer_list(text_layers)
        
        # Find visible layers
        print("\n=== Visible Layers ===")
        visible = manager.find_layers(visible_only=True)
        manager.print_layer_list(visible)
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
