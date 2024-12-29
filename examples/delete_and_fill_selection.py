"""This script demonstrates how to delete and fill a selection in one operation."""

# Import built-in modules
import os

# Import third-party modules
from photoshop import Session
from photoshop.api import SolidColor
import photoshop.api as ps

# Import local modules
from _psd_files import get_psd_files

def delete_and_fill_selection(doc, fill_type, mode=None, opacity=None, preserve_transparency=None):
    """Delete current selection and fill it with specified color.
    
    Args:
        doc: The active document.
        fill_type (SolidColor): The color to fill the selection with.
        mode (ColorBlendMode, optional): The color blend mode.
        opacity (int, optional): The opacity value.
        preserve_transparency (bool, optional): If true, preserves transparency.
    """
    # First fill the selection
    doc.selection.fill(fill_type, mode, opacity, preserve_transparency)
    # Then deselect
    doc.selection.deselect()

def main():
    """Create a selection and fill it with a solid color."""
    psd_file = get_psd_files()["export_layers_as_png.psd"]
    
    # Initialize Photoshop application
    app = ps.Application()
    
    # Open the test file
    if not os.path.exists(psd_file):
        raise FileNotFoundError(f"Test file not found: {psd_file}")
    app.load(psd_file)
    
    # Get the active document
    doc = app.activeDocument

    # Create a rectangular selection
    doc.selection.select(((100, 100), (400, 100), (400, 300), (100, 300)))

    # Create a solid color (red in this case)
    red_color = SolidColor()
    red_color.rgb.red = 255
    red_color.rgb.green = 0
    red_color.rgb.blue = 0

    # Delete and fill the selection
    delete_and_fill_selection(doc, red_color, opacity=80)

    # Save the changes
    doc.save()
    
    print("Selection has been filled with red color.")

if __name__ == "__main__":
    main()
