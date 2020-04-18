"""Create a stroke around the current selection, Set the stroke color and
width of the new stroke.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SelectionStroke.py

"""

import photoshop as ps

app = ps.Application()

if len(list((i, x) for i, x in enumerate(app.documents, 1))) > 0:
    if not app.activeDocument.activeLayer.isBackgroundLayer:
        psPixels = 1
        start_ruler_units = app.Preferences.RulerUnits
        app.preferences.rulerUnits = ps.Units.Pixels

        selRef = app.activeDocument.selection
        offset = 10
        selBounds = (
            (offset, offset),
            (app.activeDocument.width - offset, offset),
            (app.activeDocument.width - offset, app.activeDocument.height - offset),
            (offset, app.activeDocument.height - offset),
        )

        selRef.select(selBounds)
        selRef.selectBorder(5)

        # create text color properties
        strokeColor = ps.SolidColor()

        strokeColor.cmyk.cyan = 58
        strokeColor.cmyk.magenta = 0
        strokeColor.cmyk.yellow = 70
        strokeColor.cmyk.black = 0
        app.displayDialogs = ps.DialogModes.DisplayNoDialogs
        selRef.stroke(
            strokeColor,
            2,
            ps.StrokeLocation.OutsideStroke,
            ps.ColorBlendMode.ColorBlendMode,
            75,
            True,
        )

        # Set ruler units back the way we found it.
        app.preferences.rulerUnits = start_ruler_units
    else:
        print("Operation cannot be performed on background layer")
else:
    print("Create a document with an active selection before running this " "script!")
