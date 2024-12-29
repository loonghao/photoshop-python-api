"""Demonstrate copy and paste operations in Photoshop.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/CopyAndPaste.py."""

# Import local modules
from __future__ import annotations

import examples._psd_files as psd  # Import from examples.
from photoshop import Session

PSD_FILE = psd.get_psd_files()

with Session() as ps:
    app = ps.app
    startRulerUnits = app.preferences.rulerUnits
    if startRulerUnits != ps.Units.Pixels:
        app.preferences.rulerUnits = ps.Units.Pixels

    docRef = app.open(PSD_FILE["layer_comps.psd"])
    nLayerSets = len(docRef.layerSets)
    nArtLayers = len(docRef.layerSets.item(nLayerSets).artLayers)
    docRef.activeLayer = docRef.layerSets.item(nLayerSets).artLayers.item(nArtLayers)

    if docRef.activeLayer.kind != ps.LayerKind.TextLayer:
        # Select the left half of the document. Selections are always expressed
        # in pixels regardless of the current ruler unit type, so we're computing
        # the selection corner points based on the inch unit width and height
        # of the document
        x2 = (docRef.width * docRef.resolution) / 2
        y2 = docRef.height * docRef.resolution

        sel_area = ((0, 0), (x2, 0), (x2, y2), (0, y2))
        docRef.selection.select(sel_area, ps.SelectionType.ReplaceSelection, 0, False)

        docRef.selection.copy()

        # The new doc is created
        # need to change ruler units to pixels because x2 and y2 are pixel units.
        pasteDoc = app.documents.add(x2, y2, docRef.resolution, "Paste Target")
        pasteDoc.paste()
    else:
        ps.echo("You cannot copy from a text layer")

    if startRulerUnits != app.preferences.rulerUnits:
        app.preferences.rulerUnits = startRulerUnits
