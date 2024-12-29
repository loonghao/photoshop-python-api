"""Photoshop layer rotation management.

This script demonstrates how to:
1. Rotate layers in Photoshop documents
2. Handle layer selection and validation
3. Manage layer transformations
4. Handle rotation errors

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/RotateLayer.py
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

import photoshop.api as ps
from photoshop import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class RotationDirection(Enum):
    """Rotation direction options."""
    CLOCKWISE = auto()
    COUNTERCLOCKWISE = auto()

@dataclass
class LayerInfo:
    """Layer information."""
    name: str
    type_name: str
    is_background: bool
    is_visible: bool
    
    @classmethod
    def from_layer(cls, layer: ps.ArtLayer) -> LayerInfo:
        """Create LayerInfo from Photoshop layer.
        
        Args:
            layer: Photoshop layer
            
        Returns:
            LayerInfo object
        """
        return cls(
            layer.name,
            layer.typename,
            layer.isBackgroundLayer,
            layer.visible,
        )

class LayerManager:
    """Class for managing Photoshop layer operations."""
    
    def __init__(self, session: Session) -> None:
        """Initialize layer manager.
        
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
    
    def get_layer_info(self, layer: ps.ArtLayer) -> Optional[LayerInfo]:
        """Get layer information.
        
        Args:
            layer: Layer to get information for
            
        Returns:
            Layer information if successful, None otherwise
        """
        try:
            return LayerInfo.from_layer(layer)
            
        except Exception as e:
            logger.error(f"Error getting layer info: {e}")
            return None
    
    def rotate_layer(self, 
                    angle: float, 
                    direction: RotationDirection = RotationDirection.CLOCKWISE,
                    layer: Optional[ps.ArtLayer] = None) -> bool:
        """Rotate layer by specified angle.
        
        Args:
            angle: Rotation angle in degrees
            direction: Rotation direction
            layer: Layer to rotate, uses active layer if None
            
        Returns:
            True if successful
        """
        try:
            # Get target layer
            target_layer = layer or self.get_active_layer()
            if not target_layer:
                logger.error("No target layer")
                return False
            
            # Get layer info
            layer_info = self.get_layer_info(target_layer)
            if not layer_info:
                logger.error("Could not get layer info")
                return False
            
            # Check if background layer
            if layer_info.is_background:
                logger.error("Cannot rotate background layer")
                return False
            
            # Calculate rotation angle
            if direction == RotationDirection.COUNTERCLOCKWISE:
                angle = -angle
            
            # Create JavaScript code for rotation
            js_code = """
            try {
                var doc = app.activeDocument;
                var layer = doc.activeLayer;
                
                // Select layer
                doc.activeLayer = layer;
                
                // Start transform
                var idTrnf = charIDToTypeID('Trnf');
                var desc = new ActionDescriptor();
                var ref = new ActionReference();
                ref.putEnumerated(charIDToTypeID('Lyr '), charIDToTypeID('Ordn'), charIDToTypeID('Trgt'));
                desc.putReference(charIDToTypeID('null'), ref);
                executeAction(idTrnf, desc, DialogModes.NO);
                
                // Rotate layer
                var idRtte = charIDToTypeID('Rtte');
                var desc2 = new ActionDescriptor();
                desc2.putUnitDouble(charIDToTypeID('Angl'), charIDToTypeID('#Ang'), ANGLE);
                executeAction(idRtte, desc2, DialogModes.NO);
                
                // Commit transform
                var idTrnf = charIDToTypeID('Trnf');
                var desc3 = new ActionDescriptor();
                executeAction(idTrnf, desc3, DialogModes.NO);
                
                $.writeln("Rotation successful");
            } catch(e) {
                // Cancel transform
                try {
                    var idRset = charIDToTypeID('Rset');
                    var desc4 = new ActionDescriptor();
                    executeAction(idRset, desc4, DialogModes.NO);
                } catch(e2) {}
                $.writeln("Error: " + e);
            }
            """
            
            # Replace placeholders
            js_code = js_code.replace("ANGLE", str(angle))
            
            # Execute JavaScript code
            logger.info(f"Rotating layer '{layer_info.name}' by {angle} degrees")
            result = self.app.doJavaScript(js_code)
            logger.info(f"JavaScript result: {result}")
            
            if "successful" in str(result):
                return True
            logger.error(f"Rotation failed: {result}")
            return False
            
        except Exception as e:
            logger.error(f"Error in rotate_layer: {e}")
            return False

