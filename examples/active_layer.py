"""Example of working with active layers in Photoshop.

This example demonstrates how to:
1. Get and set the active layer in a document
2. Create new art layers
3. Manage layer names and properties

The script will:
- Create a new document if none exists
- Add a new art layer if document has less than 2 layers
- Display the current active layer name
- Create a new layer and rename it
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Get or create a document
    if len(ps.app.documents) < 1:
        docRef = ps.app.documents.add()
    else:
        docRef = ps.app.activeDocument

    # Ensure we have at least 2 layers
    if len(docRef.layers) < 2:
        docRef.artLayers.add()

    # Display current active layer name
    ps.echo(docRef.activeLayer.name)
    
    # Create and rename a new layer
    new_layer = docRef.artLayers.add()
    ps.echo(new_layer.name)
    new_layer.name = "test"
