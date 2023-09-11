# Import local modules
from photoshop.api._channel import Channel
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods
class Channels(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
            "removeAll",
        )

    @property
    def _channels(self):
        return list(self.app)

    def __len__(self):
        return self.length

    def __iter__(self):
        for layer in self.app:
            yield layer

    def __getitem__(self, item):
        return self.app[item]

    @property
    def length(self):
        return len(self._channels)

    def add(self):
        self.app.add()

    def removeAll(self):
        self.app.removeAll()

    def getByName(self, name) -> Channel:
        for channel in self._channels:
            if channel.name == name:
                return Channel(channel)
        raise PhotoshopPythonAPIError(f'Could not find a channel named "{name}"')
