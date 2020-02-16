from photoshop_python_api._core import Photoshop


class HSBColor(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def brightness(self):
        return self.app.brightness

    @brightness.setter
    def brightness(self, value):
        self.app.brightness = value

    @property
    def saturation(self):
        return self.app.saturation

    @saturation.setter
    def saturation(self, value):
        self.app.saturation = value

    @property
    def hue(self):
        """The hue value. Range: 0.0 to 360.0."""
        return self.app.hue

    @hue.setter
    def hue(self, value):
        self.app.hue = value
