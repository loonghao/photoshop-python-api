# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._layerSet import LayerSet
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


class LayerSets(
    CollectionWithAdd[LayerSet, int | str],
    CollectionOfRemovables[LayerSet, int | str],
    CollectionOfNamedObjects[LayerSet, int | str],
):
    """The layer sets collection in the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(LayerSet, parent)