def main() -> None:
    """Layer rotation example."""
    try:
        # Create new document
        with Session(action="new_document") as pss:
            print("\n=== Layer Rotation ===")
            
            # Create layer manager
            manager = LayerManager(pss)
            
            # Add new layer
            pss.active_document.artLayers.add()
            
            # Draw something on the layer
            js_code = """
            try {
                var doc = app.activeDocument;
                var layer = doc.activeLayer;
                
                // Create rectangle selection
                var idsetd = charIDToTypeID("setd");
                var desc = new ActionDescriptor();
                var idnull = charIDToTypeID("null");
                var ref = new ActionReference();
                var idChnl = charIDToTypeID("Chnl");
                var idfsel = charIDToTypeID("fsel");
                ref.putProperty(idChnl, idfsel);
                desc.putReference(idnull, ref);
                var idT = charIDToTypeID("T   ");
                var desc2 = new ActionDescriptor();
                var idTop = charIDToTypeID("Top ");
                desc2.putDouble(idTop, 100);
                var idLeft = charIDToTypeID("Left");
                desc2.putDouble(idLeft, 100);
                var idBtom = charIDToTypeID("Btom");
                desc2.putDouble(idBtom, 200);
                var idRght = charIDToTypeID("Rght");
                desc2.putDouble(idRght, 200);
                var idRctn = charIDToTypeID("Rctn");
                desc.putObject(idT, idRctn, desc2);
                executeAction(idsetd, desc, DialogModes.NO);
                
                // Fill selection
                var idFl = charIDToTypeID("Fl  ");
                var desc = new ActionDescriptor();
                var idUsng = charIDToTypeID("Usng");
                var idFlCn = charIDToTypeID("FlCn");
                var idFrgC = charIDToTypeID("FrgC");
                desc.putEnumerated(idUsng, idFlCn, idFrgC);
                executeAction(idFl, desc, DialogModes.NO);
                
                // Deselect
                var idsetd = charIDToTypeID("setd");
                var desc = new ActionDescriptor();
                var idnull = charIDToTypeID("null");
                var ref = new ActionReference();
                var idChnl = charIDToTypeID("Chnl");
                var idfsel = charIDToTypeID("fsel");
                ref.putProperty(idChnl, idfsel);
                desc.putReference(idnull, ref);
                var idT = charIDToTypeID("T   ");
                var idOrdn = charIDToTypeID("Ordn");
                var idNone = charIDToTypeID("None");
                desc.putEnumerated(idT, idOrdn, idNone);
                executeAction(idsetd, desc, DialogModes.NO);
                
                $.writeln("Drawing successful");
            } catch(e) {
                $.writeln("Error: " + e);
            }
            """
            
            # Execute JavaScript code
            logger.info("Drawing rectangle on layer")
            pss.app.doJavaScript(js_code)
            
            # Get active layer
            layer = manager.get_active_layer()
            if layer:
                # Get layer info
                layer_info = manager.get_layer_info(layer)
                if layer_info:
                    print(f"\nActive layer: {layer_info.name}")
                    print(f"Type: {layer_info.type_name}")
                    print(f"Is background: {layer_info.is_background}")
                    print(f"Is visible: {layer_info.is_visible}")
                
                # Rotate layer
                if manager.rotate_layer(45.0):
                    print("\nRotated layer 45 degrees clockwise")
                
                # Rotate layer counterclockwise
                if manager.rotate_layer(30.0, RotationDirection.COUNTERCLOCKWISE):
                    print("Rotated layer 30 degrees counterclockwise")
            
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
