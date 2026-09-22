"""Options for saving a document in BMO format."""

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import BMPDepthType
from photoshop.api.enumerations import OperatingSystem


class BMPSaveOptions(Photoshop):
    """Options for saving a document in BMP format."""

    object_name = "BMPSaveOptions"

    def __init__(self) -> None:
        super().__init__()

    @property
    def alphaChannels(self) -> bool:
        """State to save the alpha channels."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value: bool) -> None:
        """Sets whether to save the alpha channels or not.

        Args:

        """
        self.app.alphaChannels = value

    @property
    def depth(self) -> BMPDepthType:
        return BMPDepthType(self.app.depth)

    @depth.setter
    def depth(self, value: BMPDepthType) -> None:
        self.app.depth = value

    @property
    def flipRowOrder(self) -> bool:
        return self.app.flipRowOrder

    @flipRowOrder.setter
    def flipRowOrder(self, value: bool) -> None:
        self.app.flipRowOrder = value

    @property
    def osType(self) -> OperatingSystem:
        return OperatingSystem(self.app.osType)

    @osType.setter
    def osType(self, value: OperatingSystem) -> None:
        self.app.osType = value

    @property
    def rleCompression(self) -> bool:
        return self.app.rleCompression

    @rleCompression.setter
    def rleCompression(self, value: bool) -> None:
        self.app.rleCompression = value
