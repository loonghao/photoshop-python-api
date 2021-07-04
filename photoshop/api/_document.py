"""The active containment object for layers and all other objects.

The basic canvas for the file.

- Access the object for the currently active document through
  `Application.activeDocument.`
- You can access other documents or iterate through all open documents using
  in the `Application.documents` collection. You can access individual
  documents in the list by index, or use Documents.getByName() to retrieve
  them by name.
- Create documents programmatically using the Documents.add() method.


"""

# Import built-in modules
from pathlib import Path

# Import third-party modules
from comtypes import COMError

# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._artlayers import ArtLayers
from photoshop.api._channels import Channels
from photoshop.api._core import Photoshop
from photoshop.api._documentinfo import DocumentInfo
from photoshop.api._layerComps import LayerComps
from photoshop.api._layerSet import LayerSet
from photoshop.api._layerSets import LayerSets
from photoshop.api._layers import Layers
from photoshop.api._selection import Selection
from photoshop.api.enumerations import ExtensionType
from photoshop.api.enumerations import SaveOptions


# pylint: disable=too-many-public-methods
class Document(Photoshop):
    object_name = "Application"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def artLayers(self):
        return ArtLayers(self.app.artLayers)

    @property
    def activeLayer(self):
        """The selected layer."""
        type_ = self.eval_javascript("app.activeDocument.activeLayer.typename")
        mappings = {"LayerSet": LayerSet, "ArtLayer": ArtLayer}
        func = mappings[type_]
        return func(self.app.activeLayer)

    @activeLayer.setter
    def activeLayer(self, layer):
        """Sets the select layer as active layer.

        Args:
            layer (._artlayer.ArtLayer or
                   ._layerSet.LayerSet): The artLayer.

        """
        self.app.activeLayer = layer

    @property
    def activeChannels(self):
        """The selected channels."""
        return self.app.activeChannels

    @activeChannels.setter
    def activeChannels(self, channels):
        self.app.activeChannels = channels

    @property
    def activeHistoryBrushSource(self):
        """The history state to use with the history brush."""
        return self.app.activeHistoryBrushSource

    @property
    def activeHistoryState(self):
        """The current history state for this document."""
        return self.app.activeHistoryState

    @property
    def backgroundLayer(self):
        """The background layer for the Document."""
        return self.app.backgroundLayer

    @property
    def bitsPerChannel(self):
        """The number of bits per channel."""
        return self.app.bitsPerChannel

    @bitsPerChannel.setter
    def bitsPerChannel(self, value):
        self.app.bitsPerChannel = value

    @property
    def channels(self):
        return Channels(self.app.channels)

    @property
    def colorProfileName(self):
        """The name of the color profile. Valid only when no value is specified
        for color profile kind (to indicate a custom color profile)."""
        return self.app.colorProfileName

    @colorProfileName.setter
    def colorProfileName(self, name):
        self.app.colorProfileName = name

    @property
    def colorProfileType(self):
        """The type of color model that defines the working space of the
        Document."""
        return self.app.colorProfileType

    @colorProfileType.setter
    def colorProfileType(self, profile_type):
        self.app.colorProfileType = profile_type

    @property
    def colorSamplers(self):
        """The current color samplers associated with the Document."""
        return self.app.colorSamplers

    @property
    def componentChannels(self):
        """The color component channels for this Document."""
        return self.app.componentChannels

    @property
    def countItems(self):
        """The current count items in the Document."""
        return self.app.countItems

    @property
    def fullName(self):
        """The full path name of the Document."""
        try:
            return Path(self.app.fullName)
        except COMError:
            self.eval_javascript(
                'alert ("Please save your Document first!",' '"{}")'.format(self.name),
            )

    @property
    def height(self):
        """The height of the Document."""
        return self.app.Height

    @property
    def histogram(self):
        """A histogram showing the number of pixels at each color intensity
        level for the composite channel."""
        return self.app.Histogram

    @property
    def history_states(self):
        """The history states collection in this Document."""
        return self.app.HistoryStates

    @property
    def id(self):
        """The unique ID of this Document."""
        return self.app.Id

    @property
    def info(self):
        """Metadata about the Document."""
        return DocumentInfo(self.app.info)

    @property
    def layerComps(self):
        """The layer comps collection in this Document."""
        return LayerComps(self.app.layerComps)

    @property
    def layers(self):
        """The layers collection in the Document."""
        return Layers(self.app.Layers)

    @property
    def layerSets(self):
        """The layer sets collection in the Document."""
        return LayerSets(self.app.layerSets)

    @property
    def managed(self):
        """If true, the Document is a workgroup Document."""
        return self.app.Managed

    @property
    def measurement_scale(self):
        """The measurement scale of the Document."""
        return self.app.MeasurementScale

    @property
    def mode(self):
        """The color profile."""
        return self.app.Mode

    @property
    def name(self) -> str:
        """The Document name."""
        return self.app.name

    @property
    def parent(self):
        """The object's container."""
        return self.app.Parent

    @property
    def path(self):
        """The path to the Document."""
        try:
            return Path(self.app.path)
        except COMError:
            self.eval_javascript(
                'alert ("Please save your Document first!",' '"{}")'.format(self.name),
            )

    @path.setter
    def path(self, path):
        self.app.fullName = path

    @property
    def pathItems(self):
        return self.app.pathItems

    @property
    def pixelAspectRatio(self):
        """The (custom) pixel aspect ratio of the Document.

        Range: 0.100 to 10.000.

        """
        return self.app.pixelAspectRatio

    @property
    def printSettings(self):
        """Document print settings."""
        return self.app.printSettings

    @property
    def quickMaskMode(self):
        """If true, the document is in Quick Mask mode."""
        return self.app.quickMaskMode

    @property
    def saved(self):
        """If true, the Document been saved since the last change."""
        return self.app.Saved

    @property
    def resolution(self):
        """The resolution of the Document (in pixels per inch)"""
        return self.app.resolution

    @property
    def selection(self):
        """The selected area of the Document."""
        return Selection(self.app.selection)

    @property
    def typename(self):
        """The class name of the object."""
        return self.app.typename

    @property
    def cloudDocument(self):
        """This document is in the cloud."""
        return self.app.cloudDocument

    @property
    def cloudWorkAreaDirectory(self):
        """Local directory for this cloud document."""
        return self.app.cloudWorkAreaDirectory

    @property
    def width(self):
        return self.app.Width

    @property
    def xmpMetadata(self):
        """The XMP properties of the Document. The Camera RAW settings are
        stored here."""
        return self.app.xmpMetadata

    # Methods
    def autoCount(self, *args, **kwargs):
        """Counts the objects in the Document."""
        return self.app.autoCount(*args, **kwargs)

    def changeMode(self, *args, **kwargs):
        """Changes the mode of the Document."""
        return self.app.changeMode(*args, **kwargs)

    def close(self, saving=SaveOptions.DoNotSaveChanges):
        return self.app.close(saving)

    def convertProfile(self):
        return self.app.convertProfile()

    def flatten(self):
        """Flattens all layers."""
        return self.app.Flatten()

    def mergeVisibleLayers(self):
        """Flattens all visible layers in the Document."""
        return self.app.mergeVisibleLayers()

    def crop(self, bounds, angle=None, width=None, height=None):
        """Crops the document.

        Args:
            bounds (list of int): Four coordinates for the region remaining
                after cropping.
            angle (float, optional): The angle of cropping bounds.
            width (int, optional): The width of the resulting document.
            height (int, optional): The height of the resulting document.

        """
        return self.app.crop(bounds, angle, width, height)

    def exportDocument(self, file_path, exportAs=None, options=None):
        """Exports the Document."""
        return self.app.exportDocument(file_path, exportAs, options)

    def duplicate(self, name=None, merge_layers_only=False):
        return Document(self.app.duplicate(name, merge_layers_only))

    def paste(self):
        """Pastes contents of the clipboard into the Document."""
        return self.app.paste()

    def print(self):
        """Prints the document."""
        return self.app.print()

    def printOneCopy(self):
        self.app.printOneCopy()

    def rasterizeAllLayers(self):
        return self.app.rasterizeAllLayers()

    def recordMeasurements(self, source, dataPoints):
        """Records the measurements of document."""
        self.app.recordMeasurements(source, dataPoints)

    def reveal_all(self):
        """Expands the Document to show clipped sections."""
        return self.app.revealAll()

    def save(self):
        """Saves the Document."""
        return self.app.save()

    def saveAs(
        self, file_path, options, asCopy=True, extensionType=ExtensionType.Lowercase
    ):
        """Saves the documents with the specified save options.

        Args:
            file_path (str): Absolute path of psd file.
            options (.JPEGSaveOptions): Save options.
            asCopy (bool):
        """
        return self.app.saveAs(file_path, options, asCopy, extensionType)

    def splitChannels(self):
        """Splits the channels of the document."""
        self.app.splitChannels()

    def suspendHistory(self, historyString, javaScriptString):
        """Provides a single history state for the entire script.

        Allows a single undo for all actions taken in the script.

        """
        self.eval_javascript(
            f"app.activeDocument.suspendHistory('{historyString}',"
            f" '{javaScriptString}')"
        )

    def trap(self, width):
        """
        Applies trapping to a CMYK document.
        Valid only when ‘mode’ = CMYK.

        """
        self.app.trap(width)

    def trim(self, trim_type, top=True, left=True, bottom=True, right=True):
        """Trims the transparent area around the image on the specified
        sides of the canvas.

        Args:
            trim_type (TrimType): The color or type of pixels to base the trim
                on.
                .e.g:
                    - TrimType.BottomRightPixel
                    - TrimType.TopLeftPixel
                    - TrimType.TransparentPixels
            top (bool, optional): If true, trims away the top of the document.
            left (bool, optional): If true, trims away the left of the
                document.
            bottom (bool, optional): If true, trims away the bottom of the
                document.
            right (bool, optional): 	If true, trims away the right of the
                document.

        """
        return self.app.trim(trim_type, top, left, bottom, right)

    def resizeImage(self, width, height, resolution=72, automatic=8):
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)

        """
        return self.app.resizeImage(width, height, resolution, automatic)
