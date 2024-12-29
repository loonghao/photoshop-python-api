from __future__ import annotations

import photoshop.api as ps

app = ps.Application()
doc = app.activeDocument
for layer in doc.layerSets:
    for i in layer.layers:
        print(i.typename, i.name)
