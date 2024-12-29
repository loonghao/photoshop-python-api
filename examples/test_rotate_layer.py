"""Test the layer rotation functionality.

This script demonstrates how to use the rotate function to rotate layers in Photoshop.
"""

# Import built-in modules
import os
import sys
import logging
from pathlib import Path

# Import local modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from photoshop import Session
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.enumerations import SaveOptions

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def test_layer_rotation():
    """Test rotating layers with different angles."""
    try:
        # Start a new Photoshop session
        with Session() as ps:
            # Create a new document
            doc = ps.app.documents.add(
                width=500,
                height=500,
                resolution=72,
                name="RotationTest",
            )
            
            # Create a new layer
            layer = doc.artLayers.add()
            layer.name = "TestLayer"

            # Draw something on the layer for visibility
            # Use a rectangle for testing
            selection = ps.active_document.selection
            selection.select([[100, 100], [400, 100], [400, 400], [100, 400]])
            ps.app.foregroundColor.rgb.red = 255
            ps.app.foregroundColor.rgb.green = 0
            ps.app.foregroundColor.rgb.blue = 0
            selection.fill(ps.app.foregroundColor)
            selection.deselect()

            # Test different rotation angles
            test_angles = [45, 90, 180, -90, -45]
            
            for angle in test_angles:
                try:
                    logger.info(f"Testing rotation with angle: {angle}")
                    layer.rotate(angle)
                    # Add a small delay to make the rotation visible
                    ps.app.refresh()
                except PhotoshopPythonAPIError as e:
                    logger.error(f"Failed to rotate layer by {angle} degrees: {e!s}")
                    continue

            # Save the test document using JavaScript
            save_path = str(Path(__file__).parent / "rotation_test.psd")
            save_js = (
                'try {'
                f'    var saveFile = new File("{save_path.replace(os.sep, "/")}");'
                '    app.activeDocument.saveAs(saveFile);'
                '} catch(e) {'
                '    throw e;'
                '}'
            )
            ps.app.doJavaScript(save_js)
            logger.info(f"Test document saved to: {save_path}")

            # Close the document
            doc.close(SaveOptions.DoNotSaveChanges)

    except Exception as e:
        logger.error(f"Test failed with error: {e!s}")
        raise

if __name__ == "__main__":
    test_layer_rotation()
