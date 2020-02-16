"""
References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/ApplyFilters.py
"""
# This sample script shows how to apply 3 different filters to
# selections in the open document.
from photoshop import Application
from photoshop import DialogModes
from photoshop import SelectionType
from photoshop import SolidColor
from photoshop import TextureType

# Start up Photoshop application
# Or get Reference to already running Photoshop application instance
app = Application()

# We don't want any Photoshop dialogs displayed during automated execution
app.displayDialogs = DialogModes.DisplayNoDialogs

psPixels = 1
start_ruler_units = app.preferences.rulerUnits
if start_ruler_units is not psPixels:
    app.preferences.rulerUnits = psPixels

fileName = 'd:/Untitled-11.psd'
docRef = app.open(fileName)
nLayerSets = len([(i, x) for i, x in enumerate(docRef.layerSets)]) - 1
nArtLayers = len(
    [(i, x) for i, x in enumerate(docRef.layerSets[nLayerSets].artLayers)],
)

active_layer = docRef.activeLayer = docRef.layerSets[nLayerSets].artLayers[
    nArtLayers
]
# # sel_area argument not accepted if using win32com, using comtypes instead
sel_area = ((0, 212), (300, 212), (300, 300), (0, 300))
docRef.selection.select(sel_area, SelectionType.ReplaceSelection, 20, True)
psGaussianNoise = 2  # from enum PsNoiseDistribution
print(active_layer.name)
active_layer.applyAddNoise(15, psGaussianNoise, False)

backColor = SolidColor()
backColor.hsb.hue = 0
backColor.hsb.saturation = 0
backColor.hsb.brightness = 100
app.backgroundColor = backColor

sel_area2 = ((120, 20), (210, 20), (210, 110), (120, 110))
docRef.selection.select(sel_area2, SelectionType.ReplaceSelection, 25, False)
active_layer.applyDiffuseGlow(9, 12, 15)
active_layer.applyGlassEffect(
    7, 3, 7, False, TextureType.TinyLensTexture,
    None,
)
docRef.selection.deselect()

# Set ruler units back the way we found it
if start_ruler_units is not psPixels:
    app.Preferences.RulerUnits = start_ruler_units
