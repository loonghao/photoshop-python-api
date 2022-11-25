"""Provides a public session class for Photoshop api.

Usually we only need to manipulate the currently active document of photoshop.

So as follows:
```python

from photoshop import Session

with Session(action="new_document") as ps:
    doc = ps.active_document
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = 'Hello, World!'
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = ps.JPEGSaveOptions(quality=5)
    jpg = 'd:/hello_world.jpg'
    doc.saveAs(jpg, options, asCopy=True)
    ps.app.doJavaScript(f'alert("save to jpg: {jpg}")')

```

"""

# Import built-in modules
from typing import Any

# Import local modules
from photoshop.api import ActionDescriptor
from photoshop.api import ActionList
from photoshop.api import ActionReference
from photoshop.api import Application
from photoshop.api import BMPSaveOptions
from photoshop.api import BatchOptions
from photoshop.api import CMYKColor
from photoshop.api import EPSSaveOptions
from photoshop.api import EventID
from photoshop.api import ExportOptionsSaveForWeb
from photoshop.api import GIFSaveOptions
from photoshop.api import GrayColor
from photoshop.api import HSBColor
from photoshop.api import JPEGSaveOptions
from photoshop.api import LabColor
from photoshop.api import PDFSaveOptions
from photoshop.api import PNGSaveOptions
from photoshop.api import PhotoshopSaveOptions
from photoshop.api import RGBColor
from photoshop.api import SolidColor
from photoshop.api import TargaSaveOptions
from photoshop.api import TextItem
from photoshop.api import TiffSaveOptions
from photoshop.api import enumerations
from photoshop.api import errors


