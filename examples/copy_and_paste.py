"""
References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/CopyAndPaste.py

"""

import photoshop as ps

app = ps.Application()

startRulerUnits = app.preferences.rulerUnits

app.preferences.rulerUnits = ps.Units.Inches

doc = app.documents.add(
    7, 5, 72, None, ps.NewDocumentMode.NewRGB, ps.DocumentFill.White
)

# Make sure the active layer is not a text layer, which cannot be copied to the
# clipboard.
if doc.activeLayer.kind != ps.LayerKind.TextLayer:
    # Select the left half of the document. Selections are always expressed
    # in pixels regardless of the current ruler unit type, so we're computing
    # the selection corner points based on the inch unit width and height
    # of the document
    x2 = (doc.width * doc.resolution) / 2
    y2 = doc.height * doc.resolution

    sel_area = ((0, 0), (x2, 0), (x2, y2), (0, y2))
    doc.selection.select(sel_area, ps.SelectionType.ReplaceSelection, 0, False)

    doc.selection.copy()

    # The new doc is created
    # need to change ruler units to pixels because x2 and y2 are pixel units.
    app.preferences.rulerUnits = ps.Units.Pixels
    pasteDoc = app.documents.add(x2, y2, doc.resolution, "Paste Target")
    pasteDoc.paste()
else:
    print("You cannot copy from a text layer")

if startRulerUnits != app.preferences.rulerUnits:
    app.preferences.rulerUnits = startRulerUnits
