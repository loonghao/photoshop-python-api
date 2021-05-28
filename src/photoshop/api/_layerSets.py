# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._layerSet import LayerSet
from photoshop.api.errors import PhotoshopPythonAPIError


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

    def removeAll(self):
        self.app.removeAll()

    def getByName(self, name):
        for layer in self.app:
            if name == layer.name:
                return LayerSet(layer)
        raise PhotoshopPythonAPIError(f'Could not find a LayerSet named "{name}"')
