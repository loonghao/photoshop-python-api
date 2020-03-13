"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

import os
from photoshop import Session


fileName = os.path.join(os.path.dirname(__file__), 'layer_comps.psd')

with Session(fileName) as adobe:
    nlayerSets = adobe.active_document.layerSets
    nArtLayers = adobe.active_document.layerSets.item(nlayerSets.length)
    adobe.active_document.activeLayer = nArtLayers.artLayers.item(nArtLayers.artLayers.length)


    def SmartSharpen(inAmount, inRadius, inNoise):
        idsmart_sharpen_id = adobe.app.stringIDToTypeID(adobe.smartSharpen)
        desc37 = adobe.ActionDescriptor()

        idpresetKind = adobe.app.stringIDToTypeID(adobe.presetKind)
        idpresetKindType = adobe.app.stringIDToTypeID(adobe.presetKindType)
        idpresetKindCustom = adobe.app.stringIDToTypeID(adobe.presetKindCustom)
        desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)

        idAmnt = adobe.app.charIDToTypeID(adobe.AMNT)
        idPrc = adobe.app.charIDToTypeID(adobe.RDS)
        desc37.putUnitDouble(idAmnt, idPrc, inAmount)

        idRds = adobe.app.charIDToTypeID(adobe.RDS)
        idPxl = adobe.app.charIDToTypeID(adobe.PX1)
        desc37.putUnitDouble(idRds, idPxl, inRadius)

        idnoiseReduction = adobe.app.stringIDToTypeID(adobe.noiseReduction)
        idPrc = adobe.app.charIDToTypeID(adobe.PRC)
        desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

        idblur = adobe.app.charIDToTypeID(adobe.blur)
        idblurType = adobe.app.stringIDToTypeID(adobe.blurType)
        idGsnB = adobe.app.charIDToTypeID(adobe.GSNB)
        desc37.putEnumerated(idblur, idblurType, idGsnB)

        adobe.app.ExecuteAction(idsmart_sharpen_id, desc37)


    SmartSharpen(300, 2.0, 20)
