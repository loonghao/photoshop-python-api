"""constants type of enum for Photoshop."""
# Import built-in modules
from enum import IntEnum


class LensType(IntEnum):
    MoviePrime = 5
    Prime105 = 3
    Prime35 = 2
    ZoomLens = 1


class AdjustmentReference(IntEnum):
    Absolute = 2
    Relative = 1


class AnchorPosition(IntEnum):
    BottomCenter = 8
    BottomLeft = 7
    BottomRight = 9
    MiddleCenter = 5
    MiddleLeft = 4
    MiddleRight = 6
    TopCenter = 2
    TopLeft = 1
    TopRight = 3


class AntiAlias(IntEnum):
    Crisp = 3
    NoAntialias = 1
    Sharp = 2
    Smooth = 5
    Strong = 4


class AutoKernType(IntEnum):
    Manual = 1
    Metrics = 2
    Optical = 3


class BMPDepthType(IntEnum):
    BMP16Bits = 16
    BMP1Bit = 1
    BMP24Bits = 24
    BMP32Bits = 32
    BMP4Bits = 4
    BMP8Bits = 8
    BMP_A1R5G5B5 = 61
    BMP_A4R4G4B4 = 64
    BMP_A8R8G8B8 = 67
    BMP_R5G6B5 = 62
    BMP_R8G8B8 = 65
    BMP_X1R5G5B5 = 60
    BMP_X4R4G4B4 = 63
    BMP_X8R8G8B8 = 66


class BatchDestinationType(IntEnum):
    Folder = 3
    NoDestination = 1
    SaveAndClose = 2


class BitmapConversionType(IntEnum):
    CustomPattern = 5
    DiffusionDither = 3
    HalfThreshold = 1
    HalftoneScreen = 4
    PatternDither = 2


class BitmapHalfToneType(IntEnum):
    HalftoneCross = 6
    HalftoneDiamond = 2
    HalftoneEllie = 3
    HalftoneLine = 4
    HalftoneRound = 1
    HalftoneSquare = 5


class BitsPerChannelType(IntEnum):
    Document16Bits = 16
    Document1Bit = 1
    Document32Bits = 32
    Document8Bits = 8


class BlendMode(IntEnum):
    ColorBlend = 22
    ColorBurn = 6
    ColorDodge = 10
    Darken = 4
    DarkerColor = 28
    Difference = 18
    Dissolve = 3
    Divide = 30
    Exclusion = 19
    HardLight = 14
    HardMix = 26
    Hue = 20
    Lighten = 8
    LighterColor = 27
    LinearBurn = 7
    LinearDodge = 11
    LinearLight = 16
    Luminosity = 23
    Multiply = 5
    NormalBlend = 2
    Overlay = 12
    PassThrough = 1
    PinLight = 17
    SaturationBlend = 21
    Screen = 9
    SoftLight = 13
    Subtract = 29
    VividLight = 15


class ByteOrderType(IntEnum):
    IBMByteOrder = 1
    MacOSByteOrder = 2


class CameraRAWSettingsType(IntEnum):
    CameraDefault = 0
    CustomSettings = 2
    SelectedImage = 1


class CameraRAWSize(IntEnum):
    ExtraLargeCameraRAW = 4
    LargeCameraRAW = 3
    MaximumCameraRAW = 5
    MediumCameraRAW = 2
    MinimumCameraRAW = 0
    SmallCameraRAW = 1


class Case(IntEnum):
    AllCa = 2
    NormalCase = 1
    SmallCa = 3


class ChangeMode(IntEnum):
    ConvertToBitmap = 5
    ConvertToCMYK = 3
    ConvertToGrayscale = 1
    ConvertToIndexedColor = 6
    ConvertToLab = 4
    ConvertToMultiChannel = 7
    ConvertToRGB = 2


class ChannelType(IntEnum):
    ComponentChannel = 1
    MaskedAreaAlphaChannel = 2
    SelectedAreaAlphaChannel = 3
    SpotColorChannel = 4


