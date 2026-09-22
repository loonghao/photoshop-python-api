"""Example of creating and modifying selection strokes in Photoshop.

This example demonstrates how to:
1. Create selections with specific shapes
2. Apply strokes to selections
3. Configure stroke options
4. Work with stroke colors and widths

Key concepts:
- Selection creation
- Stroke application
- Stroke customization
- Color management
"""

# Import built-in modules
import math

# Import local modules
from photoshop import Session


def ellipse_region(left, top, width, height, segments=32):
    """Build a polygon that approximates the ellipse inscribed in the given box.

    Photoshop's Selection object has no ``selectElliptical`` method, so curved
    selections are described as a polygon of points passed to ``select()``.

    Args:
        left: Left edge of the bounding box.
        top: Top edge of the bounding box.
        width: Width of the bounding box.
        height: Height of the bounding box.
        segments: Number of points used to approximate the ellipse.

    Returns:
        list: ``[x, y]`` pairs describing the region.

    """
    center_x = left + width / 2
    center_y = top + height / 2
    radius_x = width / 2
    radius_y = height / 2
    return [
        [
            int(round(center_x + radius_x * math.cos(2 * math.pi * index / segments))),
            int(round(center_y + radius_y * math.sin(2 * math.pi * index / segments))),
        ]
        for index in range(segments)
    ]


with Session() as ps:
    doc = ps.active_document

    # Create a rectangular selection
    doc.selection.select([
        [100, 100],
        [400, 100],
        [400, 300],
        [100, 300]
    ])

    # Create stroke color
    stroke_color = ps.SolidColor()
    stroke_color.rgb.red = 255
    stroke_color.rgb.green = 0
    stroke_color.rgb.blue = 0

    # Apply stroke to selection
    doc.selection.stroke(
        stroke_color,  # Color to use
        width=2,      # Stroke width in pixels
        location=ps.StrokeLocation.InsideStroke,
        mode=ps.ColorBlendMode.NormalBlendColor,
        opacity=100,
        preserveTransparency=False,
    )

    # Create circular selection
    doc.selection.select(ellipse_region(
        left=200,
        top=200,
        width=200,
        height=200,
    ))

    # Change stroke color
    stroke_color.rgb.blue = 255

    # Apply different stroke
    doc.selection.stroke(
        stroke_color,
        width=5,
        location=ps.StrokeLocation.CenterStroke,
        mode=ps.ColorBlendMode.NormalBlendColor,
        opacity=75,
        preserveTransparency=True,
    )

    # Clear selection
    doc.selection.deselect()
