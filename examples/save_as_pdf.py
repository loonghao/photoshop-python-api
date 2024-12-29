"""Save current active document as a PDF file.

This script demonstrates different ways to save a Photoshop document as PDF,
including various PDF options and settings.
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

def save_as_pdf_simple():
    """Save document as PDF with basic settings."""
    try:
        with Session() as ps:
            # Create a simple document for testing
            doc = ps.app.documents.add(
                width=500,
                height=500,
                resolution=72,
                name="PDFTest",
            )

            # Add some content
            text_layer = doc.artLayers.add()
            text_layer.kind = LayerKind.TextLayer
            text_layer.textItem.contents = "Hello PDF!"
            text_layer.textItem.size = 72

            # Basic PDF options
            option = ps.PDFSaveOptions(
                jpegQuality=12,  # Highest quality
                layers=True,     # Preserve layers
                view=True,       # Open in PDF viewer after saving
            )
            
            # Save the file
            pdf_path = os.path.join(mkdtemp(), "test_simple.pdf")
            doc.saveAs(pdf_path, option)
            logger.info(f"PDF saved successfully: {pdf_path}")

            # Close the document
            doc.close()

    except Exception as e:
        logger.error(f"Failed to save PDF: {e!s}")
        raise

def save_as_pdf_advanced():
    """Save document as PDF with advanced settings."""
    try:
        with Session() as ps:
            # Create a test document
            doc = ps.app.documents.add(
                width=1000,
                height=1000,
                resolution=300,
                name="PDFTestAdvanced",
            )

            # Add some content
            text_layer = doc.artLayers.add()
            text_layer.kind = LayerKind.TextLayer
            text_layer.textItem.contents = "Advanced PDF Settings"
            text_layer.textItem.size = 72

            # Advanced PDF options
            option = ps.PDFSaveOptions()
            
            # Image quality settings
            option.jpegQuality = 12          # Highest quality
            
            # PDF structure settings
            option.layers = True             # Preserve layers
            option.preserveEditing = True    # Keep editing capabilities
            option.embedThumbnail = True     # Include thumbnail
            option.optimizeForWeb = True     # Optimize for web viewing
            option.view = True               # Open in PDF viewer after saving
            
            # Save the file
            pdf_path = os.path.join(mkdtemp(), "test_advanced.pdf")
            doc.saveAs(pdf_path, option)
            logger.info(f"PDF saved successfully with advanced options: {pdf_path}")

            # Close the document
            doc.close()

    except Exception as e:
        logger.error(f"Failed to save PDF with advanced options: {e!s}")
        raise

if __name__ == "__main__":
    try:
        logger.info("Starting PDF export test...")
        
        # Test simple PDF export
        save_as_pdf_simple()
        
        # Test advanced PDF export
        save_as_pdf_advanced()
        
        logger.info("PDF export test completed successfully")
        
    except Exception as e:
        logger.error(f"PDF export test failed: {e!s}")
        raise
