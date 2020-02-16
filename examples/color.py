from photoshop.document import Document
from photoshop.solid_color import SolidColor

doc = Document()
doc_ref = doc.art_layers
textColor = SolidColor()
textColor.cmyk.Cyan = 225
textColor.cmyk.magenta = 0
# textColor.cmyk.Blue = 1
newTextLayer = doc_ref.add()
psTextLayer = 2  # from enum PsLayerKind
newTextLayer.Kind = psTextLayer
newTextLayer.TextItem.Contents = 'Hello, World!'
newTextLayer.TextItem.Position = [160, 167]
newTextLayer.TextItem.Size = 36
newTextLayer.TextItem.Color = textColor.option
