"""Convert Smart object to artLayer."""

# Import local modules
from __future__ import annotations

from photoshop import Session

# example 1
with Session() as ps:
    js = """
var idplacedLayerConvertToLayers = stringIDToTypeID( "placedLayerConvertToLayers" );
executeAction( idplacedLayerConvertToLayers, undefined, DialogModes.NO );
"""
    ps.app.doJavaScript(js)

# example 2
with Session() as ps:
    descriptor = ps.ActionDescriptor
    idplacedLayerConvertToLayers = ps.app.stringIDToTypeID("placedLayerConvertToLayers")
    ps.app.executeAction(idplacedLayerConvertToLayers, descriptor)
