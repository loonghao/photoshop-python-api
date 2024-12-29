"""Example of creating a new document in Photoshop.

This example demonstrates how to:
1. Create a new document with specific dimensions
2. Set document properties like name and mode
3. Work with document units and resolution

Key concepts:
- Document creation
- Document properties
- Color mode settings
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Create a new document with specific dimensions
    doc = ps.app.documents.add(
        width=1920,
        height=1080,
        resolution=72,
        name="New Document Example"
    )
