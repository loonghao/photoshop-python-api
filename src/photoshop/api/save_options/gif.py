# Import local modules
from photoshop.api._core import Photoshop


class GIFSaveOptions(Photoshop):
    object_name = "GIFSaveOptions"

    def __init__(self):
        super().__init__()

    @property
    def colors(self):
        return self.app.color

    @colors.setter
    def colors(self, value):
        self.app.colors = value

    @property
    def dither(self):
        return self.app.dither

    @dither.setter
    def dither(self, value):
        self.app.dither = value

    @property
    def ditherAmount(self):
        return self.app.ditherAmount

    @ditherAmount.setter
    def ditherAmount(self, value):
        self.app.ditherAmount = value

    @property
    def forced(self):
        return self.app.forced

    @forced.setter
    def forced(self, value):
        self.app.forced = value

    @property
    def interlaced(self):
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value):
        self.app.interlaced = value

    @property
    def matte(self):
        return self.app.matte

    @matte.setter
    def matte(self, value):
        self.app.matte = value

    @property
    def palette(self):
        return self.app.palette

    @palette.setter
    def palette(self, value):
        self.app.palette = value

    @property
    def preserveExactColors(self):
        return self.app.preserveExactColors

    @preserveExactColors.setter
    def preserveExactColors(self, value):
        self.app.preserveExactColors = value

    @property
    def transparency(self):
        return self.app.transparency

    @transparency.setter
    def transparency(self, value):
        self.app.transparency = value
