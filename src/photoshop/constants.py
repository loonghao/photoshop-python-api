"""The photoshop constants."""

from functools import singledispatch


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

    return PatchCls


# This is an enum that will work in python-2 and python-3. No need for methods
# in here. This is an enum which means we don't need an __init__ method.
@magic_attr
class Adobe:
    presetKind = 1
    smartSharpen = 'smartSharpen'
    presetKindType = 'presetKindType'
    presetKindCustom = 'presetKindCustom'
    noiseReduction = 'noiseReduction'
    blur = 'blur'
    blurType = 'blurType'
    AMNT = 'Amnt'
    # Name of photoshop ``AdobeScriptAutomation Scripts``.
    ADOBE_SCRIPT_AUTOMATION_SCRIPTS = 'AdobeScriptAutomation Scripts'

    # The photoshop version to COM progid mappings.
    PHOTOSHOP_VERSION_MAPPINGS = {
        '2020': 140,
        '2019': 130,
        '2018': 120,
        '2017': 110,
    }

    # Values for Photoshop enumeration 'PsLayerKind'.
    NORMAL_LAYER = 1
    TEXT_LAYER = 2
    SOLID_FILL_LAYER = 3

    # Constants of Photoshop action.
    # The all action constants from ``ScriptingListenerJS`` plugin.
    # More ``StringIDs`` you can check out:
    # http://www.tonton-pixel.com/wp-content/uploads/DecisionTable.pdf
    NULL = 'null'
    GSNB = 'GsnB'
    ORDN = 'Ordn'
    DOCI = 'DocI'
    CLS = 'Cls '  # This string ID requires a space.
    LYR = 'Lyr '  # This string ID requires a space.
    OFST = 'Ofst'
    PRC = '#Prc'
    RDS = 'Rds '  # This string ID requires a space.
    PX1 = '#Pxl'
    PLC = 'Plc '  # This string ID requires a space.
    IDNT = 'Idnt'
    HRZN = 'Hrzn'
    IN = 'In  '  # This string ID requires two spaces.
    TRGT = 'Trgt'
    SAVE = 'save'
    SAVE_STAGE = 'saveStage'
    SAVE_STAGE_TYPE = 'saveStageType'
    SAVE_SUCCEEDED = 'saveSucceeded'
    RASTERIZE_LAYER = 'rasterizeLayer'
    YSN = 'YsN '  # This string ID requires a space.
    N = 'N   '  # This string ID requires three spaces.
    VRTC = 'Vrtc'
    SVNG = 'Svng'
    FTCS = 'FTcs'
    QCST = 'QCSt'
    QCSA = 'Qcsa'
    FORCE_NOTIFY = 'forceNotify'
    JSMS = 'jsMs'
    JSCT = 'jsCt'
    PLACED_LAYER_EDIT_CONTENTS = 'placedLayerEditContents'

    # The photoshop save options.
    JPEG_SAVE_OPTIONS = 'JPEGSaveOptions'
    PNG_SAVE_OPTIONS = 'PNGSaveOptions'
    PHOTOSHOP_SAVE_OPTIONS = 'PhotoshopSaveOptions'

    # Controls whether Photoshop displays dialogs during scripts.
    # Show all dialogs.
    DIALOG_MODES_ALL = 0
    # Show only dialogs related to errors.
    DIALOG_MODES_ERROR = 1
    # Show no dialogs.
    DIALOG_MODES_NO = 2

    # The measurement unit for ruler increments.
    UNITS_CM = 6  # Centimeters.
    UNITS_INCHES = 5  # Inches.
    UNITS_MM = 4  # Millimeters.
    UNITS_PERCENT = 3  # Percent.
    UNITS_PICAS = 2  # Picas.
    UNITS_PIXELS = 1  # Pixels.
    UNITS_POINTS = 0  # Points.


@magic_attr
class PsAdjustmentReference:
    Relative = 1
    Absolute = 2


@magic_attr
class AnchorPosition:
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
    NoAntialias = 1
    Sharp = 2
    Crisp = 3
    Strong = 4
    Smooth = 5


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
