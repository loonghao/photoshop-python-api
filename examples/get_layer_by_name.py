"""Manage and retrieve Photoshop layers by name.

This script demonstrates how to:
1. Get layer by name
2. List all layers in document
3. Get layer properties
4. Handle layer errors
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Optional

import examples._psd_files as psd  # Import from examples
from photoshop import Session

class LayerType(Enum):
    """Types of Photoshop layers."""
    NORMAL = "normal"
    TEXT = "text"
    ADJUSTMENT = "adjustment"
    SHAPE = "shape"
    SMART_OBJECT = "smartObject"
    BACKGROUND = "background"
    GROUP = "group"

@dataclass
class LayerInfo:
    """Information about a Photoshop layer."""
    name: str
    type: LayerType
    visible: bool
    opacity: float
    blend_mode: str
    locked: bool
    linked: bool

class LayerManager:
    """Class for managing Photoshop layers."""
    
    def __init__(self, ps: Session) -> None:
        """Initialize the layer manager.
        
        Args:
            ps: Photoshop session instance
        """
        self.ps = ps
    
    def ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists
        """
        try:
            if len(self.ps.app.documents) < 1:
                print("Error: No document is open")
                return False
            return True
        except Exception as e:
            print(f"Error checking document: {e}")
            return False
    
    def list_layers(self, include_hidden: bool = True) -> List[str]:
        """List all layers in the active document.
        
        Args:
            include_hidden: Whether to include hidden layers
            
        Returns:
            List of layer names
        """
        try:
            if not self.ensure_document_exists():
                return []
            
            doc = self.ps.active_document
            layers = []
            
            # Get all art layers
            for layer in doc.artLayers:
                if include_hidden or layer.visible:
                    layers.append(layer.name)
            
            if layers:
                print("\nLayers in document:")
                for name in layers:
                    print(f"- {name}")
            else:
                print("No layers found")
                
            return layers
            
        except Exception as e:
            print(f"Error listing layers: {e}")
            return []
    
    def get_layer_by_name(self, name: str) -> Optional[Any]:
        """Get layer by name.
        
        Args:
            name: Layer name to find
            
        Returns:
            Layer object if found, None otherwise
        """
        try:
            if not self.ensure_document_exists():
                return None
            
            layer = self.ps.active_document.artLayers.getByName(name)
            print(f"\nFound layer: {layer.name}")
            return layer
            
        except Exception as e:
            print(f"Error getting layer '{name}': {e}")
            return None
    
    def get_layer_info(self, layer: Any) -> Optional[LayerInfo]:
        """Get detailed information about a layer.
        
        Args:
            layer: Layer object
            
        Returns:
            LayerInfo object if successful, None otherwise
        """
        try:
            # Get layer properties using JavaScript
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                var layer = doc.artLayers.getByName("{layer.name}");
                var result = layer.visible + "," + layer.opacity + "," + layer.blendMode + "," + layer.allLocked;
                result
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            
            try:
                # Parse JavaScript result
                visible, opacity, blend_mode, locked = result.split(",")
                
                # Determine layer type
                layer_type = LayerType.NORMAL
                try:
                    if layer.kind == self.ps.LayerKind.TextLayer:
                        layer_type = LayerType.TEXT
                    elif layer.kind == self.ps.LayerKind.AdjustmentLayer:
                        layer_type = LayerType.ADJUSTMENT
                    elif layer.kind == self.ps.LayerKind.SmartObject:
                        layer_type = LayerType.SMART_OBJECT
                    elif layer.isBackgroundLayer:
                        layer_type = LayerType.BACKGROUND
                except Exception:
                    print("Warning: Could not determine layer type")
                
                # Create layer info
                info = LayerInfo(
                    name=layer.name,
                    type=layer_type,
                    visible=visible.lower() == "true",
                    opacity=float(opacity),
                    blend_mode=str(blend_mode),
                    locked=locked.lower() == "true",
                    linked=False,  # Simplified for now
                )
                
                print(f"\nLayer information for {info.name}:")
                print(f"- Type: {info.type.value}")
                print(f"- Visible: {info.visible}")
                print(f"- Opacity: {info.opacity:.1f}%")
                print(f"- Blend Mode: {info.blend_mode}")
                print(f"- Locked: {info.locked}")
                print(f"- Linked: {info.linked}")
                
                return info
                
            except Exception as e:
                print(f"Error parsing layer properties: {e}")
                return None
            
        except Exception as e:
            print(f"Error getting layer info: {e}")
            return None
    
    def layer_exists(self, name: str) -> bool:
        """Check if a layer exists.
        
        Args:
            name: Layer name to check
            
        Returns:
            True if layer exists
        """
        try:
            self.ps.active_document.artLayers.getByName(name)
            return True
        except Exception:
            return False

def main() -> None:
    """Demonstrate layer management."""
    # Get sample PSD file
    PSD_FILE = psd.get_psd_files()
    psd_path = PSD_FILE["export_layers_as_png.psd"]
    
    # Open document and manage layers
    with Session(psd_path, action="open", auto_close=True) as ps:
        try:
            print("\nInitializing layer manager...")
            manager = LayerManager(ps)
            
            # List all layers
            manager.list_layers()
            
            # Get layer by name
            layer_name = "blue"
            if manager.layer_exists(layer_name):
                layer = manager.get_layer_by_name(layer_name)
                if layer:
                    # Get layer info
                    manager.get_layer_info(layer)
            else:
                print(f"\nLayer '{layer_name}' not found")
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
