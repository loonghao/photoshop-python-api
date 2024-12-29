"""Create a thumbnail image for currently active document."""

# Import built-in modules
from __future__ import annotations
from pathlib import Path
from tempfile import mkdtemp
from typing import Optional

# Import local modules
from photoshop import Session


def create_thumbnail(output_path: Optional[str] = None, max_resolution: int = 512) -> str:
    """Create a thumbnail image for currently active document.

    Args:
        output_path: Output path for the thumbnail image.
        max_resolution: Maximum resolution for the thumbnail image.

    Returns:
        str: Path to the generated thumbnail image.
    """
    output_path = output_path or str(Path(mkdtemp()) / "thumb.jpg")

    with Session(auto_close=True) as ps:
        active_document = ps.active_document
        width = active_document.width
        height = active_document.height
        ratio = width / height

        if width > height:
            new_width = max_resolution
            new_height = max_resolution / ratio
        else:
            new_height = max_resolution
            new_width = max_resolution * ratio

        # Create new document
        new_doc = ps.app.documents.add(new_width, new_height)

        # Copy active document to new document
        active_document.activeLayer.copy()
        new_doc.paste()

        # Save as jpg
        options = ps.JPEGSaveOptions(quality=10)
        new_doc.saveAs(output_path, options, True)
        new_doc.close()

        return output_path


if __name__ == "__main__":
    thumb_file = create_thumbnail()
    print(f"Save thumbnail file to {thumb_file}.")
