"""
References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ActiveLayer.py

"""
import photoshop as ps

app = ps.Application()

if app.documents.length < 1:
    docRef = app.documents.add()
else:
    docRef = app.activeDocument

if docRef.layers.length < 2:
    docRef.artLayers.add()

activeLayerName = docRef.activeLayer.name
if docRef.activeLayer.name != docRef.layers.item(docRef.layers.length).name:
    docRef.activeLayer = docRef.layers.item(docRef.layers.length)
else:
    docRef.activeLayer = docRef.layers.item(1)
