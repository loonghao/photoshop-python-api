from ._core import Photoshop
from .errors import PhotoshopPythonAPIError
from ._layerSet import LayerSet


class LayerSets(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        return LayerSet(self._layerSets[key])

    @property
    def _layerSets(self):
        return list(self.app)

    @property
    def length(self):
        return len(self._layerSets)

    def add(self):
        return LayerSet(self.app.add())

    def item(self, index):
        return LayerSet(self.app.item(index))

    def getByName(self, name):
        for layer in self.app:
            if name == layer.name:
                return LayerSet(layer)
        raise PhotoshopPythonAPIError("Could not find a LayerSet named "
                                      f'"{name}"')