class ColorBlendMode(IntEnum):
    ColorBlendMode = 22
    BehindBlend = 24
    ClearBlend = 25
    ColorBurnBlend = 6
    ColorDodgeBlend = 10
    DarkenBlend = 4
    DarkerColorBlend = 28
    DifferenceBlend = 18
    DissolveBlend = 3
    DivideBlend = 30
    ExclusionBlend = 19
    HardLightBlend = 14
    HardMixBlend = 26
    HueBlend = 20
    LightenBlend = 8
    LighterColorBlend = 27
    LinearBurnBlend = 7
    LinearDodgeBlend = 11
    LinearLightBlend = 16
    LuminosityBlend = 23
    MultiplyBlend = 5
    NormalBlendColor = 2
    OverlayBlend = 12
    PinLightBlend = 17
    SaturationBlendColor = 21
    ScreenBlend = 9
    SoftLightBlend = 13
    SubtractBlend = 29
    VividLightBlend = 15


class ColorModel(IntEnum):
    CMYKModel = 3
    GrayscaleModel = 1
    HSBModel = 5
    LabModel = 4
    NoModel = 50
    RGBModel = 2


class ColorPicker(IntEnum):
    AdobeColorPicker = 1
    AppleColorPicker = 2
    PlugInColorPicker = 4
    WindowsColorPicker = 3


class ColorProfileType(IntEnum):
    Custom = 3
    No = 1
    Working = 2


class ColorReductionType(IntEnum):
    Adaptive = 2
    BlackWhiteReduction = 5
    CustomReduction = 4
    MacintoshColors = 7
    PerceptualReduction = 0
    Restrictive = 3
    SFWGrayscale = 6
    Selective = 1
    WindowsColors = 8


class ColorSpaceType(IntEnum):
    AdobeRGB = 0
    ColorMatchRGB = 1
    ProPhotoRGB = 2
    SRGB = 3


class CopyrightedType(IntEnum):
    CopyrightedWork = 1
    PublicDomain = 2
    Unmarked = 3


class CreateFields(IntEnum):
    Duplication = 1
    Interpolation = 2


class CropToType(IntEnum):
    ArtBox = 5
    BleedBox = 3
    BoundingBox = 0
    CropBox = 2
    MediaBox = 1
    TrimBox = 4


class DCSType(IntEnum):
    ColorComposite = 3
    GrayscaleComposite = 2
    NoComposite = 1


class DepthMaource(IntEnum):
    ImageHighlight = 4
    LayerMask = 3
    NoSource = 1
    TransparencyChannel = 2


class DescValueType(IntEnum):
    AliasType = 11
    BooleanType = 5
    ClassType = 10
    DoubleType = 2
    EnumeratedType = 8
    IntegerType = 1
    LargeIntegerType = 13
    ListType = 6
    ObjectType = 7
    RawType = 12
    ReferenceType = 9
    StringType = 4
    UnitDoubleType = 3


class DialogModes(IntEnum):
    DisplayAllDialogs = 1
    DisplayErrorDialogs = 2
    DisplayNoDialogs = 3


class Direction(IntEnum):
    Horizontal = 1
    Vertical = 2


class DisplacementMapType(IntEnum):
    StretchToFit = 1
    Tile = 2


class DitherType(IntEnum):
    Diffusion = 2
    NoDither = 1
    Noise = 4
    Pattern = 3


class DocumentFill(IntEnum):
    BackgroundColor = 2
    Transparent = 3
    White = 1


class DocumentMode(IntEnum):
    Bitmap = 5
    CMYK = 3
    Duotone = 8
    Grayscale = 1
    IndexedColor = 6
    Lab = 4
    MultiChannel = 7
    RGB = 2


class EditLogItemsType(IntEnum):
    Concise = 2
    Detailed = 3
    SessionOnly = 1


class ElementPlacement(IntEnum):
    PlaceAfter = 4
    PlaceAtBeginning = 1
    PlaceAtEnd = 2
    PlaceBefore = 3
    PlaceInside = 0


class EliminateFields(IntEnum):
    EvenFields = 2
    OddFields = 1


class ExportType(IntEnum):
    IllustratorPaths = 1
    SaveForWeb = 2


class ExtensionType(IntEnum):
    Lowercase = 2
    Uppercase = 3


class FileNamingType(IntEnum):
    Ddmm = 16
    Ddmmyy = 15
    DocumentNameLower = 2
    DocumentNameMixed = 1
    DocumentNameUpper = 3
    ExtensionLower = 17
    ExtensionUpper = 18
    Mmdd = 11
    Mmddyy = 10
    SerialLetterLower = 8
    SerialLetterUpper = 9
    SerialNumber1 = 4
    SerialNumber2 = 5
    SerialNumber3 = 6
    SerialNumber4 = 7
    Yyddmm = 14
    Yymmdd = 13
    Yyyymmdd = 12


