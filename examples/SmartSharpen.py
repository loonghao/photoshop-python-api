"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

import os
import photoshop as ps


app = ps.Application()

fileName = os.path.join(os.path.dirname(__file__), 'layer_comps.psd')
docRef = app.open(fileName)

nlayerSets = docRef.layerSets
nArtLayers = docRef.layerSets.item(nlayerSets.length)
docRef.activeLayer = nArtLayers.artLayers.item(nArtLayers.artLayers.length)


def SmartSharpen(inAmount, inRadius, inNoise):
    idsmart_sharpen_id = app.stringIDToTypeID(ps.smartSharpen)
    desc37 = ps.ActionDescriptor()

    idpresetKind = app.stringIDToTypeID(ps.presetKind)
    idpresetKindType = app.stringIDToTypeID(ps.presetKindType)
    idpresetKindCustom = app.stringIDToTypeID(ps.presetKindCustom)
    desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)

    idAmnt = app.charIDToTypeID(ps.AMNT)
    idPrc = app.charIDToTypeID(ps.RDS)
    desc37.putUnitDouble(idAmnt, idPrc, inAmount)

    idRds = app.charIDToTypeID(ps.RDS)
    idPxl = app.charIDToTypeID(ps.PX1)
    desc37.putUnitDouble(idRds, idPxl, inRadius)

    idnoiseReduction = app.stringIDToTypeID(ps.noiseReduction)
    idPrc = app.charIDToTypeID(ps.PRC)
    desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

    idblur = app.charIDToTypeID(ps.blur)
    idblurType = app.stringIDToTypeID(ps.blurType)
    idGsnB = app.charIDToTypeID(ps.GSNB)
    desc37.putEnumerated(idblur, idblurType, idGsnB)

    app.ExecuteAction(idsmart_sharpen_id, desc37)


SmartSharpen(300, 2.0, 20)
