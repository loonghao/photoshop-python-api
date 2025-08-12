"""Options for saving a document in Adobe PDF format.

using the Document.saveAs() method.

"""

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import (
    PDFCompatibilityType,
    PDFEncodingType,
    PDFResampleType,
    PDFStandardType,
)
from photoshop.api.errors import COMError


# pylint: disable=too-many-instance-attributes,too-many-public-methods
class PDFSaveOptions(Photoshop):
    """Options for saving a document in PDF format."""

    object_name = "PDFSaveOptions"

    def __init__(
        self,
        alphaChannels: bool = False,
        annotations: bool = True,
        colorConversion: bool = False,
        convertToEightBit: bool = True,
        description: str = "No description.",
        destinationProfile: str | None = None,
        downSample: PDFResampleType = PDFResampleType.NoResample,
        downSampleSize: float | None = None,
        downSampleSizeLimit: float | None = None,
        embedColorProfile: bool = True,
        embedThumbnail: bool = False,
        encoding: PDFEncodingType = PDFEncodingType.PDFZip,
        jpegQuality: int = 12,
        layers: bool = False,
        optimizeForWeb: bool = False,
        outputCondition: str | None = None,
        outputConditionID: str | None = None,
        PDFCompatibility: PDFCompatibilityType | None = None,
        PDFStandard: PDFStandardType | None = None,
        preserveEditing: bool = False,
        presetFile: str | None = None,
        profileInclusionPolicy: bool | None = None,
        registryName: str | None = None,
        spotColors: bool | None = None,
        tileSize: int | None = None,
        view: bool = False,
    ):
        super().__init__()
        self.alphaChannels = alphaChannels
        self.annotations = annotations
        self.colorConversion = colorConversion
        self.convertToEightBit = convertToEightBit
        self.description = description
        if destinationProfile is not None:
            self.destinationProfile
        self.downSample = downSample
        if downSampleSize is not None:
            self.downSampleSize = downSampleSize
        if downSampleSizeLimit is not None:
            self.downSampleSizeLimit = downSampleSizeLimit
        self.embedColorProfile = embedColorProfile
        self.embedThumbnail = embedThumbnail
        self.encoding = encoding
        self.jpegQuality = jpegQuality
        self.layers = layers
        self.optimizeForWeb = optimizeForWeb
        if outputCondition is not None:
            self.outputCondition = outputCondition
        if outputConditionID is not None:
            self.outputConditionID = outputConditionID
        if PDFCompatibility is not None:
            self.PDFCompatibility = PDFCompatibility
        if PDFStandard is not None:
            self.PDFStandard = PDFStandard
        self.preserveEditing = preserveEditing
        if presetFile is not None:
            self.presetFile = presetFile
        if profileInclusionPolicy is not None:
            self.profileInclusionPolicy = profileInclusionPolicy
        if registryName is not None:
            self.registryName = registryName
        if spotColors is not None:
            self.spotColors = spotColors
        if tileSize is not None:
            self.tileSize = tileSize
        self.view = view

    @property
    def alphaChannels(self) -> bool:
        """True to save the alpha channels with the file."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value: bool) -> None:
        """True to save the alpha channels with the file."""
        self.app.alphaChannels = value

    @property
    def annotations(self) -> bool:
        """If true, the annotations are saved."""
        return self.app.anotations

    @annotations.setter
    def annotations(self, value: bool) -> None:
        """If true, the annotations are saved."""
        self.app.annotations = value

    @property
    def colorConversion(self) -> bool:
        """If true, converts the color profile to the destination profile."""
        return self.app.colorConversion

    @colorConversion.setter
    def colorConversion(self, value: bool) -> None:
        """If true, converts the color profile to the destination profile."""
        self.app.colorConversion = value

    @property
    def convertToEightBit(self) -> bool:
        """If true, converts a 16-bit image to 8-bit for better
        compatibility with other applications."""
        return self.app.convertToEightBit

    @convertToEightBit.setter
    def convertToEightBit(self, value: bool) -> None:
        """If true, converts a 16-bit image to 8-bit for better
        compatibility with other applications."""
        self.app.convertToEightBit = value

    @property
    def description(self) -> str:
        """Description of the save options in use."""
        return self.app.description

    @description.setter
    def description(self, text: str) -> None:
        """Description of the save options in use."""
        self.app.description = text

    @property
    def destinationProfile(self) -> str:
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
    def destinationProfile(self, value: str) -> None:
        """Describes the final RGB or CMYK output device,
        such as a monitor or press standard."""
        self.app.destinationProfile = value

    @property
    def downSample(self) -> PDFResampleType:
        """The downsample method to use."""
        return PDFResampleType(self.app.downSample)

    @downSample.setter
    def downSample(self, value: PDFResampleType) -> None:
        """The downsample method to use."""
        self.app.downSample = value

    @property
    def downSampleSize(self) -> float:
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
    def downSampleSize(self, value: float) -> None:
        """The size (in pixels per inch) to downsample images to if they
        exceed the value specified for ‘down sample size limit’."""
        self.app.downSampleSize = value

    @property
    def downSampleSizeLimit(self) -> float:
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
    def downSampleSizeLimit(self, value: float) -> None:
        """Limits downsampling or subsampling to images that exceed this
        value (in pixels per inch)."""
        self.app.downSampleSizeLimit = value

    @property
    def embedColorProfile(self) -> bool:
        """If true, the color profile is embedded in the document."""
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, value: bool) -> None:
        """If true, the color profile is embedded in the document."""
        self.app.embedColorProfile = value

    @property
    def embedThumbnail(self) -> bool:
        """If true, includes a small preview image in Acrobat."""
        return self.app.embedThumbnail

    @embedThumbnail.setter
    def embedThumbnail(self, value: bool) -> None:
        """If true, includes a small preview image in Acrobat."""
        self.app.embedThumbnail = value

    @property
    def encoding(self) -> PDFEncodingType:
        """The encoding method to use."""
        try:
            return PDFEncodingType(self.app.encoding)
        except COMError:
            return PDFEncodingType.PDFJPEG

    @encoding.setter
    def encoding(self, value: PDFEncodingType) -> None:
        """The encoding method to use."""
        self.app.encoding = value

    @property
    def jpegQuality(self) -> int:
        """Get the quality of the produced image."""
        return self.app.jpegQuality

    @jpegQuality.setter
    def jpegQuality(self, quality: int) -> None:
        """Set the quality of the produced image.

        Valid only for JPEG-encoded PDF documents. Range: 0 to 12.

        """
        self.app.jpegQuality = quality

    @property
    def layers(self) -> bool:
        """If true, the layers are saved."""
        return self.app.layers

    @layers.setter
    def layers(self, value: bool) -> None:
        """If true, the layers are saved."""
        self.app.layers = value

    @property
    def optimizeForWeb(self) -> bool:
        """If true, improves performance of PDFs on Web servers."""
        return self.app.optimizeForWeb

    @optimizeForWeb.setter
    def optimizeForWeb(self, value: bool) -> None:
        """If true, improves performance of PDFs on Web servers."""
        self.app.optimizeForWeb = value

    @property
    def outputCondition(self) -> str:
        """An optional comment field for inserting descriptions of the
        output condition. The text is stored in the PDF/X file."""
        return self.app.outputCondition

    @outputCondition.setter
    def outputCondition(self, value: str) -> None:
        """An optional comment field for inserting descriptions of
        the output condition. The text is stored in the PDF/X file."""
        self.app.outputCondition = value

    @property
    def outputConditionID(self) -> str:
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
    def outputConditionID(self, value: str) -> None:
        """The identifier for the output condition."""
        self.app.outputConditionID = value

    @property
    def PDFCompatibility(self) -> PDFCompatibilityType:
        return PDFCompatibilityType(self.app.PDFCompatibility)

    @PDFCompatibility.setter
    def PDFCompatibility(self, value: PDFCompatibilityType) -> None:
        self.app.PDFCompatibility = value

    @property
    def PDFStandard(self) -> PDFStandardType:
        return PDFStandardType(self.app.PDFStandard)

    @PDFStandard.setter
    def PDFStandard(self, value: PDFStandardType) -> None:
        self.app.PDFStandard = value

    @property
    def preserveEditing(self) -> bool:
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
    def preserveEditing(self, value: bool) -> None:
        """If true, allows users to reopen the PDF in Photoshop with
        native Photoshop data intact."""
        self.app.preserveEditing = value

    @property
    def presetFile(self) -> str:
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
    def presetFile(self, file_name: str) -> None:
        """The preset file to use for settings; overrides other settings."""
        self.app.presetFile = file_name

    @property
    def profileInclusionPolicy(self) -> bool:
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
    def profileInclusionPolicy(self, value: bool) -> None:
        """If true, shows which profiles to include."""
        self.app.profileInclusionPolicy = value

    @property
    def registryName(self) -> str:
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
    def registryName(self, value: str) -> None:
        """The URL where the output condition is registered."""
        self.app.registryName = value

    @property
    def spotColors(self) -> bool:
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
    def spotColors(self, value: bool) -> None:
        """If true, the spot colors are saved."""
        self.app.spotColors = value

    @property
    def tileSize(self) -> int:
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
    def tileSize(self, value: int) -> None:
        """The compression option. Valid only when encoding is JPEG2000."""
        if self.encoding not in (
            PDFEncodingType.PDFJPEG2000HIGH,
            PDFEncodingType.PDFJPEG2000LOSSLESS,
            PDFEncodingType.PDFJPEG2000MED,
            PDFEncodingType.PDFJPEG2000MEDLOW,
            PDFEncodingType.PDFJPEG2000LOW,
            PDFEncodingType.PDFJPEG2000MEDHIGH,
        ):
            raise ValueError(
                "tileSize only work in JPEG2000. Please "
                "change PDFSaveOptions.encoding to JPEG2000."
            )
        self.app.tileSize = value

    @property
    def view(self) -> bool:
        """If true, opens the saved PDF in Acrobat."""
        return self.app.view

    @view.setter
    def view(self, value: bool) -> None:
        """If true, opens the saved PDF in Acrobat."""
        self.app.view = value
