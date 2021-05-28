# Import local modules
from photoshop.api._core import Photoshop


class EPSSaveOptions(Photoshop):
    """Options for saving a document in EPS format.

    using the `Document.saveAs()`

    """

    object_name = "EPSSaveOptions"

    def __init__(self):
        super().__init__()

    @property
    def embedColorProfile(self) -> bool:
        """True to embed the color profile in this document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, boolean: bool):
        """True to embed the color profile in this document."""
        self.app.embedColorProfile = boolean

    @property
    def encoding(self):
        return self.app.encoding

    @encoding.setter
    def encoding(self, value: bool):
        self.app.encoding = value

    @property
    def halftoneScreen(self):
        return self.app.halftoneScreen

    @halftoneScreen.setter
    def halftoneScreen(self, value: bool):
        self.app.halftoneScreen = value

    @property
    def interpolation(self):
        return self.app.interpolation

    @interpolation.setter
    def interpolation(self, value: bool):
        self.app.interpolation = value

    @property
    def preview(self):
        return self.app.preview

    @preview.setter
    def preview(self, value: bool):
        self.app.preview = value

    @property
    def psColorManagement(self):
        return self.app.psColorManagement

    @psColorManagement.setter
    def psColorManagement(self, value: bool):
        self.app.psColorManagement = value

    @property
    def transferFunction(self):
        return self.app.transferFunction

    @transferFunction.setter
    def transferFunction(self, value: bool):
        self.app.transferFunction = value

    @property
    def transparentWhites(self) -> bool:
        """True to display white areas as transparent"""
        return self.app.transparentWhites

    @transparentWhites.setter
    def transparentWhites(self, value: bool):
        """True to display white areas as transparent"""
        self.app.transparentWhites = value

    @property
    def vectorData(self):
        """True to include vector data."""
        return self.app.vectorData

    @vectorData.setter
    def vectorData(self, value: bool):
        """True to include vector data.

        Valid only if the document includes vector data (text).

        """
        self.app.vectorData = value
