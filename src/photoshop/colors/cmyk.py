# Import local modules
from photoshop._core import Photoshop


class CMYKColor(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.cyan = 75
        self.magenta = 68
        self.yellow = 67
        self.black = 90

    @property
    def black(self):
        """The black color value. Range: 0.0 to 100.0."""
        return self.app.black

    @black.setter
    def black(self, value):
        self.app.black = value

    @property
    def cyan(self):
        """The cyan color value. Range: 0.0 to 100.0."""
        return self.app.cyan

    @cyan.setter
    def cyan(self, value: int):
        self.app.cyan = value

    @property
    def magenta(self):
        """The magenta color value. Range: 0.0 to 100.0."""
        return self.app.magenta

    @magenta.setter
    def magenta(self, value: int):
        self.app.magenta = value

    @property
    def yellow(self):
        """The yellow color value. Range: 0.0 to 100.0."""
        return self.app.yellow

    @yellow.setter
    def yellow(self, value: float):
        self.app.yellow = value
