import photoshop as ps

# Get photoshop instance.
app = ps.Application()

# Add new document and set name to "Example for move to End."
active_document = app.documents.add(name="Example for move to End.")

# Add a new layer set.
group_layer = active_document.layerSets.add()
# Add a layer in the group.
layer = group_layer.artLayers.add()
layer.name = "This is a child layer."
# Add a new layer in this active document top.
top_layer = active_document.artLayers.add()
top_layer.name = "This is a top layer."
top_layer.moveToEnd(group_layer)
