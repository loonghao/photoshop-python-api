# This script demonstrates how you can use the action manager
# to execute the Emboss filter.
import os
from photoshop import Application
from photoshop import ActionDescriptor
from photoshop import Adobe

# Start up Photoshop application
# Or get Reference to already running Photoshop application instance
# app = Dispatch('Photoshop.Application')
app = Application()

fileName = os.path.join(os.path.dirname(__file__), 'Layer Comps.psd')
docRef = app.open(fileName)

nlayerSets = docRef.layerSets
nArtLayers = docRef.layerSets.item(len(nlayerSets)).artLayers

docRef.activeLayer = docRef.layerSets.item(len(nlayerSets)).activeLayer.item(
    len(nArtLayers))


def SmartSharpen(inAmount, inRadius, inNoise):
    idsmart_sharpen_id = app.stringIDToTypeID(Adobe.smartSharpen)
    desc37 = ActionDescriptor()

    idpresetKind = app.stringIDToTypeID(Adobe.presetKind)
    idpresetKindType = app.stringIDToTypeID(Adobe.presetKindType)
    idpresetKindCustom = app.stringIDToTypeID(Adobe.presetKindCustom)
    desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)

    idAmnt = app.charIDToTypeID(Adobe.AMNT)
    idPrc = app.charIDToTypeID(Adobe.RDS)
    desc37.putUnitDouble(idAmnt, idPrc, inAmount)

    idRds = app.charIDToTypeID(Adobe.RDS)
    idPxl = app.charIDToTypeID(Adobe.PX1)
    desc37.putUnitDouble(idRds, idPxl, inRadius)

    idnoiseReduction = app.stringIDToTypeID(Adobe.noiseReduction)
    idPrc = app.charIDToTypeID(Adobe.PRC)
    desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

    idblur = app.charIDToTypeID(Adobe.blur)
    idblurType = app.stringIDToTypeID(Adobe.blurType)
    idGsnB = app.charIDToTypeID(Adobe.GSNB)
    desc37.putEnumerated(idblur, idblurType, idGsnB)

    # now execute the action
    app.ExecuteAction(idsmart_sharpen_id, desc37)


SmartSharpen(300, 2.0, 20)
