# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import FormatOptionsType, MatteType


class JPEGSaveOptions(Photoshop):
    """Options for saving a document in JPEG format."""

    object_name = "JPEGSaveOptions"

    def __init__(
        self,
        quality: int = 5,
        embedColorProfile: bool = True,
        matte: MatteType = MatteType.NoMatte,
    ):
        super().__init__()
        self.quality = quality
        self.embedColorProfile = embedColorProfile
        self.matte = matte

    @property
    def quality(self) -> int:
        return self.app.quality

    @quality.setter
    def quality(self, value: int) -> None:
        self.app.quality = value

    @property
    def formatOptions(self) -> FormatOptionsType:
        """The download format to use."""
        return FormatOptionsType(self.app.formatOptions)

    @formatOptions.setter
    def formatOptions(self, value: FormatOptionsType) -> None:
        self.app.formatOptions = value

    @property
    def embedColorProfile(self) -> bool:
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value: bool) -> None:
        self.app.embedColorProfile = value

    @property
    def matte(self) -> MatteType:
        """The color to use to fill anti-aliased edges adjacent to
        transparent"""
        return MatteType(self.app.matte)

    @matte.setter
    def matte(self, value: MatteType) -> None:
        self.app.matte = value

    @property
    def scans(self) -> int:
        return self.app.scans

    @scans.setter
    def scans(self, value: int) -> None:
        self.app.scans = value
