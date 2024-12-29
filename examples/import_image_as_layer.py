"""Import images as layers in Photoshop.

This script demonstrates how to:
1. Import images as layers
2. Set layer properties
3. Adjust layer position and size
4. Handle multiple image formats
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional, Tuple, Union

import examples._psd_files as psd  # Import from examples
from photoshop import Session

class ImageFormat(Enum):
    """Supported image formats."""
    JPEG = ".jpg"
    PNG = ".png"
    TIFF = ".tif"
    PSD = ".psd"

@dataclass
class ImportOptions:
    """Options for importing images."""
    position: Tuple[float, float] = (0, 0)  # x, y coordinates
    scale: float = 100.0  # Scale percentage
    opacity: float = 100.0  # Layer opacity
    blend_mode: str = "normal"  # Layer blend mode
    linked: bool = False  # Link with other layers

class ImageImporter:
    """Class for importing images as layers."""
    
    def __init__(self, ps: Session) -> None:
        """Initialize image importer.
        
        Args:
            ps: Photoshop session instance
        """
        self.ps = ps
        self.doc = None
        self.imported_layers = []
    
    def ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists
        """
        try:
            if len(self.ps.app.documents) < 1:
                print("Error: No document is open")
                return False
            self.doc = self.ps.active_document
            return True
        except Exception as e:
            print(f"Error checking document: {e}")
            return False
    
    def validate_image_path(self, image_path: Union[str, Path]) -> Optional[Path]:
        """Validate image path and format.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Path object if valid, None otherwise
        """
        try:
            path = Path(image_path).resolve()
            if not path.exists():
                print(f"Error: Image not found: {path}")
                return None
                
            ext = path.suffix.lower()
            if not any(ext == format.value for format in ImageFormat):
                print(f"Error: Unsupported image format: {ext}")
                print(f"Supported formats: {[f.value for f in ImageFormat]}")
                return None
                
            return path
            
        except Exception as e:
            print(f"Error validating image path: {e}")
            return None
    
    def import_image(self, image_path: Union[str, Path], 
                    options: ImportOptions = None) -> Optional[ps.ArtLayer]:
        """Import image as a layer.
        
        Args:
            image_path: Path to image file
            options: Import options
            
        Returns:
            Layer object if successful, None otherwise
        """
        try:
            # Validate inputs
            if not self.ensure_document_exists():
                return None
                
            path = self.validate_image_path(image_path)
            if not path:
                return None
            
            if not options:
                options = ImportOptions()
            
            # Convert path to Photoshop format
            ps_path = str(path).replace("\\", "/")
            
            # Import image using JavaScript
            js_code = f"""
            try {{
                var idPlc = charIDToTypeID("Plc ");
                var desc = new ActionDescriptor();
                desc.putPath(charIDToTypeID("null"), new File("{ps_path}"));
                executeAction(idPlc, desc, DialogModes.NO);
                
                // Get the imported layer
                var layer = app.activeDocument.activeLayer;
                
                // Set layer properties
                layer.opacity = {options.opacity};
                layer.blendMode = BlendMode.{options.blend_mode.upper()};
                layer.linked = {str(options.linked).lower()};
                
                // Move layer
                layer.translate({options.position[0]}, {options.position[1]});
                
                // Scale layer if needed
                if ({options.scale} != 100) {{
                    var scaleX = {options.scale};
                    var scaleY = {options.scale};
                    layer.resize(scaleX, scaleY, AnchorPosition.MIDDLECENTER);
                }}
                
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            
            result = self.ps.app.doJavaScript(js_code)
            if result != "success":
                print(f"Error importing image: {result}")
                return None
            
            # Get imported layer
            layer = self.ps.active_document.activeLayer
            self.imported_layers.append(layer)
            
            print(f"\nImported image: {path.name}")
            print(f"Position: {options.position}")
            print(f"Scale: {options.scale}%")
            print(f"Opacity: {options.opacity}%")
            print(f"Blend Mode: {options.blend_mode}")
            
            return layer
            
        except Exception as e:
            print(f"Error importing image: {e}")
            return None
    
    def import_multiple(self, image_paths: List[Union[str, Path]], 
                       options: ImportOptions = None) -> List[ps.ArtLayer]:
        """Import multiple images as layers.
        
        Args:
            image_paths: List of image paths
            options: Import options
            
        Returns:
            List of imported layers
        """
        layers = []
        for path in image_paths:
            layer = self.import_image(path, options)
            if layer:
                layers.append(layer)
        return layers

def main() -> None:
    """Demonstrate image importing."""
    try:
        # Get sample image
        PSD_FILE = psd.get_psd_files()
        image_path = PSD_FILE["layer_comps.psd"]
        
        print(f"Importing image: {image_path}")
        
        # Import image
        with Session(action="new_document") as ps:
            importer = ImageImporter(ps)
            
            # Create import options
            options = ImportOptions(
                position=(100, 100),
                scale=50,
                opacity=80,
                blend_mode="normal",  # Use normal blend mode for compatibility
                linked=False,
            )
            
            # Import image
            layer = importer.import_image(image_path, options)
            if not layer:
                return
            
            # Import multiple images
            image_paths = [
                PSD_FILE["layer_comps.psd"],
                PSD_FILE["slate_template.psd"],
            ]
            
            print("\nImporting multiple images:")
            for path in image_paths:
                print(f"- {path}")
            
            layers = importer.import_multiple(image_paths, options)
            print(f"\nImported {len(layers)} additional images")
            
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
