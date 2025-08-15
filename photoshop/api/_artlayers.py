# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


# pylint: disable=too-many-public-methods
class ArtLayers(
    CollectionOfRemovables[ArtLayer, int | str],
    CollectionOfNamedObjects[ArtLayer, int | str],
    CollectionWithAdd[ArtLayer, int | str],
):
    """The collection of art layer objects in the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(ArtLayer, parent)
