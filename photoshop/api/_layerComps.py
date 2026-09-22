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
        comment: str = "",
        appearance: bool = True,
        position: bool = True,
        visibility: bool = True,
        childLayerCompStat: bool = False,
    ) -> LayerComp:
        len_before = self.length
        # For some reason the self.app.add returns the first layer comp,
        # which might not be the new one, so we have to get the new comp in a roundabout way.
        self.app.add(name, comment, appearance, position, visibility, childLayerCompStat)
        return self[len_before + 1]
