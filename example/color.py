from photoshop_python_api.document import Document
from photoshop_python_api.solid_color import SolidColor

doc = Document()
doc_ref = doc.art_layers
textColor = SolidColor()
textColor.RGB.Red = 225
textColor.RGB.Green = 0
textColor.RGB.Blue = 0
newTextLayer = doc_ref.add()
psTextLayer = 2  # from enum PsLayerKind
newTextLayer.Kind = psTextLayer
newTextLayer.TextItem.Contents = "Hello, World!"
newTextLayer.TextItem.Position = [160, 167]
newTextLayer.TextItem.Size = 36
newTextLayer.TextItem.Color = textColor.option
