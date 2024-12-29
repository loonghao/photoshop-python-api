"""Change the color of the background and foreground.

This example demonstrates how to:
1. Create SolidColor objects for foreground and background colors
2. Set RGB values for each color
3. Apply these colors to Photoshop's foreground and background
4. Print the current color values for verification
"""

# Import local modules
from __future__ import annotations

from photoshop import Session
from photoshop.api.enumerations import NewDocumentMode, DocumentFill

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB values to hex color code.
    
    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        
    Returns:
        Hex color code (e.g. '#FF0000' for red)
    """
    return f"#{r:02x}{g:02x}{b:02x}".upper()

def print_color_info(name: str, color) -> None:
    """Print color information in both RGB and HEX formats.
    
    Args:
        name: Name of the color (e.g. 'Foreground' or 'Background')
        color: SolidColor object containing RGB values
    """
    print(f"{name} Color:")
    print(f"  RGB: ({color.rgb.red}, {color.rgb.green}, {color.rgb.blue})")
    print(f"  HEX: {rgb_to_hex(color.rgb.red, color.rgb.green, color.rgb.blue)}")

with Session() as ps:
    # Create a new document to work with
    doc = ps.app.documents.add(
        width=800,
        height=600,
        resolution=72,
        name="Color Test",
        mode=NewDocumentMode.NewRGB,
        initialFill=DocumentFill.White,
    )
    
    # Set foreground color to red
    foregroundColor = ps.SolidColor()
    foregroundColor.rgb.red = 255    # Max red
    foregroundColor.rgb.green = 0    # No green
    foregroundColor.rgb.blue = 0     # No blue
    ps.app.foregroundColor = foregroundColor
    print_color_info("Foreground", foregroundColor)
    
    # Set background color to black
    backgroundColor = ps.SolidColor()
    backgroundColor.rgb.red = 0      # No red
    backgroundColor.rgb.green = 0    # No green
    backgroundColor.rgb.blue = 0     # No blue
    ps.app.backgroundColor = backgroundColor
    print_color_info("Background", backgroundColor)
    
    # Fill a selection with the foreground color to demonstrate the change
    doc.selection.selectAll()
    doc.selection.fill(foregroundColor)
    doc.selection.deselect()
    
    print("\nColors have been successfully updated in Photoshop!")
    print("A new document has been created and filled with the foreground color to demonstrate the change.")
