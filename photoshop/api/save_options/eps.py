# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import PreviewType
from photoshop.api.enumerations import SaveEncoding


class EPSSaveOptions(Photoshop):
    """Options for saving a document in EPS format.

    using the `Document.saveAs()`

    """

    object_name = "EPSSaveOptions"

    def __init__(self) -> None:
        super().__init__()

    @property
    def embedColorProfile(self) -> bool:
        """True to embed the color profile in this document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, boolean: bool) -> None:
        """True to embed the color profile in this document."""
        self.app.embedColorProfile = boolean

    @property
    def encoding(self) -> SaveEncoding:
        return SaveEncoding(self.app.encoding)

    @encoding.setter
    def encoding(self, value: SaveEncoding) -> None:
        self.app.encoding = value

    @property
    def halftoneScreen(self) -> bool:
        return self.app.halftoneScreen

    @halftoneScreen.setter
    def halftoneScreen(self, value: bool) -> None:
        self.app.halftoneScreen = value

    @property
    def interpolation(self) -> bool:
        return self.app.interpolation

    @interpolation.setter
    def interpolation(self, value: bool) -> None:
        self.app.interpolation = value

    @property
    def preview(self) -> PreviewType:
        return PreviewType(self.app.preview)

    @preview.setter
    def preview(self, value: PreviewType) -> None:
        self.app.preview = value

    @property
    def psColorManagement(self) -> bool:
        return self.app.psColorManagement

    @psColorManagement.setter
    def psColorManagement(self, value: bool) -> None:
        self.app.psColorManagement = value

    @property
    def transferFunction(self) -> bool:
        return self.app.transferFunction

    @transferFunction.setter
    def transferFunction(self, value: bool) -> None:
        self.app.transferFunction = value

    @property
    def transparentWhites(self) -> bool:
        """True to display white areas as transparent"""
        return self.app.transparentWhites

    @transparentWhites.setter
    def transparentWhites(self, value: bool) -> None:
        """True to display white areas as transparent"""
        self.app.transparentWhites = value

    @property
    def vectorData(self) -> bool:
        """True to include vector data."""
        return self.app.vectorData

    @vectorData.setter
    def vectorData(self, value: bool) -> None:
        """True to include vector data.

        Valid only if the document includes vector data (text).

        """
        self.app.vectorData = value
