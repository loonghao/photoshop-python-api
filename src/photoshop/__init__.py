try:
    from photoshop import colors
    from photoshop import save_options
    from photoshop import enumerations
    from photoshop import errors
    from photoshop.action_descriptor import ActionDescriptor
    from photoshop.action_list import ActionList
    from photoshop.action_refrence import ActionReference
    from photoshop.application import Application
    from photoshop.constants import *
    from photoshop.enumerations import *
    from photoshop.errors import *
    from photoshop.colors import *
    from photoshop.solid_color import SolidColor
    from photoshop.save_options import *
    from photoshop.text_fonts import TextFonts
    from photoshop.text_item import TextItem
except ModuleNotFoundError:
    # Fix Build docs failed on readthedocs.
    pass


class Session:
    """Session of photoshop.

    We can control active documents in this Session.

    Attributes:
        app (photoshop.application.Application):

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

    def __init__(self,
                 file_path=None,
                 action=None,
                 actions=None,
                 callback=None,
                 auto_close=False):
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

            actions (list of str): The list of actions.
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
        self._actions = actions or []
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
        self.PhotoshopSaveOptions = PhotoshopSaveOptions
        self.ExportOptionsSaveForWeb = ExportOptionsSaveForWeb
        self.BMPSaveOptions = BMPSaveOptions
        self.TiffSaveOptions = TiffSaveOptions
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
            for action in self._actions:
                _action = getattr(self, '_action_{}'.format(action))
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
__all__ = (
    'ActionDescriptor',
    'ActionList',
    'ActionReference',
    'Application',
    'SolidColor',
    'TextFonts',
    'TextItem',
    'Session',
    colors.__all__
    + save_options.__all__
    + enumerations.__all__
    + errors.__all__
)


__title__ = 'photoshop_python_api'
__version__ = '0.8.0'
__author__ = 'Long Hao'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Long Hao'
