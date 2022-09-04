""" This script demonstrates how you can use the action manager

to execute the Crystallize filter.
In order to find all the IDs, see https://helpx.adobe.com/photoshop/kb/downloadable-plugins-and-content.html#ScriptingListenerplugin # noqa: E501
This blog here explains what a script listener is http://blogs.adobe.com/crawlspace/2006/05/installing_and_1.html

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyCrystallizeFilterAction.py

Now the submodule action_manager provides a more friendly way to deal with action manager.
Read document for details.
"""

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session
import photoshop.api.action_manager as am


PSD_FILE = psd.get_psd_files()

with Session(PSD_FILE["layer_comps.psd"], "open") as ps:
    active_document = ps.active_document
    nLayerSets = active_document.layerSets
    print(f"The total amount of current layerSet (Group) is " f"{len(nLayerSets)}.")
    nArtLayers = active_document.layerSets.item(len(nLayerSets)).artLayers

    # get the last layer in LayerSets
    active_document.activeLayer = active_document.layerSets.item(len(nLayerSets)).artLayers.item(len(nArtLayers))

    def applyCrystallize(cellSize):
        filter_dict = {"_classID": None, "ClSz": cellSize}
        filter_desc = ps.ActionDescriptor.load(filter_dict)
        ps.app.executeAction(am.str2id("Crst"), filter_desc)

    applyCrystallize(25)
    print("Apply crystallize done.")
