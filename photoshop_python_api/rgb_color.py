from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api._core import Photoshop


class RGBColor(BasicOption, Photoshop):
    object_name = 'RGBColor'

    def __init__(self, app):
        super(RGBColor, self).__init__()
        if app:
            self.app = app

    @property
    def Blue(self):
        return self.app.Blue

    @Blue.setter
    def Blue(self, value):
        self.app.Blue = value

    @property
    def Green(self):
        return self.app.Green

    @Green.setter
    def Green(self, value):
        self.app.Green = value

    @property
    def Red(self):
        return self.app.Red

    @Red.setter
    def Red(self, value):
        self.app.Red = value

    @property
    def HexValue(self):
        return self.app.HexValue
