# Import local modules
from photoshop.api._channel import Channel
from photoshop.api._core import Photoshop
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd


class Channels(
    CollectionWithAdd[Channel, int | str],
    CollectionOfRemovables[Channel, int | str],
    CollectionOfNamedObjects[Channel, int | str],
):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(Channel, parent=parent)
