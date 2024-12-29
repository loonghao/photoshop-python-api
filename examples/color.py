"""Example of working with colors in Photoshop.

This example demonstrates how to:
1. Create and modify solid colors
2. Work with different color models (RGB, CMYK, HSB)
3. Set foreground and background colors
4. Compare color values

Key concepts:
- Color models
- Color manipulation
- Color space conversion
- Color comparison
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Create a new RGB color
    rgb_color = ps.SolidColor()
    rgb_color.rgb.red = 255
    rgb_color.rgb.green = 0
    rgb_color.rgb.blue = 0
    
    # Create a new CMYK color
    cmyk_color = ps.SolidColor()
    cmyk_color.cmyk.cyan = 0
    cmyk_color.cmyk.magenta = 100
    cmyk_color.cmyk.yellow = 100
    cmyk_color.cmyk.black = 0
    
    # Set as foreground color
    ps.app.foregroundColor = rgb_color
    
    # Create HSB color
    hsb_color = ps.SolidColor()
    hsb_color.hsb.hue = 360
    hsb_color.hsb.saturation = 100
    hsb_color.hsb.brightness = 100
    
    # Set as background color
    ps.app.backgroundColor = hsb_color
