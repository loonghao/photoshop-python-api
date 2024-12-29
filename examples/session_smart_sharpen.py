"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

# Import third-party modules
from __future__ import annotations

import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session

PSD_FILE = psd.get_psd_files()
file_path = PSD_FILE["layer_comps.psd"]

with Session(file_path, action="open") as ps:

    def SmartSharpen(inAmount, inRadius, inNoise):
        idsmart_sharpen_id = ps.app.stringIDToTypeID(ps.EventID.SmartSharpen)
        desc37 = ps.ActionDescriptor()

        idpresetKind = ps.app.stringIDToTypeID(ps.EventID.PresetKind)
        idpresetKindType = ps.app.stringIDToTypeID(ps.EventID.PresetKindType)
        idpresetKindCustom = ps.app.stringIDToTypeID(ps.EventID.PresetKindCustom)
        desc37.putEnumerated(idpresetKind, idpresetKindType, idpresetKindCustom)
        idAmnt = ps.app.charIDToTypeID("Amnt")
        idPrc = ps.app.charIDToTypeID("Rds ")
        desc37.putUnitDouble(idAmnt, idPrc, inAmount)

        idRds = ps.app.charIDToTypeID("Rds ")
        idPxl = ps.app.charIDToTypeID("#Pxl")
        desc37.putUnitDouble(idRds, idPxl, inRadius)

        idnoiseReduction = ps.app.stringIDToTypeID("noiseReduction")
        idPrc = ps.app.charIDToTypeID("#Prc")
        desc37.putUnitDouble(idnoiseReduction, idPrc, inNoise)

        idblur = ps.app.charIDToTypeID("blur")
        idblurType = ps.app.stringIDToTypeID("blurType")
        idGsnB = ps.app.charIDToTypeID("GsnB")
        desc37.putEnumerated(idblur, idblurType, idGsnB)

        ps.app.ExecuteAction(idsmart_sharpen_id, desc37)

    docRef = ps.active_document
    nlayerSets = docRef.layerSets
    nArtLayers = docRef.layerSets.item(nlayerSets.length)
    docRef.activeLayer = nArtLayers.artLayers.item(nArtLayers.artLayers.length)

    SmartSharpen(300, 2.0, 20)
