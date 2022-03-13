# Import local modules
from photoshop.api._core import Photoshop


class PhotoshopSaveOptions(Photoshop):
    """Options for saving a Photoshop document."""

    object_name = "PhotoshopSaveOptions"

    def __int__(self):
        super().__init__()

    @property
    def alphaChannels(self):
        """If true, the alpha channels are saved."""
        return self.app.alphaChannels()

    @alphaChannels.setter
    def alphaChannels(self, value):
        self.app.alphaChannels = value

    @property
    def annotations(self):
        """If true, the annotations are saved."""
        return self.app.annotations()

    @annotations.setter
    def annotations(self, value):
        self.app.annotations = value

    @property
    def embedColorProfile(self):
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile()

    @embedColorProfile.setter
    def embedColorProfile(self, value):
        self.app.embedColorProfile = value

    @property
    def layers(self):
        """If true, the layers are saved."""
        return self.app.layers()

    @layers.setter
    def layers(self, value):
        self.app.layers = value

    @property
    def spotColors(self):
        """If true, spot colors are saved."""
        return self.app.spotColors()

    @spotColors.setter
    def spotColors(self, value):
        self.app.spotColors = value
