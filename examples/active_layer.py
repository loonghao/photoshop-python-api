# Set the active layer to the last art layer of the active document, or the
# first if the last is already active.

from photoshop import Session

with Session() as ps:
    if len(ps.app.documents) < 1:
        docRef = ps.app.documents.add()
    else:
        docRef = ps.app.activeDocument

    if len(docRef.layers) < 2:
        docRef.artLayers.add()

    print(docRef.activeLayer.name)
    print(docRef.layers.item(len(docRef.layers)))
    new_layer = docRef.artLayers.add()
    print(new_layer.name)
    new_layer.name = "test"
