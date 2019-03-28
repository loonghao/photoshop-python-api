# Import local modules
from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api._core import Photoshop


class CMYKColor(BasicOption, Photoshop):
    object_name = 'CMYKColor'

    def __init__(self, app):
        super(CMYKColor, self).__init__()
        if app:
            self.app = app

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
