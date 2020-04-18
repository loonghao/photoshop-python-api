"""Change the color of the background and foreground."""
from photoshop import Session

with Session() as ps:
    foregroundColor = ps.SolidColor()
    foregroundColor.rgb.red = 255
    foregroundColor.rgb.green = 0
    foregroundColor.rgb.blue = 0
    ps.app.foregroundColor = foregroundColor

    backgroundColor = ps.SolidColor()
    backgroundColor.rgb.red = 0
    backgroundColor.rgb.green = 0
    backgroundColor.rgb.blue = 0
    ps.app.backgroundColor = backgroundColor
