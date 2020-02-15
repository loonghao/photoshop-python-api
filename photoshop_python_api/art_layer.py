# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api.text_item import TextItem


class ArtLayer(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def _layers(self):
        return [layerset for layerset in self.app]

    def __len__(self):
        return self.length

    @property
    def kind(self):
        return self.app.kind

    @kind.setter
    def kind(self, value):
        self.app.kind = value

    @property
    def textItem(self):
        return TextItem(self.app.textItem)

    @textItem.setter
    def textItem(self, value):
        self.app.textItem = value

    @property
    def fillOpacity(self):
        return self.app.fillOpacity

    @property
    def length(self):
        return len(self._layers)

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.Typename

    def add(self):
        return self.app.add()

    def get_by_name(self, name):
        return self.app.getByName(name)

    def remove_all(self):
        return self.app.RemoveAll()

    def applyAddNoise(self, amount, distribution, monochromatic):
        return self.app.applyAddNoise(amount, distribution, monochromatic)
