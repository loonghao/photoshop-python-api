"""Demonstrate how to add metadata to a Photoshop document.

This example shows how to add and modify metadata properties of the active document,
such as author, location, and title information.

Example:
    ```python
    with Session(action="new_document") as ps:
        doc = ps.active_document
        doc.info.author = "John Doe"
        doc.info.title = "My Project"
    ```

Note:
    - The script automatically creates a new document using the Session action parameter
    - The author is set to the current system username by default
    - You can view metadata in Photoshop via: File > File Info
"""

# Import built-in modules
from __future__ import annotations

import os

# Import local modules
from photoshop import Session

# Create a new Photoshop session and document
with Session(action="new_document") as ps:
    # Get reference to active document
    doc = ps.active_document

    # Set metadata properties
    doc.info.author = os.getenv("USERNAME")  # Set author to system username
    doc.info.provinceState = "Beijing"  # Set location information
    doc.info.title = "My Demo"  # Set document title

    # Print the metadata information
    ps.echo("Metadata of current active document:")
    ps.echo(doc.info)
