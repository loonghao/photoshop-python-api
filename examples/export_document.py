"""Example of exporting Photoshop documents in various formats.

This script demonstrates how to:
1. Export documents in different formats (PNG, JPEG, etc.)
2. Configure export options for each format
3. Handle export errors and exceptions
4. Export specific layers or layer groups
"""

from __future__ import annotations

import os
from enum import Enum
from tempfile import mkdtemp
from typing import Optional

import examples._psd_files as psd  # Import from examples

from photoshop import Session

class ExportFormat(Enum):
    """Supported export formats."""
    PNG = "png"
    JPEG = "jpg"
    GIF = "gif"

def export_document(ps: Session, output_path: str, format: ExportFormat, 
                   layer_name: Optional[str] = None) -> bool:
    """Export the active document or a specific layer.
    
    Args:
        ps: Photoshop session instance
        output_path: Path to save the exported file
        format: Export format
        layer_name: Name of the layer to export (optional)
        
    Returns:
        bool: True if export was successful, False otherwise
    """
    try:
        doc = ps.app.activeDocument
        
        # If layer name is specified, make it visible and hide others
        if layer_name:
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                // Hide all layers
                for (var i = 0; i < doc.layers.length; i++) {{
                    doc.layers[i].visible = false;
                }}
                // Show target layer
                var found = false;
                for (var i = 0; i < doc.layers.length; i++) {{
                    if (doc.layers[i].name === "{layer_name}") {{
                        doc.layers[i].visible = true;
                        found = true;
                        break;
                    }}
                }}
                found ? "success" : "Layer not found"
            }} catch(e) {{
                e.message
            }}
            """
            result = ps.app.doJavaScript(js_code)
            if result != "success":
                print(f"Error preparing layer: {result}")
                return False
        
        # Export document using JavaScript
        output_path_js = output_path.replace("\\", "/")
        js_code = f"""
        try {{
            var doc = app.activeDocument;
            var file = new File("{output_path_js}");
            
            // Configure export options
            var opts = new ExportOptionsSaveForWeb();
            if ("{format.value}" === "png") {{
                opts.format = SaveDocumentType.PNG;
                opts.PNG8 = false;
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
            }}
            
            // Export document
            doc.exportDocument(file, ExportType.SAVEFORWEB, opts);
            "success"
        }} catch(e) {{
            e.message
        }}
        """
        result = ps.app.doJavaScript(js_code)
        if result != "success":
            print(f"Error during export: {result}")
            return False
        
        print(f"Successfully exported to: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error exporting document: {e}")
        return False

def get_document_layers(ps: Session) -> list[str]:
    """Get names of all layers in the active document.
    
    Args:
        ps: Photoshop session instance
        
    Returns:
        list[str]: List of layer names
    """
    js_code = """
    try {
        var doc = app.activeDocument;
        var layers = [];
        for (var i = 0; i < doc.layers.length; i++) {
            layers.push(doc.layers[i].name);
        }
        layers.join("\\n")
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js_code)
    if isinstance(result, str) and not result.startswith("Error"):
        return result.split("\n")
    return []

def main() -> None:
    """Export a Photoshop document in various formats.
    
    This function demonstrates how to:
    1. Open a PSD file
    2. List available layers
    3. Export in different formats
    4. Export specific layers
    """
    # Get sample PSD file
    psd_file = psd.get_psd_files()["export_layers_as_png.psd"]
    
    # Create output directory
    temp_dir = os.path.join(mkdtemp(), "photoshop_exports")
    os.makedirs(temp_dir, exist_ok=True)
    
    with Session(psd_file, action="open", auto_close=True) as ps:
        try:
            # List available layers
            layers = get_document_layers(ps)
            if layers:
                print("\nAvailable layers:")
                for layer in layers:
                    print(f"- {layer}")
            
            # Export in different formats
            for format in ExportFormat:
                output_path = os.path.join(temp_dir, f"export.{format.value}")
                if export_document(ps, output_path, format):
                    print(f"Exported full document as {format.name}")
            
            # Export specific layers as PNG
            for layer in layers:
                output_path = os.path.join(temp_dir, f"layer_{layer}.png")
                if export_document(ps, output_path, ExportFormat.PNG, layer):
                    print(f"Exported layer: {layer}")
            
            # Open output directory
            print(f"\nExports saved to: {temp_dir}")
            os.startfile(temp_dir)
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
