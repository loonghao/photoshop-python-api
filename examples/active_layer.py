"""Demonstrate how to work with active layers in Photoshop.

This example shows how to:
1. Create a new document if none exists
2. Add new art layers to the document
3. Get and set the active layer
4. Rename layers

Example:
    ```python
    with Session() as ps:
        docRef = ps.app.documents.add()  # Create new document
        new_layer = docRef.artLayers.add()  # Add new layer
        new_layer.name = "test"  # Rename layer
    ```

Note:
    The script will create a new document if none exists,
    and will add a new layer if the document has less than 2 layers.
"""

# Import built-in modules
from __future__ import annotations

# Import local modules
from photoshop import Session

# Create a new Photoshop session
with Session() as ps:
    # Create a new document if none exists
    if len(ps.app.documents) < 1:
        docRef = ps.app.documents.add()
    else:
        docRef = ps.app.activeDocument

    # Add a new layer if document has less than 2 layers
    if len(docRef.layers) < 2:
        docRef.artLayers.add()

    # Print the name of the current active layer
    ps.echo(docRef.activeLayer.name)
    
    # Create a new art layer and make it active
    new_layer = docRef.artLayers.add()
    ps.echo(new_layer.name)
    
    # Rename the new layer
    new_layer.name = "test"
