"""Demonstrate how to work with active layers in Photoshop.

This example shows how to:
1. Create a new document if none exists
2. Add new art layers to the document
3. Get and set the active layer
4. Rename layers

Example:
    ```python
    with Session() as ps:
        doc_ref = ps.app.documents.add()  # Create new document
        new_layer = doc_ref.artLayers.add()  # Add new layer
        new_layer.name = "test"  # Rename layer
    ```

Note:
    The script will create a new document if none exists,
    and will add a new layer if the document has less than MIN_LAYERS layers.
"""

# Import built-in modules
from __future__ import annotations

# Import local modules
from photoshop import Session

def main():
    """Demonstrate active layer operations in Photoshop."""
    with Session() as ps:
        # Create a new document if none exists
        doc_ref = ps.app.documents.add() if len(ps.app.documents) < 1 else ps.app.activeDocument

        # Add a new layer if document has less than MIN_LAYERS layers
        MIN_LAYERS = 2
        if len(doc_ref.layers) < MIN_LAYERS:
            doc_ref.artLayers.add()

        # Print the name of the current active layer
        ps.echo(doc_ref.activeLayer.name)

        # Create a new art layer and make it active
        new_layer = doc_ref.artLayers.add()
        ps.echo(new_layer.name)

        # Rename the new layer
        new_layer.name = "test"

if __name__ == "__main__":
    main()
