# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import DitherType
from photoshop.api.enumerations import ForcedColors
from photoshop.api.enumerations import MatteType
from photoshop.api.enumerations import PaletteType


class GIFSaveOptions(Photoshop):
    """Options for saving a document in GIF format."""

    object_name = "GIFSaveOptions"

    def __init__(self) -> None:
        super().__init__()

    @property
    def colors(self) -> int:
        return self.app.color

    @colors.setter
    def colors(self, value: int) -> None:
        self.app.colors = value

    @property
    def dither(self) -> DitherType:
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
    def forced(self) -> ForcedColors:
        return ForcedColors(self.app.forced)

    @forced.setter
    def forced(self, value: ForcedColors) -> None:
        self.app.forced = value

    @property
    def interlaced(self) -> bool:
        return self.app.interlaced

    @interlaced.setter
    def interlaced(self, value: bool) -> None:
        self.app.interlaced = value

    @property
    def matte(self) -> MatteType:
        return MatteType(self.app.matte)

    @matte.setter
    def matte(self, value: MatteType) -> None:
        self.app.matte = value

    @property
    def palette(self) -> PaletteType:
        return PaletteType(self.app.palette)

    @palette.setter
    def palette(self, value: PaletteType) -> None:
        self.app.palette = value

    @property
    def preserveExactColors(self) -> bool:
        return self.app.preserveExactColors

    @preserveExactColors.setter
    def preserveExactColors(self, value: bool) -> None:
        self.app.preserveExactColors = value

    @property
    def transparency(self) -> bool:
        return self.app.transparency

    @transparency.setter
    def transparency(self, value: bool) -> None:
        self.app.transparency = value
