from typing import Any

# Import local modules
from photoshop.api import *


class Session:
    """Session of photoshop.

    We can control active documents in this Session.

    Attributes:
        app (photoshop.application.Application):

    """

    def __init__(
            self,
            file_path: str = None,
            action: str = None,
            callback: Any = None,
            auto_close=False,
    ):
        """Session of Photoshop.


        Examples:
            .. code-block:: python

                from photoshop import Session
                with Session("your/psd/or/psb/file_path.psd",
                            action="open") as ps:
                    ps.echo(ps.active_document.name)

        Args:
            file_path (str): The absolute path of the file. This path can be
                used together with action. If the path is an existing ``psd`
                or image path, use ``open`` action to open this file in the
                current session.
            action (str): Name of the action.
                .e.g:
                    - open
                        Open the file from the option `file_path`.
                    - new_document
                        Create a new document.
                    - document_duplicate
                        Duplicate current active document.
            callback (function): The callback function for this Photoshop
                session. The idea behind it is to allow us to pass some custom
                callback function every time we exit the current Photoshop
                session.
            auto_close (bool): Is it necessary to close the current document
                when exiting the current context session. The default is
                ``False`` not to exit current session.

        """
        super().__init__()

        self.path = file_path
        self._auto_close = auto_close
        self._callback = callback
        self._action = action
        self._active_document = None

        self.app = Application()
        self.ActionReference = ActionReference()
        self.ActionDescriptor = ActionDescriptor()
        self.EventID = EventID
        self.SolidColor = SolidColor
        self.TextItem = TextItem

        # The save options.
        self.GIFSaveOptions = GIFSaveOptions
        self.JPEGSaveOptions = JPEGSaveOptions
        self.PDFSaveOptions = PDFSaveOptions
        self.PNGSaveOptions = PNGSaveOptions
        self.PhotoshopSaveOptions = PhotoshopSaveOptions
        self.ExportOptionsSaveForWeb = ExportOptionsSaveForWeb
        self.BMPSaveOptions = BMPSaveOptions
        self.TiffSaveOptions = TiffSaveOptions
        self.TargaSaveOptions = TargaSaveOptions

        # The colors.
        self.LabColor = LabColor
        self.HSBColor = HSBColor
        self.CMYKColor = CMYKColor
        self.RGBColor = RGBColor
        self.GrayColor = GrayColor

        # From enumerations
        self.LensType = LensType
        self.AdjustmentReference = AdjustmentReference
        self.AnchorPosition = AnchorPosition
        self.AntiAlias = AntiAlias
        self.AutoKernType = AutoKernType
        self.BMPDepthType = BMPDepthType
        self.BatchDestinationType = BatchDestinationType
        self.BitmapConversionType = BitmapConversionType
        self.BitmapHalfToneType = BitmapHalfToneType
        self.BitsPerChannelType = BitsPerChannelType
        self.BlendMode = BlendMode
        self.ByteOrderType = ByteOrderType
        self.CameraRAWSettingsType = CameraRAWSettingsType
        self.CameraRAWSize = CameraRAWSize
        self.Case = Case
        self.ChangeMode = ChangeMode
        self.ChannelType = ChannelType
        self.ColorBlendMode = ColorBlendMode
        self.ColorModel = ColorModel
        self.ColorPicker = ColorPicker
        self.ColorProfileType = ColorProfileType
        self.ColorReductionType = ColorReductionType
        self.ColorSpaceType = ColorSpaceType
        self.CopyrightedType = CopyrightedType
        self.CreateFields = CreateFields
        self.CropToType = CropToType
        self.DCSType = DCSType
        self.DepthMaource = DepthMaource
        self.DescValueType = DescValueType
        self.DialogModes = DialogModes
        self.Direction = Direction
        self.DisplacementMapType = DisplacementMapType
        self.DitherType = DitherType
        self.DocumentFill = DocumentFill
        self.DocumentMode = DocumentMode
        self.EditLogItemsType = EditLogItemsType
        self.ElementPlacement = ElementPlacement
        self.EliminateFields = EliminateFields
        self.ExportType = ExportType
        self.ExtensionType = ExtensionType
        self.FileNamingType = FileNamingType
        self.FontPreviewType = FontPreviewType
        self.ForcedColors = ForcedColors
        self.FormatOptionsType = FormatOptionsType
        self.GalleryConstrainType = GalleryConstrainType
        self.GalleryFontType = GalleryFontType
        self.GallerySecurityTextColorType = GallerySecurityTextColorType
        self.GallerySecurityTextPositionType = GallerySecurityTextPositionType
        self.GallerySecurityTextRotateType = GallerySecurityTextRotateType
        self.GallerySecurityType = GallerySecurityType
        self.GalleryThumbSizeType = GalleryThumbSizeType
        self.Geometry = Geometry
        self.GridLineStyle = GridLineStyle
        self.GridSize = GridSize
        self.GuideLineStyle = GuideLineStyle
        self.IllustratorPathType = IllustratorPathType
        self.Intent = Intent
        self.JavaScriptExecutionMode = JavaScriptExecutionMode
        self.Justification = Justification
        self.Language = Language
        self.LayerCompressionType = LayerCompressionType
        self.LayerKind = LayerKind
        self.LayerType = LayerType
        self.MagnificationType = MagnificationType
        self.MatteType = MatteType
        self.MeasurementRange = MeasurementRange
        self.MeasurementSource = MeasurementSource
        self.NewDocumentMode = NewDocumentMode
        self.NoiseDistribution = NoiseDistribution
        self.OffsetUndefinedAreas = OffsetUndefinedAreas
        self.OpenDocumentMode = OpenDocumentMode
        self.OpenDocumentType = OpenDocumentType
        self.OperatingSystem = OperatingSystem
        self.Orientation = Orientation
        self.OtherPaintingCursors = OtherPaintingCursors
        self.PDFCompatibilityType = PDFCompatibilityType
        self.PDFEncodingType = PDFEncodingType
        self.PDFResampleType = PDFResampleType
        self.PDFStandardType = PDFStandardType
        self.PICTBitsPerPixel = PICTBitsPerPixel
        self.PICTCompression = PICTCompression
        self.PaintingCursors = PaintingCursors
        self.PaletteType = PaletteType
        self.PathKind = PathKind
        self.PhotoCDColorSpace = PhotoCDColorSpace
        self.PhotoCDSize = PhotoCDSize
        self.PicturePackageTextType = PicturePackageTextType
        self.PointKind = PointKind
        self.PointType = PointType
        self.PolarConversionType = PolarConversionType
        self.PreviewType = PreviewType
        self.PurgeTarget = PurgeTarget
        self.QueryStateType = QueryStateType
        self.RadialBlurMethod = RadialBlurMethod
        self.RadialBlurBest = RadialBlurBest
        self.RasterizeType = RasterizeType
        self.ReferenceFormType = ReferenceFormType
        self.ResampleMethod = ResampleMethod
        self.ResetTarget = ResetTarget
        self.RippleSize = RippleSize
        self.SaveBehavior = SaveBehavior
        self.SaveDocumentType = SaveDocumentType
        self.SaveEncoding = SaveEncoding
        self.SaveLogItemsType = SaveLogItemsType
        self.SaveOptions = SaveOptions
        self.SelectionType = SelectionType
        self.ShapeOperation = ShapeOperation
        self.SmartBlurMode = SmartBlurMode
        self.SmartBlurQuality = SmartBlurQuality
        self.SourceSpaceType = SourceSpaceType
        self.SpherizeMode = SpherizeMode
        self.StrikeThruType = StrikeThruType
        self.StrokeLocation = StrokeLocation
        self.TargaBitsPerPixels = TargaBitsPerPixels
        self.TextComposer = TextComposer
        self.TextType = TextType
        self.TextureType = TextureType
        self.TiffEncodingType = TiffEncodingType
        self.ToolType = ToolType
        self.TransitionType = TransitionType
        self.TrimType = TrimType
        self.TypeUnits = TypeUnits
        self.UndefinedAreas = UndefinedAreas
        self.UnderlineType = UnderlineType
        self.Units = Units
        self.Urgency = Urgency
        self.Wartyle = Wartyle
        self.WaveType = WaveType
        self.WhiteBalanceType = WhiteBalanceType
        self.ZigZagType = ZigZagType

    @property
    def active_document(self):
        try:
            if not self._active_document:
                return self.app.activeDocument
            return self._active_document
        except COMError:
            raise PhotoshopPythonAPIError("No active document available.")

    @staticmethod
    def echo(*args, **kwargs):
        """Print message."""
        print(*args, **kwargs)

    def alert(self, text: str):
        """Alert message box in photoshop.

        Args:
            text (str): The text will pop up in photoshop.

        """
        self.app.doJavaScript(f"alert('{text}')")

    @active_document.setter
    def active_document(self, active_document):
        """Set active document."""
        self._active_document = active_document

    def _action_open(self):
        self.active_document = self.app.open(self.path)

    def _action_new_document(self):
        self.active_document = self.app.documents.add()

    def _action_document_duplicate(self):
        self.active_document = self.active_document.duplicate()

    def __enter__(self):
        try:
            _action = getattr(self, f"_action_{self._action}")
            _action()
        except AttributeError:
            pass
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._callback:
                self._callback(self)
        except Exception as err:
            raise PhotoshopPythonAPIError(err)
        finally:
            if self._auto_close:
                self.active_document.close()
