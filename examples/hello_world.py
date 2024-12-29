"""Basic example demonstrating Photoshop automation with python-photoshop-api.

This example demonstrates how to:
1. Connect to Photoshop application
2. Create a new document
3. Add text content to the document
4. Save the document as PSD file

Key concepts:
- Application connection
- Document creation
- Text layer manipulation
- File saving
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    # Create a new document
    doc = ps.app.documents.add()
    
    # Create text layer with "Hello, World!"
    text_color = ps.SolidColor()
    text_color.rgb.red = 255
    text_color.rgb.green = 0
    text_color.rgb.blue = 0

    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = "Hello, World!"
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color

    # Save the document
    jpg_file = os.path.join(os.path.dirname(__file__), "hello_world.jpg")
    ps.JPEGSaveOptions(quality=12)
    doc.saveAs(jpg_file)
