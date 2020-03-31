from photoshop._core import Photoshop
from photoshop.artlayer import ArtLayer
from photoshop.layer import Layer


class Layers(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return list(self.app)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        item = self._layers[key]
        try:
            # If have text item will be return ArtLayer.
            item.textItem
            return ArtLayer(item)
        except:
            return Layer(self._layers[key])

    @property
    def length(self):
        return len(self._layers)

    def removeAll(self):
        return [layer.name for layer in self.app]

    def item(self, index):
        return ArtLayer(self.app.item(index))

    def __iter__(self):
        for layer in self._layers:
            if layer.kind == "1":
                yield Layer(layer)
            else:
                yield ArtLayer(layer)
