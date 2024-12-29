"""Example script demonstrating how to duplicate Photoshop documents.

This script shows how to:
1. Create a sample document with content
2. Duplicate the document with different options
3. Modify the duplicate document
4. Handle document duplication errors
"""

# Import built-in modules
from __future__ import annotations

import logging
import os
from tempfile import mkdtemp
from typing import Any, Optional, Tuple

# Import local modules
from photoshop import Session
import photoshop.api as ps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_sample_document(
    ps_session: Any,
    name: str = "OriginalDocument",
    width: int = 800,
    height: int = 600,
) -> Any:
    """Create a sample document with some content.

    Args:
        ps_session: Active Photoshop session.
        name: Name for the new document.
        width: Width of the document in pixels.
        height: Height of the document in pixels.

    Returns:
        Document object if successful, None otherwise.
    """
    try:
        # Create new document
        doc = ps_session.app.documents.add(
            width=width,
            height=height,
            resolution=300,
            name=name,
        )

        # Add a text layer
        text_layer = doc.artLayers.add()
        text_layer.kind = ps.LayerKind.TextLayer
        text_layer.textItem.contents = "Original Document"
        text_layer.textItem.position = [50, 50]
        text_layer.textItem.size = 36

        # Add a solid color layer
        color_layer = doc.artLayers.add()
        color_layer.name = "Background Color"
        
        # Create and fill selection
        doc.selection.select([
            [100, 100],
            [300, 100],
            [300, 300],
            [100, 300],
        ])
        
        # Create a pink fill color
        fill_color = ps.SolidColor()
        fill_color.rgb.red = 255
        fill_color.rgb.green = 200
        fill_color.rgb.blue = 200
        
        # Fill selection and deselect
        doc.selection.fill(fill_color)
        doc.selection.deselect()

        logger.info("Created sample document: %s", name)
        return doc

    except Exception as e:
        logger.error("Failed to create sample document: %s", str(e))
        return None


def duplicate_document(
    doc: Any,
    new_name: Optional[str] = None,
    merge_layers: bool = False,
) -> Any:
    """Duplicate a document with options.

    Args:
        doc: Document to duplicate.
        new_name: Name for the duplicate document.
        merge_layers: Whether to merge layers in the duplicate.

    Returns:
        Duplicated document object if successful, None otherwise.
    """
    try:
        # Generate new name if not provided
        if not new_name:
            new_name = f"{doc.name}_copy"

        # Duplicate document
        duplicate = doc.duplicate(new_name)
        logger.info("Duplicated document '%s' as '%s'", doc.name, new_name)

        # Merge layers if requested
        if merge_layers and len(duplicate.layers) > 1:
            duplicate.mergeVisibleLayers()
            logger.info("Merged visible layers in duplicate document")

        return duplicate

    except Exception as e:
        logger.error("Failed to duplicate document: %s", str(e))
        return None


def modify_duplicate(doc: Any) -> None:
    """Make some modifications to the duplicated document.

    Args:
        doc: Document to modify.
    """
    try:
        # Add a new text layer
        text_layer = doc.artLayers.add()
        text_layer.kind = ps.LayerKind.TextLayer
        text_layer.textItem.contents = "Duplicate Document"
        text_layer.textItem.position = [50, 150]
        text_layer.textItem.size = 36

        # Add a solid color layer
        color_layer = doc.artLayers.add()
        color_layer.name = "Additional Color"

        # Create and fill new selection
        doc.selection.select([
            [400, 100],
            [600, 100],
            [600, 300],
            [400, 300],
        ])
        
        # Create a light green fill color
        fill_color = ps.SolidColor()
        fill_color.rgb.red = 200
        fill_color.rgb.green = 255
        fill_color.rgb.blue = 200
        
        # Fill selection and deselect
        doc.selection.fill(fill_color)
        doc.selection.deselect()

        logger.info("Modified duplicate document")

    except Exception as e:
        logger.error("Failed to modify duplicate document: %s", str(e))


def save_documents(original: Any, duplicate: Any) -> Tuple[str, str]:
    """Save both original and duplicate documents.

    Args:
        original: Original document object.
        duplicate: Duplicate document object.

    Returns:
        Tuple of (original_path, duplicate_path).
    """
    try:
        # Create temp directory for saving
        temp_dir = mkdtemp()
        
        # Create PSD save options
        save_options = ps.PhotoshopSaveOptions()
        save_options.alphaChannels = True
        save_options.layers = True
        save_options.spotColors = True
        save_options.embedColorProfile = True
        
        # Save original
        original_path = os.path.join(temp_dir, f"{original.name}.psd")
        original.saveAs(original_path, save_options, asCopy=True)
        logger.info("Saved original document: %s", original_path)

        # Save duplicate
        duplicate_path = os.path.join(temp_dir, f"{duplicate.name}.psd")
        duplicate.saveAs(duplicate_path, save_options, asCopy=True)
        logger.info("Saved duplicate document: %s", duplicate_path)

        return original_path, duplicate_path

    except Exception as e:
        logger.error("Failed to save documents: %s", str(e))
        return "", ""


def main() -> None:
    """Main function demonstrating document duplication."""
    try:
        with Session(action="new_document") as ps:
            # Create original document
            original = create_sample_document(ps)
            if not original:
                return

            # Duplicate document
            duplicate = duplicate_document(
                original,
                new_name="DuplicateDocument",
                merge_layers=False,
            )
            if not duplicate:
                return

            # Modify duplicate
            modify_duplicate(duplicate)

            # Save both documents
            orig_path, dup_path = save_documents(original, duplicate)

            # Show results
            if orig_path and dup_path:
                ps.echo(f"Original document: {original.name}")
                ps.echo(f"Duplicate document: {duplicate.name}")
                ps.alert("Documents saved successfully. Check the console for paths.")
            else:
                ps.alert("Failed to save documents. Check the console for errors.")

    except Exception as e:
        logger.error("Session failed: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting document duplication example...")
        main()
        logger.info("Document duplication example completed successfully")
    except Exception as e:
        logger.error("Document duplication example failed: %s", str(e))
        raise