class FontPreviewType(IntEnum):
    FontPreviewExtraLarge = 4
    FontPreviewHuge = 5
    FontPreviewLarge = 3
    FontPreviewMedium = 2
    FontPreviewNone = 0
    FontPreviewSmall = 1


class ForcedColors(IntEnum):
    BlackWhite = 2
    NoForced = 1
    Primaries = 3
    Web = 4


class FormatOptionsType(IntEnum):
    OptimizedBaseline = 2
    Progressive = 3
    StandardBaseline = 1


class GalleryConstrainType(IntEnum):
    ConstrainBoth = 3
    ConstrainHeight = 2
    ConstrainWidth = 1


class GalleryFontType(IntEnum):
    Arial = 1
    CourierNew = 2
    Helvetica = 3
    TimesNewRoman = 4


class GallerySecurityTextColorType(IntEnum):
    BlackText = 1
    CustomText = 3
    WhiteText = 2


class GallerySecurityTextPositionType(IntEnum):
    Centered = 1
    LowerLeft = 3
    LowerRight = 5
    UpperLeft = 2
    UpperRight = 4


class GallerySecurityTextRotateType(IntEnum):
    Clockwise45 = 2
    Clockwise90 = 3
    CounterClockwise45 = 4
    CounterClockwise90 = 5
    Zero = 1


class GallerySecurityType(IntEnum):
    Caption = 5
    Copyright = 4
    Credit = 6
    CustomSecurityText = 2
    Filename = 3
    NoSecurity = 1
    Title = 7


class GalleryThumbSizeType(IntEnum):
    CustomThumbnail = 4
    Large = 3
    Medium = 2
    Small = 1


class Geometry(IntEnum):
    Heptagon = 4
    Hexagon = 2
    Octagon = 5
    Pentagon = 1
    SquareGeometry = 3
    Triangle = 0


class GridLineStyle(IntEnum):
    GridDashedLine = 2
    GridDottedLine = 3
    GridSolidLine = 1


class GridSize(IntEnum):
    LargeGrid = 4
    MediumGrid = 3
    NoGrid = 1
    SmallGrid = 2


class GuideLineStyle(IntEnum):
    GuideDashedLine = 2
    GuideSolidLine = 1


class IllustratorPathType(IntEnum):
    AllPaths = 2
    DocumentBounds = 1
    NamedPath = 3


class Intent(IntEnum):
    AbsoluteColorimetric = 4
    Perceptual = 1
    RelativeColorimetric = 3
    Saturation = 2


class JavaScriptExecutionMode(IntEnum):
    BeforeRunning = 3
    DebuggerOnError = 2
    NeverShowDebugger = 1


class Justification(IntEnum):
    Center = 2
    CenterJustified = 5
    FullyJustified = 7
    Left = 1
    LeftJustified = 4
    Right = 3
    RightJustified = 6


class Language(IntEnum):
    BrazillianPortuguese = 13
    CanadianFrench = 4
    Danish = 17
    Dutch = 16
    EnglishUK = 2
    EnglishUSA = 1
    Finnish = 5
    French = 3
    German = 6
    Italian = 9
    Norwegian = 10
    NynorskNorwegian = 11
    OldGerman = 7
    Portuguese = 12
    Spanish = 14
    Swedish = 15
    SwissGerman = 8


class LayerCompressionType(IntEnum):
    RLELayerCompression = 1
    ZIPLayerCompression = 2


class LayerKind(IntEnum):
    """The kind of a layer."""

    BlackAndWhiteLayer = 22
    BrightnessContrastLayer = 9
    ChannelMixerLayer = 12
    ColorBalanceLayer = 8
    ColorLookup = 24
    CurvesLayer = 7
    ExposureLayer = 19
    GradientFillLayer = 4
    GradientMapLayer = 13
    HueSaturationLayer = 10
    InversionLayer = 14
    Layer3D = 20
    LevelsLayer = 6
    NormalLayer = 1
    PatternFillLayer = 5
    PhotoFilterLayer = 18
    PosterizeLayer = 16
    SelectiveColorLayer = 11
    SmartObjectLayer = 17
    SolidFillLayer = 3
    TextLayer = 2
    ThresholdLayer = 15
    Vibrance = 23
    VideoLayer = 21
    ArtboardLayer = 25  # Add new type for Artboard


