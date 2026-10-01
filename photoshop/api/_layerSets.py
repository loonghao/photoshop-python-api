# Import future modules
from __future__ import annotations

# Import built-in modules
from typing import Union

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._layerSet import LayerSet
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


class LayerSets(
    CollectionWithAdd[LayerSet, Union[int, str]],
    CollectionOfRemovables[LayerSet, Union[int, str]],
    CollectionOfNamedObjects[LayerSet, Union[int, str]],
):
    """The layer sets collection in the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(LayerSet, parent)
