from photoshop._core import Photoshop


class RGBColor(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def blue(self):
        return self.app.blue

    @blue.setter
    def blue(self, value):
        self.app.blue = value

    @property
    def green(self):
        return self.app.green

    @green.setter
    def green(self, value):
        self.app.green = value

    @property
    def red(self):
        return self.app.red

    @red.setter
    def red(self, value):
        self.app.red = value

    @property
    def hexValue(self):
        return self.app.hexValue

    @hexValue.setter
    def hexValue(self, value):
        self.app.hexValue = value