class LayerType(IntEnum):
    ArtLayer = 1
    LayerSet = 2


class MagnificationType(IntEnum):
    ActualSize = 0
    FitPage = 1


class MatteType(IntEnum):
    BackgroundColorMatte = 3
    BlackMatte = 5
    ForegroundColorMatte = 2
    NetscapeGrayMatte = 7
    NoMatte = 1
    SemiGray = 6
    WhiteMatte = 4


class MeasurementRange(IntEnum):
    ActiveMeasurements = 2
    AllMeasurements = 1


class MeasurementSource(IntEnum):
    MeasureCountTool = 2
    MeasureRulerTool = 3
    MeasureSelection = 1


class NewDocumentMode(IntEnum):
    NewBitmap = 5
    NewCMYK = 3
    NewGray = 1
    NewLab = 4
    NewRGB = 2


class NoiseDistribution(IntEnum):
    GaussianNoise = 2
    UniformNoise = 1


class OffsetUndefinedAreas(IntEnum):
    OffsetRepeatEdgePixels = 3
    OffsetSetToLayerFill = 1
    OffsetWrapAround = 2


class OpenDocumentMode(IntEnum):
    OpenCMYK = 3
    OpenGray = 1
    OpenLab = 4
    OpenRGB = 2


class OpenDocumentType(IntEnum):
    AliasPIXOpen = 25
    BMPOpen = 2
    CameraRAWOpen = 32
    CompuServeGIFOpen = 3
    DICOMOpen = 33
    EOpen = 22
    EPICTPreviewOpen = 23
    ETIFFPreviewOpen = 24
    ElectricImageOpen = 26
    FilmstripOpen = 5
    JPEGOpen = 6
    PCXOpen = 7
    PDFOpen = 21
    PICTFileFormatOpen = 10
    PICTResourceFormatOpen = 11
    PNGOpen = 13
    PhotoCDOpen = 9
    PhotoshopDCS_1Open = 18
    PhotoshopDCS_2Open = 19
    PhotoshopEOpen = 4
    PhotoshopOpen = 1
    PhotoshopPDFOpen = 8
    PixarOpen = 12
    PortableBitmapOpen = 27
    RawOpen = 14
    SGIRGBOpen = 29
    ScitexCTOpen = 15
    SoftImageOpen = 30
    TIFFOpen = 17
    TargaOpen = 16
    WavefrontRLAOpen = 28
    WirelessBitmapOpen = 31


class OperatingSystem(IntEnum):
    OS2 = 1
    Windows = 2


class Orientation(IntEnum):
    Landscape = 1
    Portrait = 2


class OtherPaintingCursors(IntEnum):
    PreciseOther = 2
    StandardOther = 1


class PDFCompatibilityType(IntEnum):
    PDF13 = 1
    PDF14 = 2
    PDF15 = 3
    PDF16 = 4
    PDF17 = 5


class PDFEncodingType(IntEnum):
    PDFJPEG = 2
    PDFJPEG2000HIGH = 9
    PDFJPEG2000LOSSLESS = 14
    PDFJPEG2000LOW = 13
    PDFJPEG2000MED = 11
    PDFJPEG2000MEDHIGH = 10
    PDFJPEG2000MEDLOW = 12
    PDFJPEGHIGH = 4
    PDFJPEGLOW = 8
    PDFJPEGMED = 6
    PDFJPEGMEDHIGH = 5
    PDFJPEGMEDLOW = 7
    PDFNone = 0
    PDFZip = 1
    PDFZip4Bit = 3


class PDFResampleType(IntEnum):
    NoResample = 0
    PDFAverage = 1
    PDFBicubic = 3
    PDFSubSample = 2


class PDFStandardType(IntEnum):
    NoStandard = 0
    PDFX1A2001 = 1
    PDFX1A2003 = 2
    PDFX32002 = 3
    PDFX32003 = 4
    PDFX42008 = 5


class PICTBitsPerPixel(IntEnum):
    PICT16Bits = 16
    PICT2Bits = 2
    PICT32Bits = 32
    PICT4Bits = 4
    PICT8Bits = 8


