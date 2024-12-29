"""Export layers from a Photoshop document as PNG files.

This script demonstrates how to:
1. Export individual layers as PNG files
2. Configure PNG export options
3. Handle layer visibility and selection
4. Process layer groups and nested layers
5. Handle export errors and exceptions
"""

from __future__ import annotations

import os
from tempfile import mkdtemp
from typing import Any

import examples._psd_files as psd  # Import from examples

from photoshop import Session

class LayerExporter:
    """Class for exporting Photoshop layers."""
    
    def __init__(self, ps: Session, output_dir: str) -> None:
        """Initialize the layer exporter.
        
        Args:
            ps: Photoshop session instance
            output_dir: Directory to save exported files
        """
        self.ps = ps
        self.doc = ps.active_document
        self.output_dir = output_dir
        self.export_count = 0
        self.error_count = 0
    
    def configure_png_options(self) -> Any:
        """Configure PNG export options.
        
        Returns:
            PNG save options object
        """
        options = self.ps.PNGSaveOptions()
        options.compression = 1  # 0-9 (0=none, 9=maximum)
        options.interlaced = False
        return options
    
    def hide_all_layers(self) -> None:
        """Hide all layers in the document."""
        js_code = """
        try {
            var doc = app.activeDocument;
            var hideLayer = function(layer) {
                layer.visible = false;
                if (layer.layers) {
                    for (var i = 0; i < layer.layers.length; i++) {
                        hideLayer(layer.layers[i]);
                    }
                }
            }
            for (var i = 0; i < doc.layers.length; i++) {
                hideLayer(doc.layers[i]);
            }
            "success"
        } catch(e) {
            e.message
        }
        """
        result = self.ps.app.doJavaScript(js_code)
        if result != "success":
            print(f"Warning: Error hiding layers: {result}")
    
    def show_layer(self, layer_name: str) -> bool:
        """Make a specific layer visible.
        
        Args:
            layer_name: Name of the layer to show
            
        Returns:
            bool: True if layer was found and made visible
        """
        js_code = f"""
        try {{
            var doc = app.activeDocument;
            var findLayer = function(container, name) {{
                for (var i = 0; i < container.layers.length; i++) {{
                    var layer = container.layers[i];
                    if (layer.name === name) {{
                        layer.visible = true;
                        return true;
                    }}
                    if (layer.layers && findLayer(layer, name)) {{
                        return true;
                    }}
                }}
                return false;
            }}
            findLayer(doc, "{layer_name}") ? "success" : "Layer not found"
        }} catch(e) {{
            e.message
        }}
        """
        result = self.ps.app.doJavaScript(js_code)
        return result == "success"
    
    def get_all_layers(self) -> list[str]:
        """Get names of all layers in the document.
        
        Returns:
            list[str]: List of layer names
        """
        js_code = """
        try {
            var doc = app.activeDocument;
            var layers = [];
            var getLayers = function(container) {
                for (var i = 0; i < container.layers.length; i++) {
                    var layer = container.layers[i];
                    layers.push(layer.name);
                    if (layer.layers) {
                        getLayers(layer);
                    }
                }
            }
            getLayers(doc);
            layers.join("\\n")
        } catch(e) {
            e.message
        }
        """
        result = self.ps.app.doJavaScript(js_code)
        if isinstance(result, str) and not result.startswith("Error"):
            return result.split("\n")
        return []
    
    def export_layer(self, layer_name: str) -> bool:
        """Export a single layer as PNG.
        
        Args:
            layer_name: Name of the layer to export
            
        Returns:
            bool: True if export was successful
        """
        try:
            # Hide all layers and show target layer
            self.hide_all_layers()
            if not self.show_layer(layer_name):
                print(f"Error: Layer '{layer_name}' not found")
                self.error_count += 1
                return False
            
            # Create layer directory
            layer_dir = os.path.join(self.output_dir, layer_name)
            os.makedirs(layer_dir, exist_ok=True)
            
            # Configure export options
            options = self.configure_png_options()
            
            # Export layer
            image_path = os.path.join(layer_dir, f"{layer_name}.png")
            image_path = image_path.replace("\\", "/")  # Fix path for Photoshop
            self.doc.saveAs(image_path, options=options, asCopy=True)
            
            print(f"Successfully exported: {image_path}")
            self.export_count += 1
            return True
            
        except Exception as e:
            print(f"Error exporting layer '{layer_name}': {e}")
            self.error_count += 1
            return False
    
    def export_all_layers(self) -> None:
        """Export all layers as PNG files."""
        layers = self.get_all_layers()
        if not layers:
            print("No layers found in document")
            return
        
        print(f"\nFound {len(layers)} layers:")
        for layer in layers:
            print(f"- {layer}")
        
        print("\nExporting layers...")
        for layer in layers:
            self.export_layer(layer)
        
        print("\nExport complete!")
        print(f"Successfully exported: {self.export_count} layers")
        print(f"Failed to export: {self.error_count} layers")
        print(f"Output directory: {self.output_dir}")

def main() -> None:
    """Export layers from a Photoshop document as PNG files."""
    # Get sample PSD file
    psd_file = psd.get_psd_files()["export_layers_as_png.psd"]
    
    # Create output directory
    temp_dir = os.path.join(mkdtemp(), "photoshop_layers")
    os.makedirs(temp_dir, exist_ok=True)
    
    with Session(psd_file, action="open", auto_close=True) as ps:
        try:
            # Create exporter and export layers
            exporter = LayerExporter(ps, temp_dir)
            exporter.export_all_layers()
            
            # Open output directory
            os.startfile(temp_dir)
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
