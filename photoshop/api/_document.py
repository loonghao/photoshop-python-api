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
from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional, TypeVar, Union

# Import third-party modules
from comtypes import COMError

# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._artlayers import ArtLayers
from photoshop.api._channels import Channels
from photoshop.api._core import Photoshop
from photoshop.api._layerSet import LayerSet
from photoshop.api.enumerations import ExportType, ExtensionType, SaveOptions, TrimType

PS_Layer = TypeVar("PS_Layer", ArtLayer, LayerSet)


class Document(Photoshop):
    """The active containment object for the layers and all other objects in the script.

    the basic canvas for the file.
    """

    object_name = "Application"

    def __init__(self, parent: Any) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "autoCount",
            "changeMode",
            "close",
            "convertProfile",
            "Flatten",
            "mergeVisibleLayers",
            "crop",
            "export",
            "duplicate",
            "printOneCopy",
            "rasterizeAllLayers",
            "recordMeasurements",
            "revealAll",
            "save",
            "saveAs",
            "splitChannels",
            "trap",
            "trim",
            "resizeImage",
        )

    @property
    def artLayers(self) -> ArtLayers:
        return ArtLayers(self.app.artLayers)

    @property
    def activeLayer(self) -> PS_Layer:
        """The selected layer."""
        type_ = self.eval_javascript("app.activeDocument.activeLayer.typename")
        mappings = {"LayerSet": LayerSet, "ArtLayer": ArtLayer}
        func = mappings[type_]
        return func(self.app.activeLayer)

    @activeLayer.setter
    def activeLayer(self, layer: PS_Layer) -> None:
        """Sets the select layer as active layer.

        Args:
            layer: The artLayer or layerSet to set as active.

        """
        self.app.activeLayer = layer.app

    @property
    def activeChannels(self) -> List[Any]:
        """The selected channels."""
        return list(self.app.activeChannels)

    @activeChannels.setter
    def activeChannels(self, channels: List[Any]) -> None:
        self.app.activeChannels = channels

    @property
    def activeHistoryBrushSource(self) -> Any:
        """The history state to use with the history brush."""
        return self.app.activeHistoryBrushSource

    @property
    def activeHistoryState(self) -> Any:
        """The current history state for this document."""
        return self.app.activeHistoryState

    @activeHistoryState.setter
    def activeHistoryState(self, state: Any) -> None:
        self.app.activeHistoryState = state

    @property
    def backgroundLayer(self) -> ArtLayer:
        """The background layer for the Document."""
        return ArtLayer(self.app.backgroundLayer)

    @property
    def bitsPerChannel(self) -> int:
        """The number of bits per channel."""
        return self.app.bitsPerChannel

    @bitsPerChannel.setter
    def bitsPerChannel(self, value: int) -> None:
        self.app.bitsPerChannel = value

    @property
    def channels(self) -> Channels:
        return Channels(self.app.channels)

    @property
    def colorProfileName(self) -> str:
        """The name of the color profile."""
        return str(self.app.colorProfileName)

    @colorProfileName.setter
    def colorProfileName(self, name: str) -> None:
        self.app.colorProfileName = name

    @property
    def colorProfileType(self) -> Any:
        """The type of color model that defines the working space."""
        return self.app.colorProfileType

    @colorProfileType.setter
    def colorProfileType(self, profile_type: Any) -> None:
        self.app.colorProfileType = profile_type

    @property
    def colorSamplers(self) -> List[Any]:
        """The current color samplers associated with the Document."""
        return list(self.app.colorSamplers)

    @property
    def componentChannels(self) -> List[Any]:
        """The color component channels for this Document."""
        return list(self.app.componentChannels)

    @property
    def countItems(self) -> List[Any]:
        """The current count items in the Document."""
        return list(self.app.countItems)

    @property
    def fullName(self) -> str:
        """The full path name of the Document."""
        try:
            return str(self.app.fullName)
        except COMError:
            return ""

    @property
    def height(self) -> float:
        """The height of the Document."""
        return float(self.app.height)

    @property
    def histogram(self) -> List[int]:
        """A histogram showing the number of pixels at each color intensity level."""
        return list(self.app.histogram)

    def autoCount(self, *args: Any, **kwargs: Any) -> Any:
        """Counts the objects in the Document."""
        return self.app.autoCount(*args, **kwargs)

    def changeMode(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the mode of the Document."""
        return self.app.changeMode(*args, **kwargs)

    def close(self, saving: SaveOptions = SaveOptions.DoNotSaveChanges) -> None:
        """Closes the document."""
        return self.app.close(saving)

    def convertProfile(self) -> None:
        """Converts the color profile of the document."""
        return self.app.convertProfile()

    def flatten(self) -> None:
        """Flattens all layers."""
        return self.app.flatten()

    def mergeVisibleLayers(self) -> None:
        """Flattens all visible layers in the Document."""
        return self.app.mergeVisibleLayers()

    def crop(
        self,
        bounds: List[int],
        angle: Optional[float] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> None:
        """Crops the document.

        Args:
            bounds: Four coordinates for the region remaining after cropping.
            angle: The angle of cropping bounds.
            width: The width of the resulting document.
            height: The height of the resulting document.

        """
        return self.app.crop(bounds, angle, width, height)

    def exportDocument(
        self,
        file_path: Union[str, Path],
        exportAs: ExportType,
        options: Any,
    ) -> None:
        """Exports the Document.

        Args:
            file_path: Path where to save the exported file.
            exportAs: The export type.
            options: The export options.

        """
        if isinstance(file_path, Path):
            file_path = str(file_path)
        return self.eval_javascript(
            f'app.activeDocument.exportDocument("{file_path}", {exportAs}, {options})',
        )

    def duplicate(
        self,
        name: Optional[str] = None,
        merge_layers_only: bool = False,
    ) -> Document:
        """Duplicates this document.

        Args:
            name: The name of the new document.
            merge_layers_only: If true, duplicate merged layers only.

        Returns:
            The duplicated Document object.

        """
        return Document(self.app.duplicate(name, merge_layers_only))

    def paste(self) -> None:
        """Pastes contents of the clipboard into the Document."""
        return self.app.paste()

    def print(self) -> None:
        """Prints the document."""
        return self.app.print()

    def printOneCopy(self) -> None:
        """Print one copy of the document."""
        return self.app.printOneCopy()

    def rasterizeAllLayers(self) -> None:
        """Rasterize all layers."""
        return self.app.rasterizeAllLayers()

    def recordMeasurements(self, source: Any, dataPoints: List[Any]) -> None:
        """Records the measurements of document."""
        return self.app.recordMeasurements(source, dataPoints)

    def reveal_all(self) -> None:
        """Expands the Document to show clipped sections."""
        return self.app.revealAll()

    def save(self) -> None:
        """Saves the Document."""
        return self.app.save()

    def saveAs(
        self,
        file_path: Union[str, Path],
        options: Any,
        asCopy: bool = True,
        extensionType: ExtensionType = ExtensionType.Lowercase,
    ) -> None:
        """Saves the document with the specified save options.

        Args:
            file_path: Absolute path of file.
            options: Save options.
            asCopy: If true, saves as a copy.
            extensionType: The case of the extension.

        """
        if isinstance(file_path, Path):
            file_path = str(file_path)
        return self.app.saveAs(file_path, options, asCopy, extensionType)

    def splitChannels(self) -> List[Document]:
        """Splits the channels of the document."""
        return [Document(channel) for channel in self.app.splitChannels()]

    def suspendHistory(self, historyString: str, javaScriptString: str) -> None:
        """Provides a single history state for the entire script.

        Args:
            historyString: The history state name.
            javaScriptString: The JavaScript code to execute.

        """
        return self.app.suspendHistory(historyString, javaScriptString)

    def trap(self, width: int) -> None:
        """Applies trapping to a CMYK document.

        Args:
            width: The trap width in pixels.

        """
        return self.app.trap(width)

    def trim(
        self,
        trim_type: TrimType,
        top: bool = True,
        left: bool = True,
        bottom: bool = True,
        right: bool = True,
    ) -> None:
        """Trims the transparent area around the image.

        Args:
            trim_type: The color or type of pixels to base the trim on.
            top: If true, trims away the top of the document.
            left: If true, trims away the left of the document.
            bottom: If true, trims away the bottom of the document.
            right: If true, trims away the right of the document.

        """
        return self.app.trim(trim_type, top, left, bottom, right)

    def resizeImage(
        self,
        width: int,
        height: int,
        resolution: int = 72,
        automatic: int = 8,
    ) -> None:
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)
            automatic: Value for automatic.

        """
        return self.app.resizeImage(width, height, resolution, automatic)
