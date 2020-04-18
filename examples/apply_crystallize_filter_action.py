""" This script demonstrates how you can use the action manager

to execute the Crystallize filter.
In order to find all the IDs, see https://helpx.adobe.com/photoshop/kb/downloadable-plugins-and-content.html#ScriptingListenerplugin
This blog here explains what a script listener is http://blogs.adobe.com/crawlspace/2006/05/installing_and_1.html

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyCrystallizeFilterAction.py

"""


import os

from photoshop import Session

fileName = os.path.join(os.path.dirname(__file__), "layer_comps.psd")

with Session(fileName, "open") as ps:
    nLayerSets = ps.active_document.layerSets
    print(len(nLayerSets))
    nArtLayers = ps.active_document.layerSets.item(len(nLayerSets)).artLayers

    # get the last layer in LayerSets
    ps.active_document.activeLayer = ps.active_document.layerSets.item(
        len(nLayerSets)
    ).artLayers.item(len(nArtLayers))

    def applyCrystallize(cellSize):
        cellSizeID = ps.app.CharIDToTypeID("ClSz")
        eventCrystallizeID = ps.app.CharIDToTypeID("Crst")

        filterDescriptor = ps.ActionDescriptor
        filterDescriptor.putInteger(cellSizeID, cellSize)

        ps.app.executeAction(eventCrystallizeID, filterDescriptor)

    applyCrystallize(25)