class PICTCompression(IntEnum):
    JPEGHighPICT = 5
    JPEGLowPICT = 2
    JPEGMaximumPICT = 6
    JPEGMediumPICT = 4
    NoPICTCompression = 1


class PaintingCursors(IntEnum):
    BrushSize = 3
    Precise = 2
    Standard = 1


class PaletteType(IntEnum):
    Exact = 1
    LocalAdaptive = 8
    LocalPerceptual = 6
    LocalSelective = 7
    MacOSPalette = 2
    MasterAdaptive = 11
    MasterPerceptual = 9
    MasterSelective = 10
    PreviousPalette = 12
    Uniform = 5
    WebPalette = 4
    WindowsPalette = 3


class PathKind(IntEnum):
    ClippingPath = 2
    NormalPath = 1
    TextMask = 5
    VectorMask = 4
    WorkPath = 3


class PhotoCDColorSpace(IntEnum):
    Lab16 = 4
    Lab8 = 3
    RGB16 = 2
    RGB8 = 1


class PhotoCDSize(IntEnum):
    ExtraLargePhotoCD = 5
    LargePhotoCD = 4
    MaximumPhotoCD = 6
    MediumPhotoCD = 3
    MinimumPhotoCD = 1
    SmallPhotoCD = 2


class PicturePackageTextType(IntEnum):
    CaptionText = 5
    CopyrightText = 4
    CreditText = 6
    FilenameText = 3
    NoText = 1
    OriginText = 7
    UserText = 2


class PointKind(IntEnum):
    CornerPoint = 2
    SmoothPoint = 1


class PointType(IntEnum):
    PostScriptPoints = 1
    TraditionalPoints = 2


class PolarConversionType(IntEnum):
    PolarToRectangular = 2
    RectangularToPolar = 1


class PreviewType(IntEnum):
    EightBitTIFF = 3
    MonochromeTIFF = 2
    NoPreview = 1


class PurgeTarget(IntEnum):
    AllCaches = 4
    ClipboardCache = 3
    HistoryCaches = 2
    UndoCaches = 1


class QueryStateType(IntEnum):
    Always = 1
    Ask = 2
    Never = 3


class RadialBlurMethod(IntEnum):
    Spin = 1
    Zoom = 2


class RadialBlurBest(IntEnum):
    RadialBlurBest = 3
    RadialBlurDraft = 1
    RadialBlurGood = 2


class RasterizeType(IntEnum):
    EntireLayer = 5
    FillContent = 3
    LayerClippingPath = 4
    LinkedLayers = 6
    Shape = 2
    TextContents = 1


class ReferenceFormType(IntEnum):
    ReferenceClassType = 7
    ReferenceEnumeratedType = 5
    ReferenceIdentifierType = 3
    ReferenceIndexType = 2
    ReferenceNameType = 1
    ReferenceOffsetType = 4
    ReferencePropertyType = 6


class ResampleMethod(IntEnum):
    Automatic = 8
    Bicubic = 4
    BicubicAutomatic = 7
    BicubicSharper = 5
    BicubicSmoother = 6
    Bilinear = 3
    NearestNeighbor = 2
    NoResampling = 1
    PreserveDetails = 9


class ResetTarget(IntEnum):
    AllTools = 2
    AllWarnings = 1
    Everything = 3


class RippleSize(IntEnum):
    LargeRipple = 3
    MediumRipple = 2
    SmallRipple = 1


class SaveBehavior(IntEnum):
    AlwaysSave = 2
    AskWhenSaving = 3
    NeverSave = 1


class SaveDocumentType(IntEnum):
    AliasPIXSave = 25
    BMave = 2
    CompuServeGIFSave = 3
    ElectricImageSave = 26
    JPEGSave = 6
    PCXSave = 7
    PICTFileFormatSave = 10
    PICTResourceFormatSave = 11
    PNGSave = 13
    PhotoshopDCS_1Save = 18
    PhotoshopDCS_2Save = 19
    PhotoshopESave = 4
    PhotoshopPDFSave = 8
    Photoshoave = 1
    PixarSave = 12
    PortableBitmaave = 27
    RawSave = 14
    SGIRGBSave = 29
    ScitexCTSave = 15
    SoftImageSave = 30
    TIFFSave = 17
    TargaSave = 16
    WavefrontRLASave = 28
    WirelessBitmaave = 31


