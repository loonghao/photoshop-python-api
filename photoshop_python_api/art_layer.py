# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api.text_item import TextItem


class ArtLayer(Photoshop):
    def __init__(self, parent):
        super(ArtLayer, self).__init__(parent=parent)

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
        return self.app.artLayer.fillOpacity

    @property
    def length(self):
        return self.art_layers.length

    @property
    def parent(self):
        return self.art_layers.parent

    @property
    def typename(self):
        return self.art_layers.Typename

    def add(self):
        return self.art_layers.add()

    def get_by_name(self, name):
        return self.art_layers.getByName(name)

    def remove_all(self):
        return self.art_layers.RemoveAll()
