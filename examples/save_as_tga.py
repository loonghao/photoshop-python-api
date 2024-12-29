"""Save current active document as a TGA (Targa) file.

This script demonstrates different ways to save a Photoshop document as TGA,
including various TGA options and settings.
"""

# Import built-in modules
from __future__ import annotations

import logging
import os
from tempfile import mkdtemp

# Import local modules
from photoshop import Session
from photoshop.api.enumerations import LayerKind

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def create_sample_document(ps, name="TGATest", width=500, height=500):
    """Create a sample document with some content.

    Args:
        ps: Photoshop session object
        name (str): Document name
        width (int): Document width
        height (int): Document height

    Returns:
        Document: Created document
    """
    # Create a new document
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=72,
        name=name,
    )

    # Add a text layer
    text_layer = doc.artLayers.add()
    text_layer.kind = LayerKind.TextLayer

    # Set text color to green
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    text_color.rgb.red = 0
    text_color.rgb.blue = 0

    # Configure text properties
    text_layer.textItem.contents = "Hello, TGA!"
    text_layer.textItem.position = [width//3, height//3]
    text_layer.textItem.size = 40
    text_layer.textItem.color = text_color

    return doc

def save_as_tga_simple():
    """Save document as TGA with basic settings."""
    try:
        with Session(action="new_document") as ps:
            # Create test document
            doc = create_sample_document(ps)

            # Basic TGA options
            options = ps.TargaSaveOptions()
            options.alphaChannels = True  # Include alpha channels
            options.resolution = 32  # 32-bit depth

            # Save the file
            tga_path = os.path.join(mkdtemp("photoshop-python-api"), "test_simple.tga")
            doc.saveAs(tga_path, options, asCopy=True)
            logger.info(f"TGA saved successfully: {tga_path}")

            # Open the file
            os.startfile(tga_path)

            # Close the document
            doc.close()

    except Exception as e:
        logger.error(f"Failed to save TGA: {e!s}")
        raise

def save_as_tga_advanced():
    """Save document as TGA with advanced settings."""
    try:
        with Session(action="new_document") as ps:
            # Create test document with larger dimensions
            doc = create_sample_document(ps, "TGATestAdvanced", 1000, 1000)

            # Advanced TGA options
            options = ps.TargaSaveOptions()
            options.alphaChannels = True  # Include alpha channels
            options.resolution = 32  # 32-bit depth
            options.rleCompression = True  # Use RLE compression

            # Save the file
            tga_path = os.path.join(mkdtemp("photoshop-python-api"), "test_advanced.tga")
            doc.saveAs(tga_path, options, asCopy=True)
            logger.info(f"TGA saved successfully with advanced options: {tga_path}")

            # Open the file
            os.startfile(tga_path)

            # Close the document
            doc.close()

    except Exception as e:
        logger.error(f"Failed to save TGA with advanced options: {e!s}")
        raise

if __name__ == "__main__":
    try:
        logger.info("Starting TGA export test...")
        
        # Test simple TGA export
        save_as_tga_simple()
        
        # Test advanced TGA export
        save_as_tga_advanced()
        
        logger.info("TGA export test completed successfully")
        
    except Exception as e:
        logger.error(f"TGA export test failed: {e!s}")
        raise
