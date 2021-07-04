# Import local modules
from photoshop.api._core import Photoshop


class TiffSaveOptions(Photoshop):
    object_name = "TiffSaveOptions"

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
    def annotations(self):
        """If true, the annotations are saved."""
        return self.app.annotations

    @annotations.setter
    def annotations(self, value):
        self.app.annotations = value

    @property
    def byteOrder(self):
        """The order in which the bytes will be read.
        Default:
        Mac OS when running in Mac OS, and IBM PC when running in Windows.
        """
        return self.app.byteOrder

    @byteOrder.setter
    def byteOrder(self, value):
        self.app.byteOrder = value

    @property
    def embedColorProfile(self):
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value):
        self.app.embedColorProfile = value

    @property
    def imageCompression(self):
        """The compression type."""
        return self.app.imageCompression

    @imageCompression.setter
    def imageCompression(self, value):
        self.app.imageCompression = value

    @property
    def interleaveChannels(self):
        """If true, the channels in the image are interleaved."""
        return self.app.interleaveChannels

    @interleaveChannels.setter
    def interleaveChannels(self, value):
        self.app.interleaveChannels = value

    @property
    def jpegQuality(self):
        """The quality of the produced image, which is inversely proportionate
        to the amount of JPEG compression.
        Valid only for JPEG compressed TIFF documents. Range: 0 to 12.
        """
        return self.app.jpegQuality

    @jpegQuality.setter
    def jpegQuality(self, value):
        self.app.jpegQuality = value

    @property
    def layerCompression(self):
        return self.app.layerCompression

    @layerCompression.setter
    def layerCompression(self, value):
        """The method of compression to use when saving layers
        (as opposed to saving composite data).
        Valid only when `layers` = true.
        """
        self.app.layerCompression = value

    @property
    def layers(self):
        """If true, the layers are saved."""
        return self.app.layers

    @layers.setter
    def layers(self, value):
        self.app.layers = value

    @property
    def saveImagePyramid(self):
        """If true, preserves multi-resolution information."""
        return self.app.saveImagePyramid

    @saveImagePyramid.setter
    def saveImagePyramid(self, value):
        self.app.saveImagePyramid = value

    @property
    def spotColors(self):
        """If true, spot colors are saved."""
        return self.app.spotColors

    @spotColors.setter
    def spotColors(self, value):
        self.app.spotColors = value

    @property
    def transparency(self):
        return self.app.transparency

    @transparency.setter
    def transparency(self, value):
        """If true, saves the transparency as an additional alpha channel when
        the file is opened in another application."""
        self.app.transparency = value
