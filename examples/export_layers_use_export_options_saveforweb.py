"""Export layers from a Photoshop document using SaveForWeb options.

This script demonstrates how to:
1. Export layers using SaveForWeb options
2. Configure various export formats and settings
3. Handle layer visibility and selection
4. Process layer groups and nested layers
5. Handle export errors and exceptions
"""

from __future__ import annotations

import os
from enum import Enum
from tempfile import mkdtemp

import examples._psd_files as psd  # Import from examples

from photoshop import Session

class ExportFormat(Enum):
    """Supported export formats."""
    PNG = "png"
    JPEG = "jpg"
    GIF = "gif"

class WebExporter:
    """Class for exporting Photoshop layers using SaveForWeb options."""
    
    def __init__(self, ps: Session, output_dir: str) -> None:
        """Initialize the web exporter.
        
        Args:
            ps: Photoshop session instance
            output_dir: Directory to save exported files
        """
        self.ps = ps
        self.doc = ps.active_document
        self.output_dir = output_dir
        self.export_count = 0
        self.error_count = 0
    
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
    
    def export_layer(self, layer_name: str, format: ExportFormat) -> bool:
        """Export a single layer using SaveForWeb options.
        
        Args:
            layer_name: Name of the layer to export
            format: Export format
            
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
            
            # Export layer using JavaScript
            output_path = os.path.join(layer_dir, f"{layer_name}.{format.value}")
            output_path_js = output_path.replace("\\", "/")
            
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                var file = new File("{output_path_js}");
                
                // Configure export options
                var opts = new ExportOptionsSaveForWeb();
                if ("{format.value}" === "png") {{
                    opts.format = SaveDocumentType.PNG;
                    opts.PNG8 = false;  // Use PNG-24
                    opts.transparency = true;
                    opts.interlaced = false;
                    opts.quality = 100;
                }} else if ("{format.value}" === "jpg") {{
                    opts.format = SaveDocumentType.JPEG;
                    opts.quality = 90;
                    opts.optimized = true;
                    opts.progressive = true;
                }} else if ("{format.value}" === "gif") {{
                    opts.format = SaveDocumentType.COMPUSERVEGIF;
                    opts.transparency = true;
                    opts.dither = Dither.DIFFUSION;
                    opts.ditherAmount = 75;
                    opts.lossy = 0;
                    opts.colors = 256;
                }}
                
                // Export document
                doc.exportDocument(file, ExportType.SAVEFORWEB, opts);
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            if result != "success":
                print(f"Error during export: {result}")
                self.error_count += 1
                return False
            
            print(f"Successfully exported: {output_path}")
            self.export_count += 1
            return True
            
        except Exception as e:
            print(f"Error exporting layer '{layer_name}': {e}")
            self.error_count += 1
            return False
    
    def export_all_layers(self, formats: list[ExportFormat]) -> None:
        """Export all layers in specified formats.
        
        Args:
            formats: List of formats to export in
        """
        layers = self.get_all_layers()
        if not layers:
            print("No layers found in document")
            return
        
        print(f"\nFound {len(layers)} layers:")
        for layer in layers:
            print(f"- {layer}")
        
        print("\nExporting layers...")
        for layer in layers:
            for format in formats:
                self.export_layer(layer, format)
        
        print("\nExport complete!")
        print(f"Successfully exported: {self.export_count} files")
        print(f"Failed to export: {self.error_count} files")
        print(f"Output directory: {self.output_dir}")

def main() -> None:
    """Export layers from a Photoshop document using SaveForWeb options."""
    # Get sample PSD file
    psd_file = psd.get_psd_files()["export_layers_as_png.psd"]
    
    # Create output directory
    temp_dir = os.path.join(mkdtemp(), "photoshop_exports")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Define export formats
    formats = [
        ExportFormat.PNG,
        ExportFormat.JPEG,
        ExportFormat.GIF,
    ]
    
    with Session(psd_file, action="open", auto_close=True) as ps:
        try:
            # Create exporter and export layers
            exporter = WebExporter(ps, temp_dir)
            exporter.export_all_layers(formats)
            
            # Open output directory
            os.startfile(temp_dir)
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
