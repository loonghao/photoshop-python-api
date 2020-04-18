"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

import os

from photoshop import Session

fileName = os.path.join(os.path.dirname(__file__), "layer_comps.psd")

with Session(fileName, action="open") as ps:

    def SmartSharpen(inAmount, inRadius, inNoise):
        idsmart_sharpen_id = ps.app.stringIDToTypeID(ps.smartSharpen)
        desc37 = ps.ActionDescriptor()

        idpresetKind = ps.app.stringIDToTypeID(ps.presetKind)
        idpresetKindType = ps.app.stringIDToTypeID(ps.presetKindType)
        idpresetKindCustom = ps.app.stringIDToTypeID(ps.presetKindCustom)
        desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)

        idAmnt = ps.app.charIDToTypeID(ps.AMNT)
        idPrc = ps.app.charIDToTypeID(ps.RDS)
        desc37.putUnitDouble(idAmnt, idPrc, inAmount)

        idRds = ps.app.charIDToTypeID(ps.RDS)
        idPxl = ps.app.charIDToTypeID(ps.PX1)
        desc37.putUnitDouble(idRds, idPxl, inRadius)

        idnoiseReduction = ps.app.stringIDToTypeID(ps.noiseReduction)
        idPrc = ps.app.charIDToTypeID(ps.PRC)
        desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

        idblur = ps.app.charIDToTypeID(ps.blur)
        idblurType = ps.app.stringIDToTypeID(ps.blurType)
        idGsnB = ps.app.charIDToTypeID(ps.GSNB)
        desc37.putEnumerated(idblur, idblurType, idGsnB)

        ps.app.ExecuteAction(idsmart_sharpen_id, desc37)

    docRef = ps.active_document
    nlayerSets = docRef.layerSets
    nArtLayers = docRef.layerSets.item(nlayerSets.length)
    docRef.activeLayer = nArtLayers.artLayers.item(nArtLayers.artLayers.length)

    SmartSharpen(300, 2.0, 20)
