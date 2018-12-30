# Import local modules
from photoshop_python_api import save_options
from photoshop_python_api._core import Core
from photoshop_python_api.art_layers import ArtLayers


class Document(Core):
    def __init__(self):
        super(Document, self).__init__()

    @property
    def active_document(self):
        """The current active document."""
        return self.ps.ActiveDocument

    @property
    def active_layer(self):
        """The selected layer."""
        return self.active_document.ActiveLayer

    @property
    def art_layers(self):
        return ArtLayers()

    @property
    def active_channels(self):
        """The selected channels."""
        return self.active_document.ActiveChannels

    @property
    def active_history_brush_source(self):
        """The history state to use with the history brush."""
        return self.active_document.ActiveHistoryBrushSource

    @property
    def active_history_state(self):
        """The current history state for this document."""
        return self.active_document.ActiveHistoryState

    @property
    def background_layer(self):
        """The background layer for the document."""
        return self.active_document.BackgroundLayer

    @property
    def bits_per_channel(self):
        """The number of bits per channel."""
        return self.active_document.BitsPerChannel

    @property
    def color_profile_name(self):
        """The name of the color profile. Valid only when no value is specified
        for color profile kind (to indicate a custom color profile)."""
        return self.active_document.ColorProfileName

    @property
    def color_profile_type(self):
        """The type of color model that defines the working space of the
        document."""
        return self.active_document.ColorProfileType

    @property
    def color_samplers(self):
        """The current color samplers associated with the document."""
        return self.active_document.ColorSamplers

    @property
    def component_channels(self):
        """The color component channels for this document."""
        return self.active_document.ComponentChannels

    @property
    def count_items(self):
        """The current count items in the document."""
        return self.active_document.CountItems

    @property
    def full_name(self):
        """The full path name of the document."""
        return self.active_document.FullName

    # @property
    # def guides(self):
    #     return self.active_document.Guides
    @property
    def height(self):
        """The height of the document."""
        return self.active_document.Height

    @property
    def histogram(self):
        """A histogram showing the number of pixels at each color intensity
        level for the composite channel."""
        return self.active_document.Histogram

    @property
    def history_states(self):
        """The history states collection in this document."""
        return self.active_document.HistoryStates

    @property
    def id(self):
        """The unique ID of this document."""
        return self.active_document.Id

    @property
    def info(self):
        """Metadata about the document."""
        return self.active_document.Info

    @property
    def layer_comps(self):
        """The layer comps collection in this document."""
        return self.active_document.LayerComps

    @property
    def layers(self):
        """The layers collection in the document."""
        return self.active_document.Layers

    @property
    def layer_setes(self):
        """The layer sets collection in the document."""
        return self.active_document.LayerSets

    @property
    def managed(self):
        """If true, the document is a workgroup document."""
        return self.active_document.Managed

    @property
    def measurement_scale(self):
        """The measurement scale of the document."""
        return self.active_document.MeasurementScale

    @property
    def mode(self):
        """The color profile."""
        return self.active_document.Mode

    @property
    def name(self):
        """The document name."""
        return self.active_document.Name

    @property
    def parent(self):
        """The object's container."""
        return self.active_document.Parent

    @property
    def path(self):
        """The path to the document."""
        return self.active_document.Path

    @path.setter
    def path(self, path):
        self.active_document.full_name = path

    @property
    def path_items(self):
        return self.active_document.PathItems

    @property
    def pixel_aspect_ratio(self):
        """The (custom) pixel aspect ratio of the document. Range: 0.100 to 10.000."""
        return self.active_document.PixelAspectRatio

    # @property
    # def print_settings(self):
    #     """Document print settings."""
    #     return self.active_document.PrintSettings

    @property
    def quick_mask_mode(self):
        return self.active_document.QuickMaskMode

    @property
    def saved(self):
        """If true, the document been saved since the last change."""
        return self.active_document.Saved

    @property
    def resolution(self):
        """The resolution of the document (in pixels per inch)"""
        return self.active_document.resolution

    @property
    def selection(self):
        """The selected area of the document."""
        return self.active_document.selection

    @property
    def typename(self):
        """The class name of the object."""
        return self.active_document.typename

    @property
    def width(self):
        return self.active_document.Width

    @property
    def xmp_metadata(self):
        """The XMP properties of the document. The Camera RAW settings are
        stored here."""
        return self.active_document.XmpMetadata

    # Methods
    def auto_count(self, *args, **kwargs):
        """Counts the objects in the document."""
        return self.active_document.AutoCount(*args, **kwargs)

    def changeMode(self, *args, **kwargs):
        """Changes the mode of the document."""
        return self.active_document.ChangeMode(*args, **kwargs)

    def close(self, saving=save_options.PROMPTTOSAVECHANGES):
        return self.active_document.Close(saving)

    def convertProfile(self):
        return self.active_document.convertProfile()

    #
    # def add_art_layer(self):
    #     doc_ref = self.add()
    #     return doc_ref.ArtLayers.Add()
    #
    # def open(self, *args, **kwargs):
    #     super(Document, self).open(*args, **kwargs)
    #     return self.active_document

    #
    # @property
    # def active_document(self):
    #     return ActiveDocument()

    @property
    def documents(self):
        return self.ps.Documents

    def close_all_documents(self, mode=3):
        for doc in self.documents:
            doc.Close(mode)

    def flatten(self):
        """Flattens all layers."""
        return self.active_document.Flatten()

    def merge_visible_layers(self):
        """Flattens all visible layers in the document."""
        return self.active_document.MergeVisibleLayers()

    def crop(self, **kwargs):
        return self.active_document.Crop(**kwargs)

    def export_document(self, *args, **kwargs):
        """Exports the document."""
        return self.active_document.ExportDocument(*args, **kwargs)

    def duplicate(self, name, merge_layers_only=False):
        return self.active_document.Duplicate(name, merge_layers_only)

    def paste(self, into_selection):
        """Pastes contents of the clipboard into the document."""
        return self.active_document.Paste(into_selection)

    def rasterize_all_layers(self):
        return self.active_document.RasterizeAllLayers()

    def reveal_all(self):
        """Expands the document to show clipped sections."""
        return self.active_document.RevealAll()

    def save(self):
        """Saves the document."""
        return self.active_document.Save()

    def save_as(self, file_path, options, as_copy=False, ext=2):
        return self.active_document.SaveAs(file_path, options.option, as_copy,
                                           ext)

    def trim(self, *args, **kwargs):
        return self.active_document.trim(*args, **kwargs)

    def resize_image(self, width, height, resolution=72, psAutomatic=8):
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)

        Returns:

        """
        return self.active_document.ResizeImage(width, height, resolution,
                                                psAutomatic)
