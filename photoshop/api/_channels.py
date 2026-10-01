# Import future modules
from __future__ import annotations

# Import built-in modules
from typing import Union

# Import local modules
from photoshop.api._channel import Channel
from photoshop.api._core import Photoshop
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


class Channels(
    CollectionWithAdd[Channel, Union[int, str]],
    CollectionOfRemovables[Channel, Union[int, str]],
    CollectionOfNamedObjects[Channel, Union[int, str]],
):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(Channel, parent=parent)
