# Import local modules
from photoshop_python_api import save_options
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layers import ArtLayers
from photoshop_python_api.constants import Adobe
from photoshop_python_api.errors import COMError


class Document(Photoshop):
    object_name = 'Application'

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def artLayers(self):
        return ArtLayers(self.app.artLayers)

    @property
    def activeDocument(self):
        return self.app.activeDocument

    @property
    def activeChannels(self):
        """The selected channels."""
        return self.activeDocument.activeChannels

    @property
    def activeHistoryBrushSource(self):
        """The history state to use with the history brush."""
        return self.activeDocument.activeHistoryBrushSource

    @property
    def active_history_state(self):
        """The current history state for this Document."""
        return self.activeDocument.activeHistoryState

    @property
    def background_layer(self):
        """The background layer for the Document."""
        return self.activeDocument.backgroundLayer

    @property
    def bitsPerChannel(self):
        """The number of bits per channel."""
        return self.activeDocument.bitsPerChannel

    @property
    def colorProfileName(self):
        """The name of the color profile. Valid only when no value is specified
        for color profile kind (to indicate a custom color profile)."""
        return self.activeDocument.colorProfileName

    @property
    def colorProfileType(self):
        """The type of color model that defines the working space of the
        Document."""
        return self.activeDocument.colorProfileType

    @property
    def colorSamplers(self):
        """The current color samplers associated with the Document."""
        return self.activeDocument.colorSamplers

    @property
    def componentChannels(self):
        """The color component channels for this Document."""
        return self.activeDocument.componentChannels

    @property
    def countItems(self):
        """The current count items in the Document."""
        return self.activeDocument.countItems

    @property
    def fullName(self):
        """The full path name of the Document."""
        try:
            return self.activeDocument.fullName
        except COMError:
            self.eval_javascript(
                'alert ("Please save your Document first!",'
                '"{}")'.format(self.title),
            )

    @property
    def height(self):
        """The height of the Document."""
        return self.activeDocument.Height

    @property
    def histogram(self):
        """A histogram showing the number of pixels at each color intensity
        level for the composite channel."""
        return self.activeDocument.Histogram

    @property
    def history_states(self):
        """The history states collection in this Document."""
        return self.activeDocument.HistoryStates

    @property
    def id(self):
        """The unique ID of this Document."""
        return self.activeDocument.Id

    @property
    def info(self):
        """Metadata about the Document."""
        return self.activeDocument.Info

    @property
    def layer_comps(self):
        """The layer comps collection in this Document."""
        return self.activeDocument.LayerComps

    @property
    def layers(self):
        """The layers collection in the Document."""
        return self.activeDocument.Layers

    @property
    def layer_setes(self):
        """The layer sets collection in the Document."""
        return self.activeDocument.LayerSets

    @property
    def managed(self):
        """If true, the Document is a workgroup Document."""
        return self.activeDocument.Managed

    @property
    def measurement_scale(self):
        """The measurement scale of the Document."""
        return self.activeDocument.MeasurementScale

    @property
    def mode(self):
        """The color profile."""
        return self.activeDocument.Mode

    @property
    def name(self):
        """The Document name."""
        return self.activeDocument.Name

    @property
    def parent(self):
        """The object's container."""
        return self.activeDocument.Parent

    @property
    def path(self):
        """The path to the Document."""
        try:
            return self.activeDocument.Path
        except COMError:
            self.eval_javascript(
                'alert ("Please save your Document first!",'
                '"{}")'.format(self.title),
            )

    @path.setter
    def path(self, path):
        self.activeDocument.fullName = path

    @property
    def pathItems(self):
        return self.activeDocument.pathItems

    @property
    def pixelAspectRatio(self):
        """The (custom) pixel aspect ratio of the Document.

        Range: 0.100 to 10.000.

        """
        return self.activeDocument.pixelAspectRatio

    @property
    def printSettings(self):
        """Document print settings."""
        return self.activeDocument.printSettings

    @property
    def quick_mask_mode(self):
        return self.activeDocument.QuickMaskMode

    @property
    def saved(self):
        """If true, the Document been saved since the last change."""
        return self.activeDocument.Saved

    @property
    def resolution(self):
        """The resolution of the Document (in pixels per inch)"""
        return self.activeDocument.resolution

    @property
    def selection(self):
        """The selected area of the Document."""
        return self.activeDocument.selection

    @property
    def typename(self):
        """The class name of the object."""
        return self.activeDocument.typename

    @property
    def width(self):
        return self.activeDocument.Width

    @property
    def xmp_metadata(self):
        """The XMP properties of the Document. The Camera RAW settings are
        stored here."""
        return self.activeDocument.XmpMetadata

    # Methods
    def auto_count(self, *args, **kwargs):
        """Counts the objects in the Document."""
        return self.activeDocument.AutoCount(*args, **kwargs)

    def changeMode(self, *args, **kwargs):
        """Changes the mode of the Document."""
        return self.activeDocument.ChangeMode(*args, **kwargs)

    def close(self, saving=save_options.DONOTSAVECHANGES):
        return self.activeDocument.close(saving)

    def convertProfile(self):
        return self.activeDocument.convertProfile()

    #
    # def add_art_layer(self):
    #     doc_ref = self.add()
    #     return doc_ref.ArtLayers.Add()
    #
    # def open(self, *args, **kwargs):
    #     super(Document, self).open(*args, **kwargs)
    #     return self.ActiveDocument

    #
    # @property
    # def ActiveDocument(self):
    #     return ActiveDocument()

    def flatten(self):
        """Flattens all layers."""
        return self.activeDocument.Flatten()

    def merge_visible_layers(self):
        """Flattens all visible layers in the Document."""
        return self.activeDocument.MergeVisibleLayers()

    def crop(self, **kwargs):
        return self.activeDocument.Crop(**kwargs)

    def export_document(self, *args, **kwargs):
        """Exports the Document."""
        return self.activeDocument.ExportDocument(*args, **kwargs)

    def duplicate(self, name, merge_layers_only=False):
        self.activeDocument.duplicate(name, merge_layers_only)
        from photoshop_python_api.active_document import ActiveDocument
        return ActiveDocument()

    def paste(self, into_selection):
        """Pastes contents of the clipboard into the Document."""
        return self.activeDocument.Paste(into_selection)

    def rasterize_all_layers(self):
        return self.activeDocument.RasterizeAllLayers()

    def reveal_all(self):
        """Expands the Document to show clipped sections."""
        return self.activeDocument.RevealAll()

    def save(self):
        """Saves the Document."""
        return self.activeDocument.Save()

    def saveAs(self, file_path, options, as_copy=False):
        """Saves the documents with the specified save options."""
        return self.app.saveAs(
            file_path, options, as_copy,
            Adobe.DIALOG_MODES_NO,
        )

    def trim(self, *args, **kwargs):
        return self.activeDocument.trim(*args, **kwargs)

    def resizeImage(self, width, height, resolution=72, psAutomatic=8):
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)

        Returns:

        """
        return self.activeDocument.resizeImage(
            width, height, resolution,
            psAutomatic,
        )
