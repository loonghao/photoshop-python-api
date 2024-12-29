"""Example of duplicating documents within a Photoshop session.

This example demonstrates how to:
1. Duplicate existing documents
2. Configure duplication options
3. Handle document copies
4. Manage document references

Key concepts:
- Document duplication
- Session management
- Document handling
- Copy options
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    if len(ps.app.documents) > 0:
        # Duplicate active document
        doc = ps.active_document.duplicate()