class SaveEncoding(IntEnum):
    Ascii = 3
    Binary = 1
    JPEGHigh = 5
    JPEGLow = 2
    JPEGMaximum = 6
    JPEGMedium = 4


class SaveLogItemsType(IntEnum):
    LogFile = 2
    LogFileAndMetadata = 3
    Metadata = 1


class SaveOptions(IntEnum):
    DoNotSaveChanges = 2
    PromptToSaveChanges = 3
    SaveChanges = 1


class SelectionType(IntEnum):
    DiminishSelection = 3
    ExtendSelection = 2
    IntersectSelection = 4
    ReplaceSelection = 1


class ShapeOperation(IntEnum):
    ShapeAdd = 1
    ShapeIntersect = 3
    ShapeSubtract = 4
    ShapeXOR = 2


class SmartBlurMode(IntEnum):
    SmartBlurEdgeOnly = 2
    SmartBlurNormal = 1
    SmartBlurOverlayEdge = 3


class SmartBlurQuality(IntEnum):
    SmartBlurHigh = 3
    SmartBlurLow = 1
    SmartBlurMedium = 2


class SourceSpaceType(IntEnum):
    DocumentSpace = 1
    ProofSpace = 2


class SpherizeMode(IntEnum):
    HorizontalSpherize = 2
    NormalSpherize = 1
    VerticalSpherize = 3


class StrikeThruType(IntEnum):
    StrikeBox = 3
    StrikeHeight = 2
    StrikeOff = 1


class StrokeLocation(IntEnum):
    CenterStroke = 2
    InsideStroke = 1
    OutsideStroke = 3


class TargaBitsPerPixels(IntEnum):
    Targa16Bits = 16
    Targa24Bits = 24
    Targa32Bits = 32


class TextComposer(IntEnum):
    AdobeEveryLine = 2
    AdobeSingleLine = 1


class TextType(IntEnum):
    ParagraphText = 2
    PointText = 1


class TextureType(IntEnum):
    BlocksTexture = 1
    CanvasTexture = 2
    FrostedTexture = 3
    TextureFile = 5
    TinyLensTexture = 4


class TiffEncodingType(IntEnum):
    NoTIFFCompression = 1
    TiffJPEG = 3
    TiffLZW = 2
    TiffZIP = 4


class ToolType(IntEnum):
    ArtHistoryBrush = 9
    BackgroundEraser = 4
    Blur = 11
    Brush = 2
    Burn = 14
    CloneStamp = 5
    ColorReplacementTool = 16
    Dodge = 13
    Eraser = 3
    HealingBrush = 7
    HistoryBrush = 8
    PatternStamp = 6
    Pencil = 1
    Sharpen = 12
    Smudge = 10
    Sponge = 15


class TransitionType(IntEnum):
    BlindsHorizontal = 1
    BlindsVertical = 2
    BoxIn = 4
    BoxOut = 5
    DissolveTransition = 3
    GlitterDown = 6
    GlitterRight = 7
    GlitterRightDown = 8
    NoTrasition = 9
    Random = 10
    SplitHorizontalIn = 11
    SplitHorizontalOut = 12
    SplitVerticalIn = 13
    SplitVerticalOut = 14
    WipeDown = 15
    WipeLeft = 16
    WipeRight = 17
    WipeUp = 18


class TrimType(IntEnum):
    BottomRightPixel = 9
    TopLeftPixel = 1
    TransparentPixels = 0


class TypeUnits(IntEnum):
    TypeMM = 4
    TypePixels = 1
    TypePoints = 5


class UndefinedAreas(IntEnum):
    RepeatEdgePixels = 2
    WrapAround = 1


class UnderlineType(IntEnum):
    UnderlineLeft = 3
    UnderlineOff = 1
    UnderlineRight = 2


class Units(IntEnum):
    CM = 3
    Inches = 2
    MM = 4
    Percent = 7
    Picas = 6
    Pixels = 1
    Points = 5


class Urgency(IntEnum):
    Four = 4
    High = 8
    Low = 1
    UrgencyNone = 0
    Normal = 5
    Seven = 7
    Six = 6
    Three = 3
    Two = 2


