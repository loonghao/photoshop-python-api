# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import MatteType


class JPEGSaveOptions(Photoshop):
    object_name = "JPEGSaveOptions"

    def __init__(self, quality=5, embedColorProfile=True, matte=MatteType.NoMatte):
        super().__init__()
        self.quality = quality
        self.embedColorProfile = embedColorProfile
        self.matte = matte

    @property
    def quality(self):
        return self.app.quality

    @quality.setter
    def quality(self, value):
        self.app.quality = value

    @property
    def formatOptions(self):
        """The download format to use."""
        return self.app.formatOptions

    @formatOptions.setter
    def formatOptions(self, value):
        self.app.formatOptions = value

    @property
    def embedColorProfile(self):
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value):
        self.app.embedColorProfile = value

    @property
    def matte(self):
        """The color to use to fill anti-aliased edges adjacent to
        transparent"""
        return self.app.matte

    @matte.setter
    def matte(self, value):
        self.app.matte = value

    @property
    def scans(self):
        return self.app.scans

    @scans.setter
    def scans(self, value):
        self.app.scans = value
