"""Create a thumbnail image for currently active document.

You can use the thumbnail image to upload to Shotgun or Ftrack.

"""

# Import built-in modules
import os
from tempfile import mkdtemp

# Import local modules
from photoshop import Session


def create_thumbnail(output_path=None, max_resolution=512):
    """Create a thumbnail image for currently active document.

    Args:
        output_path (str): The absolute output path of the thumbnail image.
            The default is to output to a temporary folder.
        max_resolution (int): The max resolution of the thumbnail. The default
            is `512`.

    Returns:
        str: The absolute output path of the thumbnail image.

    """
    output_path = output_path or os.path.join(mkdtemp(prefix="thumb"), "thumb.jpg")

    with Session(auto_close=True) as ps:
        orig_name = ps.active_document.name
        width_str = ps.active_document.width
        height_str = ps.active_document.height
        thumb_name = f"{orig_name}_thumb"

        max_resolution = width_str / max_resolution
        thumb_width = int(width_str / max_resolution)
        thumb_height = int(height_str / max_resolution)

        thumb_doc = ps.active_document.duplicate(thumb_name)
        thumb_doc.resizeImage(thumb_width, thumb_height - 100)
        thumb_doc.saveAs(output_path, ps.JPEGSaveOptions(), asCopy=True)
        thumb_doc.close()
        return output_path


if __name__ == "__main__":
    thumb_file = create_thumbnail()
    print(f"Save thumbnail file to {thumb_file}.")
