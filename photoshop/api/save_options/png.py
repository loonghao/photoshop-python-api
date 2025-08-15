# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.colors.rgb import RGBColor
from photoshop.api.enumerations import ColorReductionType
from photoshop.api.enumerations import DitherType
from photoshop.api.enumerations import SaveDocumentType


class ExportOptionsSaveForWeb(Photoshop):
    """Options for exporting Save For Web files."""

    object_name = "ExportOptionsSaveForWeb"

    def __init__(self) -> None:
        super().__init__()
        self.PNG8 = False  # Sets it to PNG-24 bit

    @property
    def format(self) -> SaveDocumentType:
        """The file format to use. One of the SaveDocumentType constants."""
        return SaveDocumentType(self.app.format)

    @format.setter
    def format(self, value: SaveDocumentType) -> None:
        """Set the file format to use."""
        self.app.format = value

    @property
    def PNG8(self) -> bool:
        """If true, uses 8 bits. If false, uses 24 bits. Valid only when 'format' = PNG."""
        return self.app.PNG8

    @PNG8.setter
    def PNG8(self, value: bool) -> None:
        self.app.PNG8 = value

    @property
    def blur(self) -> float:
        """Applies blur to the image to reduce artifacts."""
        return self.app.blur

    @blur.setter
    def blur(self, value: float) -> None:
        self.app.blur = value

    @property
    def colorReduction(self) -> ColorReductionType:
        """The color reduction algorithm."""
        return ColorReductionType(self.app.colorReduction)

    @colorReduction.setter
    def colorReduction(self, value: ColorReductionType) -> None:
        self.app.colorReduction = value

    @property
    def colors(self) -> int:
        """The number of colors in the palette."""
        return self.app.colors

    @colors.setter
    def colors(self, value: int) -> None:
        self.app.colors = value

    @property
    def dither(self) -> DitherType:
        """The type of dither to use."""
        return DitherType(self.app.dither)

    @dither.setter
    def dither(self, value: DitherType) -> None:
        self.app.dither = value

    @property
    def ditherAmount(self) -> int:
        return self.app.ditherAmount

    @ditherAmount.setter
    def ditherAmount(self, value: int) -> None:
        self.app.ditherAmount = value

    @property
    def includeProfile(self) -> bool:
        return self.app.includeProfile

    @includeProfile.setter
    def includeProfile(self, value: bool) -> None:
        self.app.includeProfile = value

    @property
    def interlaced(self) -> bool:
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value: bool) -> None:
        self.app.interlaced = value

    @property
    def lossy(self) -> int:
        return self.app.lossy

    @lossy.setter
    def lossy(self, value: int) -> None:
        self.app.lossy = value

    @property
    def matteColor(self) -> RGBColor:
        return self.app.matteColor

    @matteColor.setter
    def matteColor(self, value: RGBColor) -> None:
        self.app.matteColor = value

    @property
    def optimized(self) -> bool:
        """If true, optimization is enabled."""
        return self.app.optimized

    @optimized.setter
    def optimized(self, value: bool) -> None:
        self.app.optimized = value

    @property
    def quality(self) -> int:
        """The quality of the output image, from 0 to 100."""
        return self.app.quality

    @quality.setter
    def quality(self, value: int) -> None:
        self.app.quality = value

    @property
    def transparency(self) -> bool:
        return self.app.transparency

    @transparency.setter
    def transparency(self, value: bool) -> None:
        self.app.transparency = value

    @property
    def transparencyAmount(self) -> int:
        return self.app.transparencyAmount

    @transparencyAmount.setter
    def transparencyAmount(self, value: int) -> None:
        self.app.transparencyAmount = value

    @property
    def transparencyDither(self) -> DitherType:
        return DitherType(self.app.transparencyDither)

    @transparencyDither.setter
    def transparencyDither(self, value: DitherType) -> None:
        self.app.transparencyDither = value

    @property
    def webSnap(self) -> int:
        return self.app.webSnap

    @webSnap.setter
    def webSnap(self, value: int) -> None:
        self.app.webSnap = value


class PNGSaveOptions(Photoshop):
    """Options for saving file as PNG."""

    object_name = "PNGSaveOptions"

    def __init__(self, interlaced: bool = False, compression: int = 6) -> None:
        super().__init__()
        self.interlaced = interlaced
        self.compression = compression

    @property
    def interlaced(self) -> bool:
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value: bool) -> None:
        self.app.interlaced = value

    @property
    def compression(self) -> int:
        return self.app.compression

    @compression.setter
    def compression(self, value: int) -> None:
        self.app.compression = value
