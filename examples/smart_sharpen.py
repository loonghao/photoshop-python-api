"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
import photoshop.api as ps


app = ps.Application()

PSD_FILE = psd.get_psd_files()
file_path = PSD_FILE["layer_comps.psd"]
docRef = app.open(file_path)

nlayerSets = docRef.layerSets
nArtLayers = docRef.layerSets.item(nlayerSets.length)
docRef.activeLayer = nArtLayers.artLayers.item(nArtLayers.artLayers.length)


def SmartSharpen(inAmount, inRadius, inNoise):
    idsmart_sharpen_id = app.stringIDToTypeID(ps.EventID.SmartSharpen)
    desc37 = ps.ActionDescriptor()

    idpresetKind = app.stringIDToTypeID(ps.EventID.PresetKind)
    idpresetKindType = app.stringIDToTypeID(ps.EventID.PresetKindType)
    idpresetKindCustom = app.stringIDToTypeID(ps.EventID.PresetKindCustom)
    desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)

    idAmnt = app.charIDToTypeID("Amnt")
    idPrc = app.charIDToTypeID("Rds ")
    desc37.putUnitDouble(idAmnt, idPrc, inAmount)

    idRds = app.charIDToTypeID("Rds ")
    idPxl = app.charIDToTypeID("#Pxl")
    desc37.putUnitDouble(idRds, idPxl, inRadius)

    idnoiseReduction = app.stringIDToTypeID("noiseReduction")
    idPrc = app.charIDToTypeID("#Prc")
    desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

    idblur = app.charIDToTypeID("blur")
    idblurType = app.stringIDToTypeID("blurType")
    idGsnB = app.charIDToTypeID("GsnB")
    desc37.putEnumerated(idblur, idblurType, idGsnB)

    app.ExecuteAction(idsmart_sharpen_id, desc37)


SmartSharpen(300, 2.0, 20)
