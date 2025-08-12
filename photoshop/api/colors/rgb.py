# Import local modules
from photoshop.api._core import Photoshop


class RGBColor(Photoshop):
    """The definition of an RGB color mode."""

    object_name = "RGBColor"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self.blue = self.app.blue
        self.green = self.app.green
        self.red = self.app.red

    @property
    def blue(self) -> float:
        return self.app.blue

    @blue.setter
    def blue(self, value: float) -> None:
        self.app.blue = value

    @property
    def green(self) -> float:
        return self.app.green

    @green.setter
    def green(self, value: float) -> None:
        self.app.green = value

    @property
    def red(self) -> float:
        return self.app.red

    @red.setter
    def red(self, value: float) -> None:
        self.app.red = value

    @property
    def hexValue(self) -> str:
        return self.app.hexValue

    @hexValue.setter
    def hexValue(self, value: str) -> None:
        self.app.hexValue = value

    def __str__(self) -> str:
        return f"[red: {self.red}, green:{self.green},  blue:{self.blue})]"
