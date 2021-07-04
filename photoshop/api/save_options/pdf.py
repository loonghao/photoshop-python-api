"""Options for saving a document in Adobe PDF format.

using the Document.saveAs() method.

"""

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import PDFEncodingType
from photoshop.api.enumerations import PDFResampleType
from photoshop.api.errors import COMError


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class PDFSaveOptions(Photoshop):
    object_name = "PDFSaveOptions"

    def __init__(self, **kwargs):
        super().__init__()
        self.layers = False
        self.jpegQuality = 12
        self.alphaChannels = False
        self.embedThumbnail = True
        self.view = False
        self.annotations = True
        self.colorConversion = False
        self.convertToEightBit = True
        self.description = "No description."
        self.encoding_types = PDFEncodingType
        self.downSample = PDFResampleType.NoResample
        self.embedColorProfile = True
        if kwargs:
            if "encoding" in kwargs:
                self.encoding = kwargs.get("encoding", self.encoding_types.PDFJPEG)
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def alphaChannels(self):
        """True to save the alpha channels with the file."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value):
        """True to save the alpha channels with the file."""
        self.app.alphaChannels = value

    @property
    def annotations(self):
        """If true, the annotations are saved."""
        return self.app.anotations

    @annotations.setter
    def annotations(self, value):
        """If true, the annotations are saved."""
        self.app.annotations = value

    @property
    def colorConversion(self):
        """If true, converts the color profile to the destination profile."""
        return self.app.colorConversion

    @colorConversion.setter
    def colorConversion(self, value):
        """If true, converts the color profile to the destination profile."""
        self.app.colorConversion = value

    @property
    def convertToEightBit(self):
        """If true, converts a 16-bit image to 8-bit for better
        compatibility with other applications."""
        return self.app.convertToEightBit

    @convertToEightBit.setter
    def convertToEightBit(self, value):
        """If true, converts a 16-bit image to 8-bit for better
        compatibility with other applications."""
        self.app.convertToEightBit = value

    @property
    def description(self):
        """Description of the save options in use."""
        return self.app.description

    @description.setter
    def description(self, text):
        """Description of the save options in use."""
        self.app.description = text

    @property
    def destinationProfile(self):
        """Describes the final RGB or CMYK output device,
        such as a monitor or press standard."""
        try:
            return self.app.destinationProfile
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @destinationProfile.setter
    def destinationProfile(self, value):
        """Describes the final RGB or CMYK output device,
        such as a monitor or press standard."""
        self.app.destinationProfile = value

    @property
    def downSample(self):
        """The downsample method to use."""
        return self.app.downSample

    @downSample.setter
    def downSample(self, value):
        """The downsample method to use."""
        self.app.downSample = value

    @property
    def downSampleSize(self):
        """The size (in pixels per inch) to downsample images to if they
        exceed the value specified for down sample size limit."""
        try:
            return self.app.downSampleSize
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @downSampleSize.setter
    def downSampleSize(self, value):
        """The size (in pixels per inch) to downsample images to if they
        exceed the value specified for ‘down sample size limit’."""
        self.app.downSampleSize = value

    @property
    def downSampleSizeLimit(self):
        """Limits downsampling or subsampling to images that
        exceed this value (in pixels per inch)."""
        try:
            return self.app.downSampleSizeLimit
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @downSampleSizeLimit.setter
    def downSampleSizeLimit(self, value: float):
        """Limits downsampling or subsampling to images that exceed this
        value (in pixels per inch)."""
        self.app.downSampleSizeLimit = value

    @property
    def embedColorProfile(self):
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value: bool):
        """If true, the color profile is embedded in the document."""
        self.app.embedColorProfile = value

    @property
    def embedThumbnail(self):
        """If true, includes a small preview image in Acrobat."""
        return self.app.embedThumbnail

    @embedThumbnail.setter
    def embedThumbnail(self, value: bool):
        """If true, includes a small preview image in Acrobat."""
        self.app.embedThumbnail = value

    @property
    def encoding(self):
        """The encoding method to use."""
        try:
            return self.app.encoding
        except COMError:
            return self.encoding_types.PDFJPEG

    @encoding.setter
    def encoding(self, value: str):
        """The encoding method to use."""
        self.app.encoding = value

    @property
    def jpegQuality(self):
        """Get the quality of the produced image."""
        return self.app.jpegQuality

    @jpegQuality.setter
    def jpegQuality(self, quality: int):
        """Set the quality of the produced image.

        Valid only for JPEG-encoded PDF documents. Range: 0 to 12.

        """
        self.app.jpegQuality = quality

    @property
    def layers(self):
        """If true, the layers are saved."""
        return self.app.layers

    @layers.setter
    def layers(self, value: bool):
        """If true, the layers are saved."""
        self.app.layers = value

    @property
    def optimizeForWeb(self):
        """If true, improves performance of PDFs on Web servers."""
        return self.app.optimizeForWeb

    @optimizeForWeb.setter
    def optimizeForWeb(self, value: bool):
        """If true, improves performance of PDFs on Web servers."""
        self.app.optimizeForWeb = value

    @property
    def outputCondition(self):
        """An optional comment field for inserting descriptions of the
        output condition. The text is stored in the PDF/X file."""
        return self.app.outputCondition

    @outputCondition.setter
    def outputCondition(self, value):
        """An optional comment field for inserting descriptions of
        the output condition. The text is stored in the PDF/X file."""
        self.app.outputCondition = value

    @property
    def outputConditionID(self):
        """The identifier for the output condition."""
        try:
            return self.app.outputConditionID
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @outputConditionID.setter
    def outputConditionID(self, value):
        """The identifier for the output condition."""
        self.app.outputConditionID = value

    @property
    def preserveEditing(self):
        """If true, allows users to reopen the PDF in Photoshop with
        native Photoshop data intact."""
        try:
            return self.app.preserveEditing
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @preserveEditing.setter
    def preserveEditing(self, value):
        """If true, allows users to reopen the PDF in Photoshop with
        native Photoshop data intact."""
        self.app.preserveEditing = value

    @property
    def presetFile(self):
        """The preset file to use for settings; overrides other settings."""
        try:
            return self.app.presetFile
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @presetFile.setter
    def presetFile(self, file_name):
        """The preset file to use for settings; overrides other settings."""
        self.app.presetFile = file_name

    @property
    def profileInclusionPolicy(self):
        """If true, shows which profiles to include."""
        try:
            return self.app.profileInclusionPolicy
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @profileInclusionPolicy.setter
    def profileInclusionPolicy(self, value):
        """If true, shows which profiles to include."""
        self.app.profileInclusionPolicy = value

    @property
    def registryName(self):
        """The URL where the output condition is registered."""
        try:
            return self.app.registryName
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @registryName.setter
    def registryName(self, value):
        """The URL where the output condition is registered."""
        self.app.registryName = value

    @property
    def spotColors(self):
        """If true, the spot colors are saved."""
        try:
            return self.app.spotColors
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @spotColors.setter
    def spotColors(self, value):
        """If true, the spot colors are saved."""
        self.app.spotColors = value

    @property
    def tileSize(self):
        """The compression option. Valid only when encoding is JPEG2000."""
        try:
            return self.app.tileSize
        except COMError:
            raise ValueError(
                "Should set value first. "
                "This parameter can only be read after the "
                "value has been set."
            )

    @tileSize.setter
    def tileSize(self, value):
        """The compression option. Valid only when encoding is JPEG2000."""
        if self.encoding not in (
            self.encoding_types.PDFJPEG2000HIGH,
            self.encoding_types.PDFJPEG2000LOSSLESS,
            self.encoding_types.PDFJPEG2000MED,
            self.encoding_types.PDFJPEG2000MEDLOW,
            self.encoding_types.PDFJPEG2000LOW,
            self.encoding_types.PDFJPEG2000MEDHIGH,
        ):
            raise ValueError(
                "tileSize only work in JPEG2000. Please "
                "change PDFSaveOptions.encoding to JPEG2000."
            )
        self.app.tileSize = value

    @property
    def view(self):
        """If true, opens the saved PDF in Acrobat."""
        return self.app.view

    @view.setter
    def view(self, value):
        """If true, opens the saved PDF in Acrobat."""
        self.app.view = value
