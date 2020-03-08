# Set the active layer to the last art layer of the active document, or the
# first if the last is already active.


import photoshop as ps

app = ps.Application()
if app.documents.length < 1:
    docRef = app.documents.add()
else:
    docRef = app.activeDocument

if docRef.layers.length < 2:
    docRef.artLayers.add()


print(docRef.activeLayer.name)
print(docRef.layers.item(docRef.layers.length))
# Set current active to first layer.
# docRef.activeLayer = docRef.layers.item(1)
new_layer = docRef.artLayers.add()
print(new_layer.name)
new_layer.name = "test"

