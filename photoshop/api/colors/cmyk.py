"""Defines a CMYK color, used in the `SolidColor` object."""

# Import local modules
from photoshop.api._core import Photoshop


class CMYKColor(Photoshop):
    """A CMYK color specification."""

    object_name = "CMYKColor"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def black(self) -> float:
        """The black color value. Range: 0.0 to 100.0."""
        return self.app.black

    @black.setter
    def black(self, value: float) -> None:
        self.app.black = value

    @property
    def cyan(self) -> float:
        """The cyan color value. Range: 0.0 to 100.0."""
        return self.app.cyan

    @cyan.setter
    def cyan(self, value: float) -> None:
        self.app.cyan = value

    @property
    def magenta(self) -> float:
        """The magenta color value. Range: 0.0 to 100.0."""
        return self.app.magenta

    @magenta.setter
    def magenta(self, value: float) -> None:
        self.app.magenta = value

    @property
    def yellow(self) -> float:
        """The yellow color value. Range: 0.0 to 100.0."""
        return self.app.yellow

    @yellow.setter
    def yellow(self, value: float) -> None:
        self.app.yellow = value
