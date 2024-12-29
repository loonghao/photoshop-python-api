"""Example script demonstrating how to save Photoshop documents as PSD files.

This script shows different methods for saving PSD files with various options:
1. Simple PSD saving with basic options
2. Advanced PSD saving with additional features like compatibility settings
"""

# Import built-in modules
from __future__ import annotations

import logging
import os
from tempfile import mkdtemp
from typing import Any

# Import local modules
from photoshop import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_sample_document(
    ps: Any,
    name: str = "PSDTest",
    width: int = 500,
    height: int = 500,
) -> Any:
    """Create a sample document.

    Args:
        ps: Photoshop session object.
        name: Name for the new document.
        width: Width of the document in pixels.
        height: Height of the document in pixels.

    Returns:
        Document: Created Photoshop document object.
    """
    # Create a new document with high resolution
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=300,
        name=name,
    )

    return doc


def save_as_psd_simple() -> None:
    """Save document as PSD with basic settings."""
    try:
        with Session() as ps:
            # Create test document
            doc = create_sample_document(ps)

            # Configure basic PSD options
            options = ps.PhotoshopSaveOptions()
            options.alphaChannels = True     # Save alpha channels
            options.layers = True            # Save layers
            options.spotColors = True        # Save spot colors
            options.embedColorProfile = True # Embed color profile

            # Save to temp directory
            psd_path = os.path.join(mkdtemp(), "test_simple.psd")
            doc.saveAs(psd_path, options, asCopy=True)
            logger.info("PSD saved successfully: %s", psd_path)

            # Open the file for preview
            os.startfile(psd_path)

            # Cleanup
            doc.close()

    except Exception as e:
        logger.error("Failed to save PSD: %s", str(e))
        raise


def save_as_psd_advanced() -> None:
    """Save document as PSD with advanced settings."""
    try:
        with Session() as ps:
            # Create test document with moderate size
            doc = create_sample_document(ps, "PSDTestAdvanced", 800, 800)

            # Configure advanced PSD options
            options = ps.PhotoshopSaveOptions()
            
            # Layer settings
            options.alphaChannels = True     # Save alpha channels
            options.layers = True            # Save layers
            options.spotColors = True        # Save spot colors
            options.embedColorProfile = True # Embed color profile
            options.annotations = True       # Save annotations
            
            # Compatibility settings
            options.maximizeCompatibility = True  # For better compatibility

            # Save to temp directory
            psd_path = os.path.join(mkdtemp(), "test_advanced.psd")
            doc.saveAs(psd_path, options, asCopy=True)
            logger.info("PSD saved successfully with advanced options: %s", psd_path)

            # Open the file for preview
            os.startfile(psd_path)

            # Cleanup
            doc.close()

    except Exception as e:
        logger.error("Failed to save PSD with advanced options: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting PSD export test...")
        
        # Test both PSD export methods
        save_as_psd_simple()
        save_as_psd_advanced()
        
        logger.info("PSD export test completed successfully")
        
    except Exception as e:
        logger.error("PSD export test failed: %s", str(e))
        raise
