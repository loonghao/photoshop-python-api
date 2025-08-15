# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._layerComp import LayerComp
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables


class LayerComps(
    CollectionOfRemovables[LayerComp, int | str],
    CollectionOfNamedObjects[LayerComp, int | str],
):
    """The layer comps collection in this document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(LayerComp, parent=parent)
        self._flag_as_method("add")

    def add(
        self,
        name: str,
        comment: str = "No Comment.",
        appearance: bool = True,
        position: bool = True,
        visibility: bool = True,
        childLayerCompStat: bool = False,
    ) -> LayerComp:
        return LayerComp(self.app.add(name, comment, appearance, position, visibility, childLayerCompStat))
