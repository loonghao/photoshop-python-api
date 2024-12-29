"""Example of retrieving a Photoshop document by its name.

This example demonstrates how to:
1. Access documents in the Photoshop application
2. Find a specific document by its name
3. Handle cases when the document doesn't exist

Key concepts:
- Using the documents collection
- Document name comparison
- Error handling for missing documents
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Try to get document named 'test.psd'
    for doc in ps.app.documents:
        if doc.name == "test.psd":
            ps.echo(doc.name)
            break
    else:
        ps.echo("Document not found!")
