"""Replace images in Photoshop layers.

This script demonstrates how to:
1. Replace image contents in a placed layer
2. Resize replaced image to match original dimensions
3. Handle layer bounds and dimensions
4. Manage image replacement errors
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple, Union

import examples._psd_files as psd  # Import from examples
import photoshop.api as ps
from photoshop import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

@dataclass
class ImageBounds:
    """Image bounds information."""
    left: float
    top: float
    right: float
    bottom: float
    
    @property
    def width(self) -> float:
        """Get image width."""
        return self.right - self.left
    
    @property
    def height(self) -> float:
        """Get image height."""
        return self.bottom - self.top
    
    @classmethod
    def from_bounds(cls, bounds: Tuple[float, float, float, float]) -> ImageBounds:
        """Create ImageBounds from bounds tuple.
        
        Args:
            bounds: Bounds tuple (left, top, right, bottom)
            
        Returns:
            ImageBounds object
        """
        return cls(bounds[0], bounds[1], bounds[2], bounds[3])

class ImageReplacer:
    """Class for replacing images in Photoshop layers."""
    
    def __init__(self, session: Session) -> None:
        """Initialize image replacer.
        
        Args:
            session: Photoshop session
        """
        self.session = session
        self.doc = session.active_document
        self.app = session.app
    
    def get_active_layer(self) -> Optional[ps.ArtLayer]:
        """Get active layer.
        
        Returns:
            Active layer if exists, None otherwise
        """
        try:
            return self.doc.activeLayer
            
        except Exception as e:
            logger.error(f"Error getting active layer: {e}")
            return None
    
    def get_layer_bounds(self, layer: ps.ArtLayer) -> Optional[ImageBounds]:
        """Get layer bounds.
        
        Args:
            layer: Layer to get bounds for
            
        Returns:
            Layer bounds if successful, None otherwise
        """
        try:
            bounds = layer.bounds
            return ImageBounds.from_bounds(bounds)
            
        except Exception as e:
            logger.error(f"Error getting layer bounds: {e}")
            return None
    
    def replace_image(self, image_path: Union[str, Path]) -> bool:
        """Replace image in active layer.
        
        Args:
            image_path: Path to replacement image
            
        Returns:
            True if successful
        """
        try:
            # Get active layer
            layer = self.get_active_layer()
            if not layer:
                logger.error("No active layer")
                return False
            
            # Get original bounds
            original_bounds = self.get_layer_bounds(layer)
            if not original_bounds:
                logger.error("Could not get layer bounds")
                return False
            
            logger.info(f"Original layer '{layer.name}' bounds: {original_bounds}")
            
            # Replace image contents
            replace_contents = self.app.stringIDToTypeID("placedLayerReplaceContents")
            desc = self.session.ActionDescriptor
            idnull = self.app.charIDToTypeID("null")
            desc.putPath(idnull, str(image_path))
            
            try:
                self.app.executeAction(replace_contents, desc)
                logger.info("Image contents replaced successfully")
            except Exception as e:
                logger.error(f"Error replacing image contents: {e}")
                return False
            
            # Get new bounds
            layer = self.get_active_layer()
            if not layer:
                logger.error("Could not get active layer after replacement")
                return False
            
            current_bounds = self.get_layer_bounds(layer)
            if not current_bounds:
                logger.error("Could not get layer bounds after replacement")
                return False
            
            logger.info(f"New layer bounds: {current_bounds}")
            
            # Calculate and apply resize
            try:
                new_size = original_bounds.width / current_bounds.width * 100
                layer.resize(new_size, new_size, self.session.AnchorPosition.MiddleCenter)
                logger.info(f"Resized layer to {new_size}%")
                return True
                
            except Exception as e:
                logger.error(f"Error resizing layer: {e}")
                return False
            
        except Exception as e:
            logger.error(f"Error replacing image: {e}")
            return False

def main() -> None:
    """Image replacement example."""
    try:
        # Get PSD files
        psd_files = psd.get_psd_files()
        template_path = psd_files["replace_images.psd"]
        replacement_path = psd_files["red_100x200.png"]
        
        # Process template
        with Session(template_path, action="open") as pss:
            print("\n=== Image Replacement ===")
            
            # Replace image
            replacer = ImageReplacer(pss)
            if replacer.replace_image(replacement_path):
                print("Image replaced successfully")
            else:
                print("Failed to replace image")
            
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
