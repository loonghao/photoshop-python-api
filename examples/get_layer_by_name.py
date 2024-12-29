"""Example of retrieving a layer by its name in Photoshop.

This example demonstrates how to:
1. Access layers in the active document
2. Find a specific layer by its name
3. Handle layer search in the document hierarchy

Key concepts:
- Layer navigation
- Name-based layer lookup
- Active document context
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Access active document's layers
    doc = ps.app.activeDocument
    for layer in doc.layers:
        if layer.name == "example layer":
            ps.echo(layer.name)
            break
