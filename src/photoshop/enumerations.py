"""The enumerations defined for use with Photoshop properties and methods."""


def magic_attr(cls):
    def _mappings(index):
        for key, value in cls.__dict__.items():
            if index == value:
                return key

    class PatchCls(cls):
        def __init__(self, index):
            self._index = index

        def __repr__(self):
            return _mappings(self._index)

        def __eq__(self, other):
            return _mappings(self._index) == other

    return PatchCls


@magic_attr
class AdjustmentReference:
    """Color adjustment specifications."""

    Relative = 1
    Absolute = 2


@magic_attr
class AnchorPosition:
    """The pint around which to transform and object.

    This is the point that doest not move when an object is rotated or resized
    using methods in `ArtLayer`, `LayerSet` and `Selection`, or when the
    entire canvas is resized with Document.resizeCanvas().

    """

    TopLeft = 1
    TopCenter = 2
    TopRight = 3
    MiddleLeft = 4
    MiddleCenter = 5
    BottomLeft = 7
    BottomCenter = 8
    BottomRight = 9


@magic_attr
class AntiAlias:
    """

    Method to use to smooth edges by softening the color transition
    between edge pixels and background pixels.

    """

    NoAntialias = 1
    Sharp = 2
    Crisp = 3
    Strong = 4
    Smooth = 5


@magic_attr
class AutoKernType:
    """The type of kerning to use for characters.

    Used in `TextItem.autoKerning`.

    """

    Manual = 2
    Metrics = 1
    OPTICAL = 3


@magic_attr
class BatchDestinationType:
    """The Destination, if any, for batch-processed files, specified in the
    BatchOptions used with the `Application.batch()` method:


    """

    FOLDER = 1
    NODESTINATION = 2
    SAVEANDCLOSE = 3


@magic_attr
class BitmapConversionType:
    """Specifies the quality of an image you are converting to bitmap mode.

    Used in `BitmapConversionOptions`.

    """

    CUSTOMPATTERN = 1


@magic_attr
class NewDocumentMode:
    NewGray = 1
    NewRGB = 2
    NewCMYK = 3
    NewLab = 4
    NewBitmap = 5


@magic_attr
class DocumentFill:
    White = 1
    BackgroundColor = 2
    Transparent = 3


@magic_attr
class DialogModes:
    DisplayAllDialogs = 1
    DisplayErrorDialogs = 2
    DisplayNoDialogs = 3


@magic_attr
class SelectionType:
    ReplaceSelection = 1
    ExtendSelection = 2
    DiminishSelection = 3
    IntersectSelection = 4


@magic_attr
class TextureType:
    BlocksTexture = 1
    CanvasTexture = 2
    FrostedTexture = 3
    TinyLensTexture = 4
    TextureFile = 5


@magic_attr
class TextCase:
    AllCAPS = 1
    NORMAL = 2
    SMALLCAPS = 3


@magic_attr
class Units:
    Pixels = 1
    Inches = 2
    CM = 3
    MM = 4
    Points = 5
    Picas = 6
    Percent = 7


@magic_attr
class LayerKind:
    NormalLayer = 1
    TextLayer = 2
    SolidFillLayer = 3


@magic_attr
class FormatOptionsType:
    OptimizedBaseline = 2
    Progressive = 3
    StandardBaseline = 4


@magic_attr
class MatteType:
    NoMatte = 1
    ForegroundColorMatte = 2
    BackgroundColorMatte = 3
    WhiteMatte = 4
    BlackMatte = 5
    SemiGray = 6
    NetscapeGrayMatte = 7


@magic_attr
class ExtensionType:
    Lowercase = 2
    Uppercase = 3


@magic_attr
class BitsPerChannelType:
    Document1Bit = 1
    Document8Bits = 8
    Document16Bits = 16
    Document32Bits = 32


@magic_attr
class ColorBlendMode:
    NormalBlendColor = 2
    DissolveBlend = 3
    DarkenBlend = 4
    MultiplyBlend = 5
    ColorBurnBlend = 6
    LinearBurnBlend = 7
    LightenBlend = 8
    ScreenBlend = 9
    ColorDodgeBlend = 10
    LinearDodgeBlend = 11
    OverlayBlend = 12
    SoftLightBlend = 13
    HardLightBlend = 14
    VividLightBlend = 15
    LinearLightBlend = 16
    PinLightBlend = 17
    DifferenceBlend = 18
    ExclusionBlend = 19
    HueBlend = 20
    SaturationBlendColor = 21
    ColorBlendMode = 22
    LuminosityBlend = 23
    BehindBlend = 24
    ClearBlend = 25
    HardMixBlend = 26
    LighterColorBlend = 27
    DarkerColorBlend = 28
    SubtractBlend = 29
    DivideBlend = 30


@magic_attr
class StrokeLocation:
    InsideStroke = 1
    CenterStroke = 2
    OutsideStroke = 3


@magic_attr
class NoiseDistribution:
    UniformNoise = 1
    GaussianNoise = 2


@magic_attr
class SaveOptions:
    SaveChanges = 1
    DoNotSaveChanges = 2
    PromptToSaveChanges = 3


@magic_attr
class ColorModel:
    CMYK = 3
    GRAYSCALE = 1
    HSB = 5
    LAB = 4
    NONE = 1
    RGB = 1


@magic_attr
class DescValueType:
    ALLASTYPE = 1
    BOOLEANTYPE = 2
    CLASSTYPE = 3
    DOUBLETYPE = 4
    ENUMERATEDTYPE = 5
    INTEGERTYPE = 6
    LARGEINTEGERTYPE = 7
    LISTTYPE = 8
    OBJECTTYPE = 9
    RAWTYPE = 10
    REFERENCETYPE = 11
    STRINGTYPE = 12
    UNITDOUBLE = 13


@magic_attr
class ReferenceFormType:
    CLASSTYPE = 1
    ENUMERATED = 2
    IDENTIFIER = 3
    INDEX = 4
    NAME = 5
    OFFSET = 6
    PROPERTY = 7


@magic_attr
class MeasurementRange:
    ALLMEASUREMENTS = 1
    ACTIVEMEASUREMENTS = 2


@magic_attr
class ElementPlacement:
    INSIDE = 0
    PLACEATBEGINNING = 1
    PLACEATEND = 2
    PLACEBEFORE = 3
    PLACEAFTER = 4


@magic_attr
class TargaBitsPerPixels:
    SIXTEEN = 0
    THIRTYTWO = 1
    TWENTYFOUR = 2


@magic_attr
class RasterizeType:
    ENTIRELAYER = 0
    FILLCONTENT = 1
    LAYERCLIPPINGPATH = 2
    LINKEDLAYERS = 3
    SHAPE = 4
    TEXTCONTENTS = 5


__all__ = [
    "ColorModel",
    "AdjustmentReference",
    "AnchorPosition",
    "AntiAlias",
    "NewDocumentMode",
    "DescValueType",
    "DocumentFill",
    "DialogModes",
    "SelectionType",
    "TextureType",
    "Units",
    "LayerKind",
    "FormatOptionsType",
    "MatteType",
    "ExtensionType",
    "BitsPerChannelType",
    "ColorBlendMode",
    "StrokeLocation",
    "NoiseDistribution",
    "ReferenceFormType",
    "SaveOptions",
    "ElementPlacement",
    "TargaBitsPerPixels",
    "RasterizeType"
]
