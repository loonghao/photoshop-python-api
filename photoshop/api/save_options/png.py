# Import local modules
from photoshop.api._core import Photoshop


class ExportOptionsSaveForWeb(Photoshop):
    object_name = "ExportOptionsSaveForWeb"

    def __init__(self):
        super().__init__()
        self.format = 13  # PNG
        self.PNG8 = False  # Sets it to PNG-24 bit

    @property
    def PNG8(self):
        return self.app.PNG8

    @PNG8.setter
    def PNG8(self, value):
        self.app.PNG8 = value

    @property
    def blur(self):
        return self.app.blur

    @blur.setter
    def blur(self, value):
        self.app.blur = value

    @property
    def colorReduction(self):
        return self.app.colorReduction

    @colorReduction.setter
    def colorReduction(self, value):
        self.app.colorReduction = value

    @property
    def colors(self):
        """The number of colors in the palette."""
        return self.app.colors

    @colors.setter
    def colors(self, value):
        """The number of colors in the palette."""
        self.app.colors = value

    @property
    def dither(self):
        return self.app.dither

    @dither.setter
    def dither(self, value):
        self.app.dither = value


class PNGSaveOptions(Photoshop):
    object_name = "PNGSaveOptions"

    def __init__(self):
        super().__init__()
        self.interlaced = False
        self.compression = True

    @property
    def interlaced(self):
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value):
        self.app.interlaced = value
