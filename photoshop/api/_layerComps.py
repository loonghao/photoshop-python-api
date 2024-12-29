# Import local modules
from __future__ import annotations

from typing import Any

from photoshop.api._collection_base import CollectionBase
from photoshop.api._layerComp import LayerComp
from photoshop.api.errors import PhotoshopPythonAPIError


class LayerComps(CollectionBase[LayerComp]):
    """The layer comps collection in this document.
    
    This class represents a collection of layer compositions in a Photoshop document.
    Layer comps are snapshots of the state of the Layers palette. Layer comps save
    layer visibility and position states.
    
    It provides methods to:
    - Add new layer comps
    - Access layer comps by index or name
    - Remove layer comps
    - Iterate over layer comps
    """

    def add(
        self,
        name: str,
        comment: str = "No Comment.",
        appearance: bool = True,
        position: bool = True,
        visibility: bool = True,
        childLayerCompStat: bool = False,
    ) -> LayerComp:
        """Add a new layer comp to the document.
        
        Args:
            name: The name of the layer comp
            comment: The description of the layer comp
            appearance: If true, save the layer appearance
            position: If true, save the layer position
            visibility: If true, save the layer visibility
            childLayerCompStat: If true, save the child layer comp state
            
        Returns:
            LayerComp: The newly created layer comp
        """
        return self._wrap_item(
            self.app.add(
                name,
                comment,
                appearance,
                position,
                visibility,
                childLayerCompStat,
            ),
        )

    def getByName(self, name: str) -> LayerComp:
        """Get the first layer comp with the specified name.
        
        Args:
            name: The name of the layer comp to find
            
        Returns:
            LayerComp: The layer comp with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no layer comp with the specified name is found
        """
        for layer_comp in self:
            if layer_comp.name == name:
                return layer_comp
        raise PhotoshopPythonAPIError(f'Could not find a layer comp named "{name}"')

    def removeAll(self) -> None:
        """Delete all layer comps in the collection."""
        self.app.removeAll()

    def _wrap_item(self, item: Any) -> LayerComp:
        """Wrap a COM layer comp object in a LayerComp instance.
        
        Args:
            item: The COM layer comp object to wrap
            
        Returns:
            LayerComp: The wrapped layer comp
        """
        return LayerComp(item)
