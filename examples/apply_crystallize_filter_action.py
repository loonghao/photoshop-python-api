"""Demonstrate how to apply the Crystallize filter using Photoshop's Action Manager.

This example shows how to:
1. Use Photoshop's Action Manager to apply filters
2. Work with layer sets and art layers
3. Execute complex filter operations using action descriptors

The script applies the Crystallize filter to the last art layer in the last layer set
of the document. It uses Photoshop's Action Manager system to execute the filter,
which requires specific IDs and descriptors.

Example:
    ```python
    def applyCrystallize(cellSize):
        # Create action descriptor and reference
        desc = ps.ActionDescriptor
        ref = ps.ActionReference()
        ref.putClass(ps.app.CharIDToTypeID("Crst"))
        
        # Set filter parameters
        desc1 = desc()
        desc1.putReference(nullID, ref)
        desc1.putInteger(cellSizeID, cellSize)
        
        # Execute the filter
        app.executeAction(filterDistortNS, desc1)
    ```

References:
    - Photoshop Scripting Listener Plugin:
      https://helpx.adobe.com/photoshop/kb/downloadable-plugins-and-content.html#ScriptingListenerplugin
    - Script Listener Guide:
      http://blogs.adobe.com/crawlspace/2006/05/installing_and_1.html
    - Based on:
      https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyCrystallizeFilterAction.py

Note:
    The Script Listener plugin is essential for finding action IDs when developing
    similar scripts. It records all actions performed in Photoshop as JavaScript code.
"""

# Import third-party modules
from __future__ import annotations

# Import local modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session

# Get sample PSD file path
PSD_FILE = psd.get_psd_files()

# Open the PSD file in Photoshop
with Session(PSD_FILE["layer_comps.psd"], "open") as ps:
    app = ps.app
    active_document = ps.active_document
    
    # Get all layer sets (groups) in the document
    nLayerSets = active_document.layerSets
    ps.echo(f"The total amount of current layerSet (Group) is {len(nLayerSets)}.")
    
    # Get art layers from the last layer set
    nArtLayers = active_document.layerSets.item(len(nLayerSets)).artLayers
    
    # Set the last art layer in the last layer set as active
    active_document.activeLayer = active_document.layerSets.item(len(nLayerSets)).artLayers.item(len(nArtLayers))

    def applyCrystallize(cellSize: int) -> None:
        """Apply the Crystallize filter to the active layer.
        
        Args:
            cellSize: The size of the crystallize cells (1-300).
        """
        # Define action IDs
        cellSizeID = ps.app.CharIDToTypeID("ClSz")
        eventCrystallizeID = ps.app.CharIDToTypeID("Crst")
        ps.app.CharIDToTypeID("FlDt")
        nullID = ps.app.CharIDToTypeID("null")
        desc = ps.ActionDescriptor
        ref = ps.ActionReference
        filterDistortNS = ps.app.StringIDToTypeID("filterDistort")

        # Create a reference for the Crystallize filter
        ref1 = ref()
        ref1.putClass(eventCrystallizeID)
        
        # Set up the filter parameters
        desc1 = desc()
        desc1.putReference(nullID, ref1)
        desc1.putInteger(cellSizeID, cellSize)
        
        # Execute the Crystallize filter
        app.executeAction(filterDistortNS, desc1)

    # Apply the Crystallize filter with cell size 25
    applyCrystallize(25)
    ps.echo("Apply crystallize done.")
