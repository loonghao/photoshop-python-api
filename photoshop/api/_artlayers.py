# Import future modules
from __future__ import annotations

# Import built-in modules
from typing import Union

# Import local modules
from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


# pylint: disable=too-many-public-methods
class ArtLayers(
    CollectionOfRemovables[ArtLayer, Union[int, str]],
    CollectionOfNamedObjects[ArtLayer, Union[int, str]],
    CollectionWithAdd[ArtLayer, Union[int, str]],
):
    """The collection of art layer objects in the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(ArtLayer, parent)
