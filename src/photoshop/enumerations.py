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
