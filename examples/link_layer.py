import photoshop as ps

app = ps.Application()

start_ruler_units = app.preferences.rulerUnits

if len(app.documents) < 1:
    if start_ruler_units is not ps.Units.Pixels:
        app.preferences.rulerUnits = ps.Units.Pixels
    docRef = app.documents.add(
        320, 240, 72, None, ps.NewDocumentMode.NewRGB, ps.DocumentFill.BackgroundColor,
    )
else:
    docRef = app.activeDocument

layerRef = docRef.artLayers.add()
layerRef2 = docRef.artLayers.add()
layerRef.link(layerRef2)

# Set the ruler back to where it was
app.preferences.rulerUnits = start_ruler_units
