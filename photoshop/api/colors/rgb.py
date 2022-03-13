# Import local modules
from photoshop.api._core import Photoshop


class RGBColor(Photoshop):
    """The definition of an RGB color mode."""

    object_name = "RGBColor"

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.blue = self.app.blue
        self.green = self.app.green
        self.red = self.app.red

    @property
    def blue(self) -> int:
        return round(self.app.blue)

    @blue.setter
    def blue(self, value: int):
        self.app.blue = value

    @property
    def green(self) -> int:
        return round(self.app.green)

    @green.setter
    def green(self, value: int):
        self.app.green = value

    @property
    def red(self) -> int:
        return round(self.app.red)

    @red.setter
    def red(self, value: int):
        self.app.red = value

    @property
    def hexValue(self):
        return self.app.hexValue

    @hexValue.setter
    def hexValue(self, value):
        self.app.hexValue = value

    def __str__(self):
        return f"[red: {self.red}, green:{self.green},  blue:{self.blue})]"
