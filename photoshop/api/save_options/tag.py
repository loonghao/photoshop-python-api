# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import TargaBitsPerPixels


class TargaSaveOptions(Photoshop):
    """Options for saving a document in TGA (Targa) format."""

    object_name = "TargaSaveOptions"

    def __int__(self) -> None:
        super().__init__()

    @property
    def alphaChannels(self) -> bool:
        """If true, the alpha channels are saved."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value: bool) -> None:
        self.app.alphaChannels = value

    @property
    def resolution(self) -> TargaBitsPerPixels:
        return TargaBitsPerPixels(self.app.resolution)

    @resolution.setter
    def resolution(self, value: TargaBitsPerPixels) -> None:
        self.app.resolution = value

    @property
    def rleCompression(self) -> bool:
        return self.app.rleCompression

    @rleCompression.setter
    def rleCompression(self, value: bool) -> None:
        self.app.rleCompression = value
