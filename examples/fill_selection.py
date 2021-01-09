# Fill the current selection with an RGB color.


from photoshop import Session

with Session() as ps:
    start_ruler_units = ps.app.Preferences.RulerUnits

    if len(ps.app.documents) < 1:
        if start_ruler_units is not ps.Units.Pixels:
            ps.app.Preferences.RulerUnits = ps.Units.Pixels
        docRef = ps.app.documents.add(
            320, 240, 72, None, ps.NewDocumentMode.NewRGB, ps.DocumentFill.White
        )
        docRef.artLayers.add()
        ps.app.preferences.rulerUnits = start_ruler_units

    if not ps.active_document.activeLayer.isBackgroundLayer:
        selRef = ps.active_document.selection
        fillcolor = ps.SolidColor()
        fillcolor.rgb.red = 225
        fillcolor.rgb.green = 0
        fillcolor.rgb.blue = 0
        selRef.fill(fillcolor, ps.ColorBlendMode.NormalBlendColor, 25, False)
    else:
        ps.echo("Can't perform operation on background layer.")
