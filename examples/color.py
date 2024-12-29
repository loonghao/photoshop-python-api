"""Example of working with colors in Photoshop.

This script demonstrates how to:
1. Create a solid color
2. Set RGB values
3. Apply color to text layers
4. Verify color values

Module Attributes:
    None

Module Classes:
    None

Module Functions:
    main() -> None
"""


# Import local modules``
from __future__ import annotations
from photoshop import Session

def main() -> None:
    """Run the example script.

    This function creates a solid color, sets RGB values, applies the color to a text layer, 
    and verifies the color values.

    Returns:
        None
    """
    with Session() as ps:
        doc = ps.active_document
        # Add a solid color.
        text_color = ps.SolidColor()
        text_color.rgb.red = 255.0
        text_color.rgb.green = 197
        text_color.rgb.blue = 0

        # Create empty layer.
        new_text_layer = doc.artLayers.add()
        # Set empty layer type to text layer
        new_text_layer.kind = ps.LayerKind.TextLayer
        # Set current text layer contents to "Hello, World!".
        new_text_layer.textItem.contents = "Hello, World!"
        # Set font to Microsoft YaHei
        new_text_layer.textItem.font = "Microsoft YaHei"
        # Change current text layer position.
        new_text_layer.textItem.position = [160, 167]
        # Change current text layer text size.
        new_text_layer.textItem.size = 36
        # Change current text layer color.
        new_text_layer.textItem.color = text_color

        # Verify the color values
        if new_text_layer.textItem.color.rgb.red == text_color.rgb.red:
            ps.echo("Text color set successfully")
        else:
            ps.echo("Failed to set text color")

if __name__ == "__main__":
    main()
