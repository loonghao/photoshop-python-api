"""Change the color of the background and foreground."""
from photoshop import Session

with Session() as ps:
    foregroundColor = ps.SolidColor()
    foregroundColor.rgb.red = 255
    ps.app.foregroundColor = foregroundColor

    backgroundColor = ps.SolidColor()
    backgroundColor.rgb.green = 255
    ps.app.backgroundColor = backgroundColor
