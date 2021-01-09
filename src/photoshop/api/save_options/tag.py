# Import local modules
from .._core import Photoshop
from ..enumerations import TargaBitsPerPixels


class TargaSaveOptions(Photoshop):
    object_name = "TargaSaveOptions"

    def __int__(self):
        super().__init__()

    @property
    def alphaChannels(self):
        """If true, the alpha channels are saved."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value):
        self.app.alphaChannels = value

    @property
    def resolution(self):
        return self.app.resolution

    @resolution.setter
    def resolution(self, value: TargaBitsPerPixels = TargaBitsPerPixels.Targa24Bits):
        self.app.resolution = value

    @property
    def rleCompression(self):
        return self.app.rleCompression

    @rleCompression.setter
    def rleCompression(self, value):
        self.app.rleCompression = value
