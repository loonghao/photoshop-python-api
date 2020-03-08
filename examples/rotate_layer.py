"""This scripts demonstrates how to rotate a layer 45 degrees clockwise.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/RotateLayer.py

"""

import photoshop as ps

app = ps.Application()

if len(app.documents) > 0:
    print(app.activeDocument.activeLayer.typename)
    if not app.activeDocument.activeLayer.isBackgroundLayer:
        docRef = app.activeDocument
        layerRef = docRef.layers[0]
        layerRef.rotate(45.0)
    else:
        print("Operation cannot be performed on background layer")
else:
    print("You must have at least one open document to run this script!")
