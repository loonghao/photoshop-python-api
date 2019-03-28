# Import local modules
from photoshop_python_api import save_options
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layers import ArtLayers


class Documents(Photoshop):
    def __init__(self):
        super(Documents, self).__init__()

    def Add(self):
        return self.adobe.Documents.Add()

    @property
    def ActiveDocument(self):
        """The current active Document."""
        return self.adobe.ActiveDocument

    @property
    def active_layer(self):
        """The selected layer."""
        return self.ActiveDocument.ActiveLayer

    @property
    def art_layers(self):
        return ArtLayers()

    @property
    def active_channels(self):
        """The selected channels."""
        return self.ActiveDocument.ActiveChannels

    @property
    def active_history_brush_source(self):
        """The history state to use with the history brush."""
        return self.ActiveDocument.ActiveHistoryBrushSource

    @property
    def active_history_state(self):
        """The current history state for this Document."""
        return self.ActiveDocument.ActiveHistoryState

    @property
    def background_layer(self):
        """The background layer for the Document."""
        return self.ActiveDocument.BackgroundLayer

    @property
    def bits_per_channel(self):
        """The number of bits per channel."""
        return self.ActiveDocument.BitsPerChannel

    @property
    def color_profile_name(self):
        """The name of the color profile. Valid only when no value is specified
        for color profile kind (to indicate a custom color profile)."""
        return self.ActiveDocument.ColorProfileName

    @property
    def color_profile_type(self):
        """The type of color model that defines the working space of the
        Document."""
        return self.ActiveDocument.ColorProfileType

    @property
    def color_samplers(self):
        """The current color samplers associated with the Document."""
        return self.ActiveDocument.ColorSamplers

    @property
    def component_channels(self):
        """The color component channels for this Document."""
        return self.ActiveDocument.ComponentChannels

    @property
    def count_items(self):
        """The current count items in the Document."""
        return self.ActiveDocument.CountItems

    @property
    def full_name(self):
        """The full path name of the Document."""
        return self.ActiveDocument.FullName

    # @property
    # def guides(self):
    #     return self.ActiveDocument.Guides
    @property
    def height(self):
        """The height of the Document."""
        return self.ActiveDocument.Height

    @property
    def histogram(self):
        """A histogram showing the number of pixels at each color intensity
        level for the composite channel."""
        return self.ActiveDocument.Histogram

    @property
    def history_states(self):
        """The history states collection in this Document."""
        return self.ActiveDocument.HistoryStates

    @property
    def id(self):
        """The unique ID of this Document."""
        return self.ActiveDocument.Id

    @property
    def info(self):
        """Metadata about the Document."""
        return self.ActiveDocument.Info

    @property
    def layer_comps(self):
        """The layer comps collection in this Document."""
        return self.ActiveDocument.LayerComps

    @property
    def layers(self):
        """The layers collection in the Document."""
        return self.ActiveDocument.Layers

    @property
    def layer_setes(self):
        """The layer sets collection in the Document."""
        return self.ActiveDocument.LayerSets

    @property
    def managed(self):
        """If true, the Document is a workgroup Document."""
        return self.ActiveDocument.Managed

    @property
    def measurement_scale(self):
        """The measurement scale of the Document."""
        return self.ActiveDocument.MeasurementScale

    @property
    def mode(self):
        """The color profile."""
        return self.ActiveDocument.Mode

    @property
    def name(self):
        """The Document name."""
        return self.ActiveDocument.Name

    @property
    def parent(self):
        """The object's container."""
        return self.ActiveDocument.Parent

    @property
    def path(self):
        """The path to the Document."""
        return self.ActiveDocument.Path

    @path.setter
    def path(self, path):
        self.ActiveDocument.fullName = path

    @property
    def path_items(self):
        return self.ActiveDocument.PathItems

    @property
    def pixel_aspect_ratio(self):
        """The (custom) pixel aspect ratio of the Document. Range: 0.100 to 10.000."""
        return self.ActiveDocument.PixelAspectRatio

    # @property
    # def print_settings(self):
    #     """Document print settings."""
    #     return self.ActiveDocument.PrintSettings

    @property
    def quick_mask_mode(self):
        return self.ActiveDocument.QuickMaskMode

    @property
    def saved(self):
        """If true, the Document been saved since the last change."""
        return self.ActiveDocument.Saved

    @property
    def resolution(self):
        """The resolution of the Document (in pixels per inch)"""
        return self.ActiveDocument.resolution

    @property
    def selection(self):
        """The selected area of the Document."""
        return self.ActiveDocument.selection

    @property
    def typename(self):
        """The class name of the object."""
        return self.ActiveDocument.typename

    @property
    def width(self):
        return self.ActiveDocument.Width

    @property
    def xmp_metadata(self):
        """The XMP properties of the Document. The Camera RAW settings are
        stored here."""
        return self.ActiveDocument.XmpMetadata

    # Methods
    def auto_count(self, *args, **kwargs):
        """Counts the objects in the Document."""
        return self.ActiveDocument.AutoCount(*args, **kwargs)

    def changeMode(self, *args, **kwargs):
        """Changes the mode of the Document."""
        return self.ActiveDocument.ChangeMode(*args, **kwargs)

    def close(self, saving=save_options.PROMPTTOSAVECHANGES):
        return self.ActiveDocument.Close(saving)

    def convertProfile(self):
        return self.ActiveDocument.convertProfile()

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

    @property
    def documents(self):
        return self.adobe.Documents

    def close_all_documents(self, mode=3):
        for doc in self.documents:
            doc.Close(mode)

    def flatten(self):
        """Flattens all layers."""
        return self.ActiveDocument.Flatten()

    def merge_visible_layers(self):
        """Flattens all visible layers in the Document."""
        return self.ActiveDocument.MergeVisibleLayers()

    def crop(self, **kwargs):
        return self.ActiveDocument.Crop(**kwargs)

    def export_document(self, *args, **kwargs):
        """Exports the Document."""
        return self.ActiveDocument.ExportDocument(*args, **kwargs)

    def duplicate(self, name, merge_layers_only=False):
        return self.ActiveDocument.Duplicate(name, merge_layers_only)

    def paste(self, into_selection):
        """Pastes contents of the clipboard into the Document."""
        return self.ActiveDocument.Paste(into_selection)

    def rasterize_all_layers(self):
        return self.ActiveDocument.RasterizeAllLayers()

    def reveal_all(self):
        """Expands the Document to show clipped sections."""
        return self.ActiveDocument.RevealAll()

    def save(self):
        """Saves the Document."""
        return self.ActiveDocument.Save()

    def save_as(self, file_path, options, as_copy=False, ext=2):
        return self.ActiveDocument.SaveAs(file_path, options.option, as_copy,
                                          ext)

    def trim(self, *args, **kwargs):
        return self.ActiveDocument.trim(*args, **kwargs)

    def resize_image(self, width, height, resolution=72, psAutomatic=8):
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)

        Returns:

        """
        return self.ActiveDocument.ResizeImage(width, height, resolution,
                                               psAutomatic)
