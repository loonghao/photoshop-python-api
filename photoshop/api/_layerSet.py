from collections.abc import Sequence
from typing import TYPE_CHECKING, Iterator

from photoshop.api._artlayer import ArtLayer
from photoshop.api._artlayers import ArtLayers
from photoshop.api._channel import Channel
from photoshop.api._channels import Channels
from photoshop.api._core import Photoshop
from photoshop.api._layer import Layer
from photoshop.api.enumerations import ElementPlacement


if TYPE_CHECKING:
    from photoshop.api._layers import Layers
    from photoshop.api._layerSets import LayerSets


class LayerSet(Layer):
    """A group of layer objects, which can include art layer objects and other (nested) layer set objects.

    A single command or set of commands manipulates all layers in a layer set object.

    """

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
            "merge",
        )

    @property
    def artLayers(self) -> ArtLayers:
        return ArtLayers(self.app.artLayers)

    @property
    def enabledChannels(self) -> Channels:
        return Channels(self.app.enabledChannels)

    @enabledChannels.setter
    def enabledChannels(self, value: Sequence[Channel] | Channels) -> None:
        self.app.enabledChannels = value.app if isinstance(value, Channels) else [channel.app for channel in value]

    @property
    def layers(self) -> "Layers":
        # pylint: disable=import-outside-toplevel
        from ._layers import Layers

        return Layers(self.app.layers)

    @property
    def layerSets(self) -> "LayerSets":
        # pylint: disable=import-outside-toplevel
        from ._layerSets import LayerSets

        return LayerSets(self.app.layerSets)

    def duplicate(
        self,
        relativeObject: Layer | None = None,
        insertionLocation: ElementPlacement | None = None,
    ):
        return LayerSet(self.app.duplicate(relativeObject.app if relativeObject else None, insertionLocation))

    def add(self) -> "LayerSet":
        """Adds an element."""
        return LayerSet(self.app.add())

    def merge(self) -> ArtLayer:
        """Merges the layer set."""
        return ArtLayer(self.app.merge())

    def __iter__(self) -> Iterator[Layer]:
        for layer in self.layers:
            yield layer
