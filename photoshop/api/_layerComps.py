# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._layerComp import LayerComp
from photoshop.api.errors import PhotoshopPythonAPIError


class LayerComps(Photoshop):
    """The layer comps collection in this document."""

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
            "removeAll",
        )

    def __len__(self):
        return self.length

    @property
    def length(self):
        return len(self._layers)

    @property
    def _layers(self):
        return list(self.app)

    @property
    def parent(self):
        return self.app.parent

    @property
    def typename(self):
        return self.app.typename

    def add(
        self,
        name,
        comment="No Comment.",
        appearance=True,
        position=True,
        visibility=True,
        childLayerCompStat=False,
    ):
        return LayerComp(self.app.add(name, comment, appearance, position, visibility, childLayerCompStat))

    def getByName(self, name):
        for layer in self._layers:
            if layer.name == name:
                return LayerComp(layer)
        raise PhotoshopPythonAPIError(f'Could not find a layer named "{name}"')

    def removeAll(self):
        self.app.removeAll()

    def __iter__(self):
        for layer in self._layers:
            yield LayerComp(layer)
