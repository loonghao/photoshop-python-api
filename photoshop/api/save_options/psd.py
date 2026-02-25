# Import local modules
from photoshop.api._core import Photoshop


class PhotoshopSaveOptions(Photoshop):
    """Options for saving a Photoshop document."""

    object_name = "PhotoshopSaveOptions"

    def __int__(self) -> None:
        super().__init__()

    @property
    def alphaChannels(self) -> bool:
        """If true, the alpha channels are saved."""
        return self.app.alphaChannels()

    @alphaChannels.setter
    def alphaChannels(self, value: bool) -> None:
        self.app.alphaChannels = value

    @property
    def annotations(self) -> bool:
        """If true, the annotations are saved."""
        return self.app.annotations()

    @annotations.setter
    def annotations(self, value: bool) -> None:
        self.app.annotations = value

    @property
    def embedColorProfile(self) -> bool:
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile()

    @embedColorProfile.setter
    def embedColorProfile(self, value: bool) -> None:
        self.app.embedColorProfile = value

    @property
    def layers(self) -> bool:
        """If true, the layers are saved."""
        return self.app.layers()

    @layers.setter
    def layers(self, value: bool) -> None:
        self.app.layers = value

    @property
    def spotColors(self) -> bool:
        """If true, spot colors are saved."""
        return self.app.spotColors()

    @spotColors.setter
    def spotColors(self, value: bool) -> None:
        self.app.spotColors = value