class Wartyle(IntEnum):
    Arc = 2
    ArcLower = 3
    ArcUpper = 4
    Arch = 5
    Bulge = 6
    Fish = 11
    FishEye = 13
    Flag = 9
    Inflate = 14
    NoWarp = 1
    Rise = 12
    ShellLower = 7
    ShellUpper = 8
    Squeeze = 15
    Twist = 16
    Wave = 10


class WaveType(IntEnum):
    Sine = 1
    Square = 3
    Triangular = 2


class WhiteBalanceType(IntEnum):
    AsShot = 0
    Auto = 1
    Cloudy = 3
    CustomCameraSettings = 8
    Daylight = 2
    Flash = 7
    Fluorescent = 6
    Shade = 4
    Tungsten = 5


class ZigZagType(IntEnum):
    AroundCenter = 1
    OutFromCenter = 2
    PondRipples = 3


__all__ = [
    "LensType",
    "AdjustmentReference",
    "AnchorPosition",
    "AntiAlias",
    "AutoKernType",
    "BMPDepthType",
    "BatchDestinationType",
    "BitmapConversionType",
    "BitmapHalfToneType",
    "BitsPerChannelType",
    "BlendMode",
    "ByteOrderType",
    "CameraRAWSettingsType",
    "CameraRAWSize",
    "Case",
    "ChangeMode",
    "ChannelType",
    "ColorBlendMode",
    "ColorModel",
    "ColorPicker",
    "ColorProfileType",
    "ColorReductionType",
    "ColorSpaceType",
    "CopyrightedType",
    "CreateFields",
    "CropToType",
    "DCSType",
    "DepthMaource",
    "DescValueType",
    "DialogModes",
    "Direction",
    "DisplacementMapType",
    "DitherType",
    "DocumentFill",
    "DocumentMode",
    "EditLogItemsType",
    "ElementPlacement",
    "EliminateFields",
    "ExportType",
    "ExtensionType",
    "FileNamingType",
    "FontPreviewType",
    "ForcedColors",
    "FormatOptionsType",
    "GalleryConstrainType",
    "GalleryFontType",
    "GallerySecurityTextColorType",
    "GallerySecurityTextPositionType",
    "GallerySecurityTextRotateType",
    "GallerySecurityType",
    "GalleryThumbSizeType",
    "Geometry",
    "GridLineStyle",
    "GridSize",
    "GuideLineStyle",
    "IllustratorPathType",
    "Intent",
    "JavaScriptExecutionMode",
    "Justification",
    "Language",
    "LayerCompressionType",
    "LayerKind",
    "LayerType",
    "MagnificationType",
    "MatteType",
    "MeasurementRange",
    "MeasurementSource",
    "NewDocumentMode",
    "NoiseDistribution",
    "OffsetUndefinedAreas",
    "OpenDocumentMode",
    "OpenDocumentType",
    "OperatingSystem",
    "Orientation",
    "OtherPaintingCursors",
    "PDFCompatibilityType",
    "PDFEncodingType",
    "PDFResampleType",
    "PDFStandardType",
    "PICTBitsPerPixel",
    "PICTCompression",
    "PaintingCursors",
    "PaletteType",
    "PathKind",
    "PhotoCDColorSpace",
    "PhotoCDSize",
    "PicturePackageTextType",
    "PointKind",
    "PointType",
    "PolarConversionType",
    "PreviewType",
    "PurgeTarget",
    "QueryStateType",
    "RadialBlurMethod",
    "RadialBlurBest",
    "RasterizeType",
    "ReferenceFormType",
    "ResampleMethod",
    "ResetTarget",
    "RippleSize",
    "SaveBehavior",
    "SaveDocumentType",
    "SaveEncoding",
    "SaveLogItemsType",
    "SaveOptions",
    "SelectionType",
    "ShapeOperation",
    "SmartBlurMode",
    "SmartBlurQuality",
    "SourceSpaceType",
    "SpherizeMode",
    "StrikeThruType",
    "StrokeLocation",
    "TargaBitsPerPixels",
    "TextComposer",
    "TextType",
    "TextureType",
    "TiffEncodingType",
    "ToolType",
    "TransitionType",
    "TrimType",
    "TypeUnits",
    "UndefinedAreas",
    "UnderlineType",
    "Units",
    "Urgency",
    "Wartyle",
    "WaveType",
    "WhiteBalanceType",
    "ZigZagType",
]
