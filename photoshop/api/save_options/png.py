# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ColorReductionType
from photoshop.api.enumerations import DitherType
from photoshop.api.enumerations import SaveDocumentType


class ExportOptionsSaveForWeb(Photoshop):
    """Options for exporting Save For Web files."""

    object_name = "ExportOptionsSaveForWeb"

    def __init__(self):
        super().__init__()
        self._format = SaveDocumentType.PNGSave  # Default to PNG
        self.PNG8 = False  # Sets it to PNG-24 bit

    @property
    def format(self) -> SaveDocumentType:
        """The file format to use. One of the SaveDocumentType constants."""
        return self._format

    @format.setter
    def format(self, value: SaveDocumentType):
        """Set the file format to use."""
        self._format = value

    @property
    def PNG8(self) -> bool:
        """If true, uses 8 bits. If false, uses 24 bits. Valid only when 'format' = PNG."""
        return self.app.PNG8

    @PNG8.setter
    def PNG8(self, value: bool):
        self.app.PNG8 = value

    @property
    def blur(self) -> float:
        """Applies blur to the image to reduce artifacts."""
        return self.app.blur

    @blur.setter
    def blur(self, value: float):
        self.app.blur = value

    @property
    def colorReduction(self) -> ColorReductionType:
        """The color reduction algorithm."""
        return self.app.colorReduction

    @colorReduction.setter
    def colorReduction(self, value: ColorReductionType):
        self.app.colorReduction = value

    @property
    def colors(self) -> int:
        """The number of colors in the palette."""
        return self.app.colors

    @colors.setter
    def colors(self, value: int):
        self.app.colors = value

    @property
    def dither(self) -> DitherType:
        """The type of dither to use."""
        return self.app.dither

    @dither.setter
    def dither(self, value: DitherType):
        self.app.dither = value

    @property
    def optimized(self) -> bool:
        """If true, optimization is enabled."""
        return self.app.optimized

    @optimized.setter
    def optimized(self, value: bool):
        self.app.optimized = value

    @property
    def quality(self) -> int:
        """The quality of the output image, from 0 to 100."""
        return self.app.quality

    @quality.setter
    def quality(self, value: int):
        self.app.quality = value


class PNGSaveOptions(Photoshop):
    """Options for saving file as PNG."""

    object_name = "PNGSaveOptions"

    def __init__(self, interlaced: bool = False, compression: int = 6):
        super().__init__()
        self.interlaced = interlaced
        self.compression = compression

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
