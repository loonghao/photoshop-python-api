"""Compare colors in Photoshop.

This example demonstrates how to:
1. Get and set foreground and background colors
2. Compare colors using isEqual method
3. Print color information in RGB and HEX formats
4. Create a color palette demonstration
5. Work with different color models (RGB, HSB)

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/CompareColors.py
"""

# Import local modules
from __future__ import annotations
from typing import Tuple, Dict
import math

from photoshop import Session
from photoshop.api.enumerations import NewDocumentMode, DocumentFill, LayerKind

# Define some common colors with their names
COLORS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Magenta": (255, 0, 255),
    "Cyan": (0, 255, 255),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
    "Pink": (255, 192, 203),
    "Turquoise": (64, 224, 208),
}

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

def rgb_to_hsb(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """Convert RGB to HSB/HSV.
    
    Args:
        r: Red value (0-255)
        g: Green value (0-255)
        b: Blue value (0-255)
        
    Returns:
        Tuple of (Hue, Saturation, Brightness)
    """
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax - cmin

    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    else:
        h = (60 * ((r - g) / diff) + 240) % 360

    s = 0 if cmax == 0 else (diff / cmax) * 100
    v = cmax * 100
    return h, s, v

def print_color_info(name: str, color) -> None:
    """Print color information in RGB, HEX and HSB formats.
    
    Args:
        name: Name of the color
        color: SolidColor object containing RGB values
    """
    rgb = (color.rgb.red, color.rgb.green, color.rgb.blue)
    hsb = rgb_to_hsb(*rgb)
    print(f"{name} Color:")
    print(f"  RGB: {rgb}")
    print(f"  HEX: {rgb_to_hex(*rgb)}")
    print(f"  HSB: H:{hsb[0]:.1f}° S:{hsb[1]:.1f}% B:{hsb[2]:.1f}%")

def create_color_grid(doc, colors: Dict[str, Tuple[int, int, int]], ps) -> None:
    """Create a grid of color squares with labels.
    
    Args:
        doc: Photoshop document
        colors: Dictionary of color names and their RGB values
        ps: Photoshop session
    """
    num_colors = len(colors)
    cols = 5  # Number of columns in the grid
    rows = math.ceil(num_colors / cols)
    
    square_size = 100
    margin = 20
    text_height = 30
    
    # Calculate total dimensions
    total_width = cols * (square_size + margin) - margin
    total_height = rows * (square_size + text_height + margin) - margin
    
    # Resize document to fit the grid
    doc.resizeImage(width=total_width, height=total_height)
    
    for i, (name, (r, g, b)) in enumerate(colors.items()):
        row = i // cols
        col = i % cols
        
        # Calculate position
        x = col * (square_size + margin)
        y = row * (square_size + text_height + margin)
        
        # Create color square layer
        square_layer = doc.artLayers.add()
        square_layer.name = f"{name} Square"
        
        # Fill with color
        color = ps.SolidColor()
        color.rgb.red = r
        color.rgb.green = g
        color.rgb.blue = b
        
        # Select area for color square
        doc.selection.select([
            [x, y],
            [x + square_size, y],
            [x + square_size, y + square_size],
            [x, y + square_size],
        ])
        
        # Set foreground color and fill
        ps.app.foregroundColor = color
        doc.selection.fill(ps.app.foregroundColor)
        doc.selection.deselect()
        
        # Add text label
        text_layer = doc.artLayers.add()
        text_layer.kind = LayerKind.TextLayer
        text_layer.name = f"{name} Label"
        text_layer.textItem.contents = f"{name}\n{rgb_to_hex(r, g, b)}"
        text_layer.textItem.position = [x, y + square_size + 5]
        text_layer.textItem.size = 12
        text_layer.textItem.font = "Microsoft YaHei"
        
        # Set text color (black or white depending on background)
        text_color = ps.SolidColor()
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        if brightness < 128:
            text_color.rgb.red = text_color.rgb.green = text_color.rgb.blue = 255
        else:
            text_color.rgb.red = text_color.rgb.green = text_color.rgb.blue = 0
        text_layer.textItem.color = text_color

def main() -> None:
    """Run the example script."""
    with Session() as ps:
        # Create a new document
        doc = ps.app.documents.add(
            width=800,
            height=600,
            resolution=72,
            name="Color Palette Demo",
            mode=NewDocumentMode.NewRGB,
            initialFill=DocumentFill.White,
        )
        
        # Create color grid
        create_color_grid(doc, COLORS, ps)
        
        # Print color information
        print("Color Palette Information:")
        print("-" * 50)
        for name, (r, g, b) in COLORS.items():
            color = ps.SolidColor()
            color.rgb.red = r
            color.rgb.green = g
            color.rgb.blue = b
            print_color_info(name, color)
            print()
        
        print("\nA color palette has been created in Photoshop!")
        print(f"The palette contains {len(COLORS)} different colors with their RGB, HEX, and HSB values.")
        print("Each color is displayed as a square with its name and HEX code.")

if __name__ == "__main__":
    main()
