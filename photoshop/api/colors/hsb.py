"""Defines an HSB color, used in the `SolidColor` object."""

# Import local modules
from photoshop.api._core import Photoshop


class HSBColor(Photoshop):
    """An HSB color specification."""

    object_name = "HSBColor"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def brightness(self):
        return round(self.app.brightness)

    @brightness.setter
    def brightness(self, value):
        self.app.brightness = value

    @property
    def saturation(self):
        return round(self.app.saturation)

    @saturation.setter
    def saturation(self, value):
        self.app.saturation = value

    @property
    def hue(self):
        """The hue value. Range: 0.0 to 360.0."""
        return round(self.app.hue)

    @hue.setter
    def hue(self, value):
        self.app.hue = value
