"""Link layers in Photoshop.

This script demonstrates how to:
1. Link multiple layers together
2. Unlink layers
3. Check layer link status
4. Manage layer links with groups
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Set, Union

import photoshop.api as ps
from photoshop.api._artlayer import ArtLayer
from photoshop.api._layerSet import LayerSet

@dataclass
class LayerLinkOptions:
    """Options for linking layers."""
    preserve_position: bool = True  # Keep layer positions when linking
    include_effects: bool = True  # Include layer effects in linking
    include_masks: bool = True  # Include layer masks in linking

class LayerLinker:
    """Class for managing layer links."""
    
    def __init__(self, app: ps.Application) -> None:
        """Initialize layer linker.
        
        Args:
            app: Photoshop application instance
        """
        self.app = app
        self.doc = None
        self.linked_groups: Set[str] = set()  # Track linked groups by name
        self._save_ruler_units()
    
    def _save_ruler_units(self) -> None:
        """Save current ruler units."""
        self.start_ruler_units = self.app.preferences.rulerUnits
        if self.start_ruler_units is not ps.Units.Pixels:
            self.app.preferences.rulerUnits = ps.Units.Pixels
    
    def _restore_ruler_units(self) -> None:
        """Restore original ruler units."""
        self.app.preferences.rulerUnits = self.start_ruler_units
    
    def ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists or was created
        """
        try:
            if len(self.app.documents) < 1:
                # Create new document
                self.doc = self.app.documents.add(
                    width=320,
                    height=240,
                    resolution=72,
                    title=None,
                    mode=ps.NewDocumentMode.NewRGB,
                    initialFill=ps.DocumentFill.BackgroundColor,
                )
                print("\nCreated new document: 320x240 pixels")
            else:
                self.doc = self.app.activeDocument
            return True
        except Exception as e:
            print(f"Error ensuring document exists: {e}")
            return False
    
    def get_layer(self, layer: Union[str, ArtLayer, LayerSet]) -> Optional[Union[ArtLayer, LayerSet]]:
        """Get layer by name or object.
        
        Args:
            layer: Layer name or object
            
        Returns:
            Layer object if found, None otherwise
        """
        try:
            if isinstance(layer, str):
                # Search in art layers
                for art_layer in self.doc.artLayers:
                    if art_layer.name == layer:
                        return art_layer
                # Search in layer sets
                for layer_set in self.doc.layerSets:
                    if layer_set.name == layer:
                        return layer_set
                print(f"Error: Layer not found: {layer}")
                return None
            return layer
        except Exception as e:
            print(f"Error getting layer: {e}")
            return None
    
    def link_layers(self, layers: List[Union[str, ArtLayer, LayerSet]], 
                   options: LayerLinkOptions = None) -> bool:
        """Link multiple layers together.
        
        Args:
            layers: List of layer names or objects
            options: Link options
            
        Returns:
            bool: True if successful
        """
        try:
            if not self.ensure_document_exists():
                return False
            
            if not options:
                options = LayerLinkOptions()
            
            # Get layer objects
            layer_objects = []
            for layer in layers:
                layer_obj = self.get_layer(layer)
                if layer_obj:
                    layer_objects.append(layer_obj)
                
            if len(layer_objects) < 2:
                print("Error: Need at least 2 layers to link")
                return False
            
            # Link layers
            for i in range(1, len(layer_objects)):
                try:
                    # Use JavaScript to link layers with options
                    js_code = f"""
                    try {{
                        var layer1 = app.activeDocument.layers.getByName("{layer_objects[0].name}");
                        var layer2 = app.activeDocument.layers.getByName("{layer_objects[i].name}");
                        
                        // Link layers
                        layer1.link(layer2);
                        
                        // Apply options
                        layer1.preserveTransparency = {str(options.preserve_position).lower()};
                        layer2.preserveTransparency = {str(options.preserve_position).lower()};
                        
                        "success"
                    }} catch(e) {{
                        e.message
                    }}
                    """
                    
                    result = self.app.doJavaScript(js_code)
                    if result != "success":
                        print(f"Error linking layers: {result}")
                        return False
                        
                    print(f"Linked layers: {layer_objects[0].name} <-> {layer_objects[i].name}")
                    
                except Exception as e:
                    print(f"Error linking layers: {e}")
                    return False
            
            return True
            
        except Exception as e:
            print(f"Error linking layers: {e}")
            return False
        finally:
            self._restore_ruler_units()
    
    def unlink_layer(self, layer: Union[str, ArtLayer, LayerSet]) -> bool:
        """Unlink a layer from all its links.
        
        Args:
            layer: Layer name or object
            
        Returns:
            bool: True if successful
        """
        try:
            if not self.ensure_document_exists():
                return False
            
            layer_obj = self.get_layer(layer)
            if not layer_obj:
                return False
            
            # Use JavaScript to unlink layer
            js_code = f"""
            try {{
                var layer = app.activeDocument.layers.getByName("{layer_obj.name}");
                layer.unlink();
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            
            result = self.app.doJavaScript(js_code)
            if result != "success":
                print(f"Error unlinking layer: {result}")
                return False
            
            print(f"Unlinked layer: {layer_obj.name}")
            return True
            
        except Exception as e:
            print(f"Error unlinking layer: {e}")
            return False
        finally:
            self._restore_ruler_units()
    
    def is_linked(self, layer: Union[str, ArtLayer, LayerSet]) -> bool:
        """Check if a layer is linked.
        
        Args:
            layer: Layer name or object
            
        Returns:
            bool: True if layer is linked
        """
        try:
            if not self.ensure_document_exists():
                return False
            
            layer_obj = self.get_layer(layer)
            if not layer_obj:
                return False
            
            # Use JavaScript to check link status
            js_code = f"""
            try {{
                var layer = app.activeDocument.layers.getByName("{layer_obj.name}");
                layer.linked
            }} catch(e) {{
                e.message
            }}
            """
            
            result = self.app.doJavaScript(js_code)
            return result == "true"
            
        except Exception as e:
            print(f"Error checking layer link status: {e}")
            return False
        finally:
            self._restore_ruler_units()

def main() -> None:
    """Demonstrate layer linking."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        linker = LayerLinker(app)
        
        # Create new document if needed
        if not linker.ensure_document_exists():
            return
        
        # Create test layers
        layer1 = linker.doc.artLayers.add()
        layer1.name = "Layer 1"
        layer2 = linker.doc.artLayers.add()
        layer2.name = "Layer 2"
        layer3 = linker.doc.artLayers.add()
        layer3.name = "Layer 3"
        
        print("\nCreated test layers:")
        print(f"- {layer1.name}")
        print(f"- {layer2.name}")
        print(f"- {layer3.name}")
        
        # Create link options
        options = LayerLinkOptions(
            preserve_position=True,
            include_effects=True,
            include_masks=True,
        )
        
        # Link layers
        linker.link_layers([layer1, layer2, layer3], options)
        
        # Check link status
        for layer in [layer1, layer2, layer3]:
            is_linked = linker.is_linked(layer)
            print(f"\n{layer.name} is {'linked' if is_linked else 'not linked'}")
        
        # Unlink a layer
        linker.unlink_layer(layer2)
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
