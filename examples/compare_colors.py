"""Example of comparing colors in Photoshop.

This example demonstrates how to:
1. Compare colors across different color models
2. Convert between color spaces
3. Check color equality
4. Work with color tolerances

Key concepts:
- Color comparison
- Color space conversion
- Color equality testing
- Color model differences
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Create two colors for comparison
    color1 = ps.SolidColor()
    color1.rgb.red = 255
    color1.rgb.green = 0
    color1.rgb.blue = 0
    
    color2 = ps.SolidColor()
    color2.rgb.red = 255
    color2.rgb.green = 0
    color2.rgb.blue = 0
    
    # Compare colors
    is_same = (color1.rgb.red == color2.rgb.red and
               color1.rgb.green == color2.rgb.green and
               color1.rgb.blue == color2.rgb.blue)
    
    ps.echo(f"Colors are {'same' if is_same else 'different'}")
