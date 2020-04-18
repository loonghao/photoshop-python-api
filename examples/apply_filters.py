"""
References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyFilters.py

"""
import os

# selections in the open document.
import photoshop as ps

# Start up Photoshop application
app = ps.Application()

# We don't want any Photoshop dialogs displayed during automated execution
app.displayDialogs = ps.DialogModes.DisplayNoDialogs

psPixels = 1
start_ruler_units = app.preferences.rulerUnits
if start_ruler_units is not psPixels:
    app.preferences.rulerUnits = psPixels

fileName = os.path.join(os.path.dirname(__file__), "layer_comps.psd")
docRef = app.open(fileName)
nLayerSets = len(list((i, x) for i, x in enumerate(docRef.layerSets))) - 1
nArtLayers = len(
    list((i, x) for i, x in enumerate(docRef.layerSets[nLayerSets].artLayers)),
)

active_layer = docRef.activeLayer = docRef.layerSets[nLayerSets].artLayers[nArtLayers]
sel_area = ((0, 212), (300, 212), (300, 300), (0, 300))
docRef.selection.select(sel_area, ps.SelectionType.ReplaceSelection, 20, True)
print(active_layer.name)
active_layer.applyAddNoise(15, ps.NoiseDistribution.GaussianNoise, False)

backColor = ps.SolidColor()
backColor.hsb.hue = 0
backColor.hsb.saturation = 0
backColor.hsb.brightness = 100
app.backgroundColor = backColor

sel_area2 = ((120, 20), (210, 20), (210, 110), (120, 110))
docRef.selection.select(sel_area2, ps.SelectionType.ReplaceSelection, 25, False)
active_layer.applyDiffuseGlow(9, 12, 15)
active_layer.applyGlassEffect(
    7, 3, 7, False, ps.TextureType.TinyLensTexture, None,
)
docRef.selection.deselect()

# Set ruler units back the way we found it.
if start_ruler_units is not psPixels:
    app.Preferences.RulerUnits = start_ruler_units
