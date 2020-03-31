try:
    from photoshop.action_descriptor import ActionDescriptor
    from photoshop.action_refrence import ActionReference
    from photoshop.application import Application
    from photoshop.artlayer import ArtLayer
    from photoshop.layerSets import LayerSets
    from photoshop.layerSet import LayerSet
    from photoshop.colors import (
        LabColor,
        HSBColor,
        CMYKColor,
        RGBColor,
    )
    from photoshop.document import Document
    from photoshop.documents import Documents
    from photoshop.layer import Layer
    from photoshop.save_options import (
        GIFSaveOptions,
        JPEGSaveOptions,
        PDFSaveOptions,
        PNGSaveOptions,
    )
    from photoshop.solid_color import SolidColor
    from photoshop.text_item import TextItem
    from photoshop.enumerations import NoiseDistribution
    from photoshop.enumerations import Units
    from photoshop.enumerations import LayerKind
    from photoshop.enumerations import NewDocumentMode
    from photoshop.enumerations import DocumentFill
    from photoshop.enumerations import DialogModes
    from photoshop.enumerations import SelectionType
    from photoshop.enumerations import TextureType
    from photoshop.enumerations import ColorBlendMode
    from photoshop.enumerations import StrokeLocation
    from photoshop.enumerations import SaveOptions
    from photoshop.constants import *
    from photoshop.errors import PhotoshopPythonAPIError
    from photoshop.errors import COMError
except ModuleNotFoundError:
    # Fix Build docs failed on readthedocs.
    pass


class Session:
    """Session of photoshop.

    We can control active documents in this Session.

    """
    presetKind = 'presetKindType'
    smartSharpen = 'smartSharpen'
    presetKindType = 'presetKindType'
    presetKindCustom = 'presetKindCustom'
    noiseReduction = 'noiseReduction'
    blur = 'blur'
    blurType = 'blurType'
    AMNT = 'Amnt'
    contentLayer = 'contentLayer'
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

    def __init__(self, file_path=None, action=None, callback=None,
                 auto_close=False):
        super().__init__()
        self.path = file_path
        self._auto_close = auto_close
        self._callback = callback
        self._action = action
        self._active_document = None
        self.app = Application()
        self.SaveOptions = SaveOptions
        self.SolidColor = SolidColor
        self.StrokeLocation = StrokeLocation
        self.ColorBlendMode = ColorBlendMode
        self.TextItem = TextItem
        self.ActionReference = ActionReference()
        self.ActionDescriptor = ActionDescriptor()
        self.NoiseDistribution = NoiseDistribution
        self.TextureType = TextureType
        self.SelectionType = SelectionType
        self.DocumentFill = DocumentFill
        self.DialogModes = DialogModes
        self.NewDocumentMode = NewDocumentMode
        self.LayerKind = LayerKind
        self.Units = Units
        self.GIFSaveOptions = GIFSaveOptions
        self.JPEGSaveOptions = JPEGSaveOptions
        self.PDFSaveOptions = PDFSaveOptions
        self.PNGSaveOptions = PNGSaveOptions
        self.LabColor = LabColor
        self.HSBColor = HSBColor
        self.CMYKColor = CMYKColor
        self.RGBColor = RGBColor

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
            _action = getattr(self, '_action_{}'.format(self._action))
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


# All public APIs.
__all__ = [
    'ActionDescriptor',
    'ActionReference',
    'ArtLayer',
    'Application',
    'CMYKColor',
    'ColorBlendMode',
    'DialogModes',
    'DocumentFill',
    'Document',
    'Documents',
    'SelectionType',
    'StrokeLocation',
    'TextureType',
    'NewDocumentMode',
    'LayerKind',
    'SolidColor',
    'TextItem',
    'LabColor',
    'LayerSets',
    'LayerSet',
    'HSBColor',
    'RGBColor',
    'Layer',
    'NoiseDistribution',
    'SaveOptions',
    'JPEGSaveOptions',
    'PNGSaveOptions',
    'PDFSaveOptions',
    'GIFSaveOptions',
    'Units',
    'Session'
]

__title__ = 'photoshop_python_api'
__version__ = '0.7.2'
__author__ = 'Long Hao'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Long Hao'