# pylint: disable=too-many-arguments
class Session:
    """Session of photoshop.

    We can control active documents in this Session.

    Attributes:
        app: Application of Photoshop.
        ActionReference:
        ActionDescriptor:

    """

    def __init__(
        self,
        file_path: str = None,
        action: str = None,
        callback: Any = None,
        auto_close: bool = False,
        ps_version: str = None,
    ):
        """Session of Photoshop.


        Examples:
            ```python

                from photoshop import Session
                with Session("your/psd/or/psb/file_path.psd",
                            action="open") as ps:
                    ps.echo(ps.active_document.name)
            ```

        Args:
            file_path: The absolute path of the file. This path can be
                used together with action. If the path is an existing ``psd`
                or image path, use ``open`` action to open this file in the
                current session.
            action: Name of the action.
                .e.g:
                    - open
                        Open the file from the option `file_path`.
                    - new_document
                        Create a new document.
                    - document_duplicate
                        Duplicate current active document.
            callback: The callback function for this Photoshop session. The idea behind it is to allow us to pass
                some custom callback function every time we exit the current Photoshop session.
            auto_close: Is it necessary to close the current document when exiting the current context session.
                The default is ``False`` not to exit current session.
            ps_version: Specify the version number of photoshop.
                .e.g:
                    - 2022
                    - 2021
                    - cs6

        """
        super().__init__()

        self.path = file_path
        self._auto_close = auto_close
        self._callback = callback
        self._action = action
        self._active_document = None

        self.app: Application = Application(version=ps_version)
        self.ActionReference: ActionReference = ActionReference()
        self.ActionDescriptor: ActionDescriptor = ActionDescriptor()
        self.ActionList: ActionList = ActionList()
        self.EventID = EventID
        self.SolidColor = SolidColor
        self.TextItem = TextItem
        self.BatchOptions = BatchOptions

        # The save options.
        self.GIFSaveOptions = GIFSaveOptions
        self.JPEGSaveOptions = JPEGSaveOptions
        self.PDFSaveOptions = PDFSaveOptions
        self.EPSSaveOptions = EPSSaveOptions
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
        self.LensType = enumerations.LensType
        self.AdjustmentReference = enumerations.AdjustmentReference
        self.AnchorPosition = enumerations.AnchorPosition
        self.AntiAlias = enumerations.AntiAlias
        self.AutoKernType = enumerations.AutoKernType
        self.BMPDepthType = enumerations.BMPDepthType
        self.BatchDestinationType = enumerations.BatchDestinationType
        self.BitmapConversionType = enumerations.BitmapConversionType
        self.BitmapHalfToneType = enumerations.BitmapHalfToneType
        self.BitsPerChannelType = enumerations.BitsPerChannelType
        self.BlendMode = enumerations.BlendMode
        self.ByteOrderType = enumerations.ByteOrderType
        self.CameraRAWSettingsType = enumerations.CameraRAWSettingsType
        self.CameraRAWSize = enumerations.CameraRAWSize
        self.Case = enumerations.Case
        self.ChangeMode = enumerations.ChangeMode
        self.ChannelType = enumerations.ChannelType
        self.ColorBlendMode = enumerations.ColorBlendMode
        self.ColorModel = enumerations.ColorModel
        self.ColorPicker = enumerations.ColorPicker
        self.ColorProfileType = enumerations.ColorProfileType
        self.ColorReductionType = enumerations.ColorReductionType
        self.ColorSpaceType = enumerations.ColorSpaceType
        self.CopyrightedType = enumerations.CopyrightedType
        self.CreateFields = enumerations.CreateFields
        self.CropToType = enumerations.CropToType
        self.DCSType = enumerations.DCSType
        self.DepthMaource = enumerations.DepthMaource
        self.DescValueType = enumerations.DescValueType
        self.DialogModes = enumerations.DialogModes
        self.Direction = enumerations.Direction
        self.DisplacementMapType = enumerations.DisplacementMapType
        self.DitherType = enumerations.DitherType
        self.DocumentFill = enumerations.DocumentFill
        self.DocumentMode = enumerations.DocumentMode
        self.EditLogItemsType = enumerations.EditLogItemsType
        self.ElementPlacement = enumerations.ElementPlacement
        self.EliminateFields = enumerations.EliminateFields
        self.ExportType = enumerations.ExportType
        self.ExtensionType = enumerations.ExtensionType
        self.FileNamingType = enumerations.FileNamingType
        self.FontPreviewType = enumerations.FontPreviewType
        self.ForcedColors = enumerations.ForcedColors
        self.FormatOptionsType = enumerations.FormatOptionsType
        self.GalleryConstrainType = enumerations.GalleryConstrainType
        self.GalleryFontType = enumerations.GalleryFontType
        self.GallerySecurityTextColorType = enumerations.GallerySecurityTextColorType
        self.GallerySecurityTextPositionType = enumerations.GallerySecurityTextPositionType
        self.GallerySecurityTextRotateType = enumerations.GallerySecurityTextRotateType
        self.GallerySecurityType = enumerations.GallerySecurityType
        self.GalleryThumbSizeType = enumerations.GalleryThumbSizeType
        self.Geometry = enumerations.Geometry
        self.GridLineStyle = enumerations.GridLineStyle
        self.GridSize = enumerations.GridSize
        self.GuideLineStyle = enumerations.GuideLineStyle
        self.IllustratorPathType = enumerations.IllustratorPathType
        self.Intent = enumerations.Intent
        self.JavaScriptExecutionMode = enumerations.JavaScriptExecutionMode
        self.Justification = enumerations.Justification
        self.Language = enumerations.Language
        self.LayerCompressionType = enumerations.LayerCompressionType
        self.LayerKind = enumerations.LayerKind
        self.LayerType = enumerations.LayerType
        self.MagnificationType = enumerations.MagnificationType
        self.MatteType = enumerations.MatteType
        self.MeasurementRange = enumerations.MeasurementRange
        self.MeasurementSource = enumerations.MeasurementSource
        self.NewDocumentMode = enumerations.NewDocumentMode
        self.NoiseDistribution = enumerations.NoiseDistribution
        self.OffsetUndefinedAreas = enumerations.OffsetUndefinedAreas
        self.OpenDocumentMode = enumerations.OpenDocumentMode
        self.OpenDocumentType = enumerations.OpenDocumentType
        self.OperatingSystem = enumerations.OperatingSystem
        self.Orientation = enumerations.Orientation
        self.OtherPaintingCursors = enumerations.OtherPaintingCursors
        self.PDFCompatibilityType = enumerations.PDFCompatibilityType
        self.PDFEncodingType = enumerations.PDFEncodingType
        self.PDFResampleType = enumerations.PDFResampleType
        self.PDFStandardType = enumerations.PDFStandardType
        self.PICTBitsPerPixel = enumerations.PICTBitsPerPixel
        self.PICTCompression = enumerations.PICTCompression
        self.PaintingCursors = enumerations.PaintingCursors
        self.PaletteType = enumerations.PaletteType
        self.PathKind = enumerations.PathKind
        self.PhotoCDColorSpace = enumerations.PhotoCDColorSpace
        self.PhotoCDSize = enumerations.PhotoCDSize
        self.PicturePackageTextType = enumerations.PicturePackageTextType
        self.PointKind = enumerations.PointKind
        self.PointType = enumerations.PointType
        self.PolarConversionType = enumerations.PolarConversionType
        self.PreviewType = enumerations.PreviewType
        self.PurgeTarget = enumerations.PurgeTarget
        self.QueryStateType = enumerations.QueryStateType
        self.RadialBlurMethod = enumerations.RadialBlurMethod
        self.RadialBlurBest = enumerations.RadialBlurBest
        self.RasterizeType = enumerations.RasterizeType
        self.ReferenceFormType = enumerations.ReferenceFormType
        self.ResampleMethod = enumerations.ResampleMethod
        self.ResetTarget = enumerations.ResetTarget
        self.RippleSize = enumerations.RippleSize
        self.SaveBehavior = enumerations.SaveBehavior
        self.SaveDocumentType = enumerations.SaveDocumentType
        self.SaveEncoding = enumerations.SaveEncoding
        self.SaveLogItemsType = enumerations.SaveLogItemsType
        self.SaveOptions = enumerations.SaveOptions
        self.SelectionType = enumerations.SelectionType
        self.ShapeOperation = enumerations.ShapeOperation
        self.SmartBlurMode = enumerations.SmartBlurMode
        self.SmartBlurQuality = enumerations.SmartBlurQuality
        self.SourceSpaceType = enumerations.SourceSpaceType
        self.SpherizeMode = enumerations.SpherizeMode
        self.StrikeThruType = enumerations.StrikeThruType
        self.StrokeLocation = enumerations.StrokeLocation
        self.TargaBitsPerPixels = enumerations.TargaBitsPerPixels
        self.TextComposer = enumerations.TextComposer
        self.TextType = enumerations.TextType
        self.TextureType = enumerations.TextureType
        self.TiffEncodingType = enumerations.TiffEncodingType
        self.ToolType = enumerations.ToolType
        self.TransitionType = enumerations.TransitionType
        self.TrimType = enumerations.TrimType
        self.TypeUnits = enumerations.TypeUnits
        self.UndefinedAreas = enumerations.UndefinedAreas
        self.UnderlineType = enumerations.UnderlineType
        self.Units = enumerations.Units
        self.Urgency = enumerations.Urgency
        self.Wartyle = enumerations.Wartyle
        self.WaveType = enumerations.WaveType
        self.WhiteBalanceType = enumerations.WhiteBalanceType
        self.ZigZagType = enumerations.ZigZagType

    @property
    def active_document(self):
        """Get current active document.

        Raises:
            - PhotoshopPythonAPICOMError: No active document available.

        """
        try:
            if not self._active_document:
                return self.app.activeDocument
            return self._active_document
        except errors.PhotoshopPythonAPICOMError:
            raise errors.PhotoshopPythonAPIError("No active document available.")

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

    def run_action(self):
        try:
            _action = getattr(self, f"_action_{self._action}")
            _action()
        except AttributeError:
            pass

    def close(self):
        """closing current session."""
        if self._auto_close:
            self.active_document.close()

    def __enter__(self):
        self.run_action()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._callback:
                self._callback(self)
        except Exception as err:
            raise errors.PhotoshopPythonAPIError(err)
        finally:
            self.close()
