# Import local modules
from photoshop._core import Photoshop


class CMYKColor(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def Black(self):
        return self.app.Black

    @Black.setter
    def Black(self, value):
        self.app.Black = value

    @property
    def Cyan(self):
        return self.app.Cyan

    @Cyan.setter
    def Cyan(self, value):
        self.app.Cyan = value

    @property
    def magenta(self):
        return self.app.magenta

    @magenta.setter
    def magenta(self, value):
        self.app.magenta = value

    @property
    def Yellow(self):
        return self.app.HexValue

    @Yellow.setter
    def Yellow(self):
        return self.app.Yellow

    @Yellow.getter
    def Yellow(self):
        return self.app.Yellow
