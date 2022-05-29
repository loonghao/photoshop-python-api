# Import local modules
from photoshop.api._core import Photoshop


class ExportOptionsSaveForWeb(Photoshop):
    """Options for exporting Save For Web files."""

    object_name = "ExportOptionsSaveForWeb"

    def __init__(self):
        super().__init__()
        self.format = 13  # PNG
        self.PNG8 = False  # Sets it to PNG-24 bit

    @property
    def PNG8(self):
        """If true, uses 8 bits. If false, uses 24 bits. Valid only when ‘format’ = PNG."""
        return self.app.PNG8

    @PNG8.setter
    def PNG8(self, value: bool):
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

    @property
    def quality(self):
        return self.app.quality

    @quality.setter
    def quality(self, value: int):
        self.app.quality = value


class PNGSaveOptions(Photoshop):
    object_name = "PNGSaveOptions"

    def __init__(self):
        super().__init__()
        self.interlaced = False
        self.compression = 6

    @property
    def interlaced(self) -> bool:
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value: bool):
        self.app.interlaced = value

    @property
    def compression(self) -> int:
        return self.app.compression

    @compression.setter
    def compression(self, value: int):
        self.app.compression = value
