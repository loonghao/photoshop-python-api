"""Defines a CMYK color, used in the `SolidColor` object."""

# Import local modules

# Import local modules
from photoshop.api._core import Photoshop


class CMYKColor(Photoshop):
    object_name = "CMYKColor"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def black(self) -> int:
        """The black color value. Range: 0.0 to 100.0."""
        return round(self.app.black)

    @black.setter
    def black(self, value: int):
        self.app.black = value

    @property
    def cyan(self) -> int:
        """The cyan color value. Range: 0.0 to 100.0."""
        return round(self.app.cyan)

    @cyan.setter
    def cyan(self, value: int):
        self.app.cyan = value

    @property
    def magenta(self) -> int:
        """The magenta color value. Range: 0.0 to 100.0."""
        return round(self.app.magenta)

    @magenta.setter
    def magenta(self, value: int):
        self.app.magenta = value

    @property
    def yellow(self) -> int:
        """The yellow color value. Range: 0.0 to 100.0."""
        return round(self.app.yellow)

    @yellow.setter
    def yellow(self, value: int):
        self.app.yellow = value
