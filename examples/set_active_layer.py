"""Example script demonstrating how to manage active layers in Photoshop.

This script shows how to:
1. Create a document with multiple layers
2. Navigate between layers
3. Get and set the active layer
4. Modify layer properties
5. Handle layer selection errors

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ActiveLayer.py
"""

# Import built-in modules
from __future__ import annotations

import logging
from typing import Any, List

# Import local modules
from photoshop import Session
import photoshop.api as ps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_sample_layers(doc: Any) -> List[Any]:
    """Create sample layers in the document.

    Args:
        doc: Active Photoshop document.

    Returns:
        List of created layers.
    """
    try:
        layers = []
        
        # Create text layers
        for i in range(3):
            layer = doc.artLayers.add()
            layer.kind = ps.LayerKind.TextLayer
            layer.name = f"Text Layer {i+1}"
            layer.textItem.contents = f"Sample Text {i+1}"
            layer.textItem.position = [50, 50 + i * 50]
            layer.textItem.size = 24
            layers.append(layer)
            logger.info("Created text layer: %s", layer.name)

        # Create shape layers
        for i in range(2):
            layer = doc.artLayers.add()
            layer.name = f"Shape Layer {i+1}"
            
            # Create and fill selection
            doc.selection.select([
                [200 + i * 150, 100],
                [300 + i * 150, 100],
                [300 + i * 150, 200],
                [200 + i * 150, 200],
            ])
            
            # Create different colors for shapes
            fill_color = ps.SolidColor()
            if i == 0:
                fill_color.rgb.red = 255
                fill_color.rgb.green = 200
                fill_color.rgb.blue = 200
            else:
                fill_color.rgb.red = 200
                fill_color.rgb.green = 255
                fill_color.rgb.blue = 200
            
            doc.selection.fill(fill_color)
            doc.selection.deselect()
            
            layers.append(layer)
            logger.info("Created shape layer: %s", layer.name)

        return layers

    except Exception as e:
        logger.error("Failed to create sample layers: %s", str(e))
        return []


def set_active_layer(
    doc: Any,
    target: Any,
    by_name: bool = False,
) -> bool:
    """Set the active layer in the document.

    Args:
        doc: Active Photoshop document.
        target: Layer object or layer name to activate.
        by_name: If True, target is a layer name. If False, target is a layer object.

    Returns:
        True if successful, False otherwise.
    """
    try:
        if by_name:
            # Find layer by name
            for i in range(doc.layers.length):
                layer = doc.layers[i]
                if layer.name == target:
                    doc.activeLayer = layer
                    logger.info("Activated layer by name: %s", target)
                    return True
            logger.error("Layer not found: %s", target)
            return False
        # Set layer directly
        doc.activeLayer = target
        logger.info("Activated layer: %s", target.name)
        return True

    except Exception as e:
        logger.error("Failed to set active layer: %s", str(e))
        return False


def get_layer_info(layer: Any) -> None:
    """Log information about a layer.

    Args:
        layer: Photoshop layer object.
    """
    try:
        logger.info("Layer Info:")
        logger.info("  Name: %s", layer.name)
        logger.info("  Kind: %s", layer.kind)
        logger.info("  Visible: %s", layer.visible)
        logger.info("  Opacity: %d%%", layer.opacity)
        
        if layer.kind == ps.LayerKind.TextLayer:
            logger.info("  Text: %s", layer.textItem.contents)
            logger.info("  Font Size: %d", layer.textItem.size)

    except Exception as e:
        logger.error("Failed to get layer info: %s", str(e))


def main() -> None:
    """Main function demonstrating layer management."""
    try:
        with Session(action="new_document") as ps:
            doc = ps.active_document

            # Create sample layers
            layers = create_sample_layers(doc)
            if not layers:
                return

            # Show initial active layer
            logger.info("Initial active layer: %s", doc.activeLayer.name)

            # Cycle through layers
            for layer in layers:
                if set_active_layer(doc, layer):
                    get_layer_info(layer)

            # Try to activate layer by name
            if set_active_layer(doc, "Text Layer 1", by_name=True):
                get_layer_info(doc.activeLayer)

            # Show final active layer
            logger.info("Final active layer: %s", doc.activeLayer.name)

    except Exception as e:
        logger.error("Session failed: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting layer management example...")
        main()
        logger.info("Layer management example completed successfully")
    except Exception as e:
        logger.error("Layer management example failed: %s", str(e))
        raise
