"""This script demonstrates how you can use the action manager to execute the Crystallize filter.

In order to find all the IDs, see https://helpx.adobe.com/photoshop/kb/downloadable-plugins-and-content.html#ScriptingListenerplugin # noqa: E501
This blog here explains what a script listener is http://blogs.adobe.com/crawlspace/2006/05/installing_and_1.html

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyCrystallizeFilterAction.py."""

# Import third-party modules
from __future__ import annotations

# Import local modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session

PSD_FILE = psd.get_psd_files()

with Session(PSD_FILE["layer_comps.psd"], "open") as ps:
    app = ps.app
    active_document = ps.active_document
    nLayerSets = active_document.layerSets
    ps.echo(f"The total amount of current layerSet (Group) is {len(nLayerSets)}.")
    nArtLayers = active_document.layerSets.item(len(nLayerSets)).artLayers
    active_document.activeLayer = active_document.layerSets.item(len(nLayerSets)).artLayers.item(len(nArtLayers))

    def applyCrystallize(cellSize: int) -> None:
        cellSizeID = ps.app.CharIDToTypeID("ClSz")
        eventCrystallizeID = ps.app.CharIDToTypeID("Crst")
        filterDistID = ps.app.CharIDToTypeID("FlDt")
        nullID = ps.app.CharIDToTypeID("null")
        desc = ps.ActionDescriptor
        ref = ps.ActionReference
        filterDistortNS = ps.app.StringIDToTypeID("filterDistort")

        # Create a reference for Crystallize
        ref1 = ref()
        ref1.putClass(eventCrystallizeID)
        desc1 = desc()
        desc1.putReference(nullID, ref1)
        desc1.putInteger(cellSizeID, cellSize)
        app.executeAction(filterDistortNS, desc1)

    applyCrystallize(25)
    ps.echo("Apply crystallize done.")
