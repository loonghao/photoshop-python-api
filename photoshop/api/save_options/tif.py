# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import (
    ByteOrderType,
    LayerCompressionType,
    TiffEncodingType,
)


class TiffSaveOptions(Photoshop):
    """Options for saving a document in TIFF format."""

    object_name = "TiffSaveOptions"

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
    def annotations(self) -> bool:
        """If true, the annotations are saved."""
        return self.app.annotations

    @annotations.setter
    def annotations(self, value: bool) -> None:
        self.app.annotations = value

    @property
    def byteOrder(self) -> ByteOrderType:
        """The order in which the bytes will be read.
        Default:
        Mac OS when running in Mac OS, and IBM PC when running in Windows.
        """
        return ByteOrderType(self.app.byteOrder)

    @byteOrder.setter
    def byteOrder(self, value: ByteOrderType) -> None:
        self.app.byteOrder = value

    @property
    def embedColorProfile(self) -> bool:
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value: bool) -> None:
        self.app.embedColorProfile = value

    @property
    def imageCompression(self) -> TiffEncodingType:
        """The compression type."""
        return TiffEncodingType(self.app.imageCompression)

    @imageCompression.setter
    def imageCompression(self, value: TiffEncodingType) -> None:
        self.app.imageCompression = value

    @property
    def interleaveChannels(self) -> bool:
        """If true, the channels in the image are interleaved."""
        return self.app.interleaveChannels

    @interleaveChannels.setter
    def interleaveChannels(self, value: bool) -> None:
        self.app.interleaveChannels = value

    @property
    def jpegQuality(self) -> int:
        """The quality of the produced image, which is inversely proportionate
        to the amount of JPEG compression.
        Valid only for JPEG compressed TIFF documents. Range: 0 to 12.
        """
        return self.app.jpegQuality

    @jpegQuality.setter
    def jpegQuality(self, value: int) -> None:
        self.app.jpegQuality = value

    @property
    def layerCompression(self) -> LayerCompressionType:
        return LayerCompressionType(self.app.layerCompression)

    @layerCompression.setter
    def layerCompression(self, value: LayerCompressionType) -> None:
        """The method of compression to use when saving layers
        (as opposed to saving composite data).
        Valid only when `layers` = true.
        """
        self.app.layerCompression = value

    @property
    def layers(self) -> bool:
        """If true, the layers are saved."""
        return self.app.layers

    @layers.setter
    def layers(self, value: bool) -> None:
        self.app.layers = value

    @property
    def saveImagePyramid(self) -> bool:
        """If true, preserves multi-resolution information."""
        return self.app.saveImagePyramid

    @saveImagePyramid.setter
    def saveImagePyramid(self, value: bool) -> None:
        self.app.saveImagePyramid = value

    @property
    def spotColors(self) -> bool:
        """If true, spot colors are saved."""
        return self.app.spotColors

    @spotColors.setter
    def spotColors(self, value: bool) -> None:
        self.app.spotColors = value

    @property
    def transparency(self) -> bool:
        return self.app.transparency

    @transparency.setter
    def transparency(self, value: bool) -> None:
        """If true, saves the transparency as an additional alpha channel when
        the file is opened in another application."""
        self.app.transparency = value
