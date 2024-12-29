"""Example of changing background and foreground colors in Photoshop.

This example demonstrates how to:
1. Set foreground and background colors
2. Work with color swatches
3. Switch between foreground and background colors
4. Reset colors to default values

Key concepts:
- Color management
- Foreground/background colors
- Color swatches
- Default colors
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Create new colors
    fg_color = ps.SolidColor()
    fg_color.rgb.red = 255
    fg_color.rgb.green = 0
    fg_color.rgb.blue = 0
    
    bg_color = ps.SolidColor()
    bg_color.rgb.red = 0
    bg_color.rgb.green = 0
    bg_color.rgb.blue = 255
    
    # Set foreground and background colors
    ps.app.foregroundColor = fg_color
    ps.app.backgroundColor = bg_color
    
    # Print current colors
    ps.echo(f"Foreground RGB: {ps.app.foregroundColor.rgb.red}, "
            f"{ps.app.foregroundColor.rgb.green}, "
            f"{ps.app.foregroundColor.rgb.blue}")
    
    ps.echo(f"Background RGB: {ps.app.backgroundColor.rgb.red}, "
            f"{ps.app.backgroundColor.rgb.green}, "
            f"{ps.app.backgroundColor.rgb.blue}")
