"""Example of copying and pasting in Photoshop.

This script demonstrates how to:
1. Create a source document with sample content
2. Select different areas (full document, partial area)
3. Copy the selection with various options
4. Create a new document with matching properties
5. Paste the copied content with proper positioning
6. Handle different layer types (normal, text, smart object)

Module Attributes:
    None

Module Classes:
    None

Module Functions:
    create_sample_document() -> None
    copy_paste_area() -> None
    main() -> None
"""

from __future__ import annotations

# Import local modules
from photoshop import Session
from photoshop.api import Units
from photoshop.api.enumerations import NewDocumentMode, DocumentFill, LayerKind

def create_sample_document(ps, name: str = "Source Document") -> None:
    """Create a sample document with various content.
    
    Args:
        ps: Photoshop session object
        name: Name of the document to create
    """
    # Create a new document
    doc = ps.app.documents.add(
        width=500,
        height=300,
        resolution=72,
        name=name,
        mode=NewDocumentMode.NewRGB,
        initialFill=DocumentFill.White,
    )
    
    # Create a shape layer
    shape_layer = doc.artLayers.add()
    shape_layer.name = "Blue Rectangle"
    
    # Set shape color
    color = ps.SolidColor()
    color.rgb.red = 0
    color.rgb.green = 0
    color.rgb.blue = 255
    
    # Create shape selection
    doc.selection.select([
        [50, 50],
        [450, 50],
        [450, 250],
        [50, 250],
    ])
    
    # Fill shape
    ps.app.foregroundColor = color
    doc.selection.fill(ps.app.foregroundColor)
    doc.selection.deselect()
    
    # Add text layer
    text_layer = doc.artLayers.add()
    text_layer.kind = LayerKind.TextLayer
    text_layer.name = "Sample Text"
    text_layer.textItem.contents = "Copy & Paste Demo"
    text_layer.textItem.position = [150, 150]
    text_layer.textItem.size = 24
    text_layer.textItem.font = "Microsoft YaHei"
    
    print(f"Created sample document: {name}")

def copy_paste_area(
    ps,
    source_doc,
    paste_doc_name: str = "Paste Target",
    method: str = "all",
) -> None:
    """Copy an area from source document and paste into a new document.
    
    Args:
        ps: Photoshop session object
        source_doc: Source document to copy from
        paste_doc_name: Name for the new document
        method: Copy method ('all', 'merged', 'layer')
    """
    # Get document dimensions
    doc_width = int(source_doc.width)
    doc_height = int(source_doc.height)
    
    # Select appropriate copy method
    js = ""
    if method == "all":
        js = """
        try {
            app.activeDocument.selection.selectAll();
            app.activeDocument.selection.copy();
            app.activeDocument.selection.deselect();
            "success"
        } catch(e) {
            e.message
        }
        """
    elif method == "merged":
        js = """
        try {
            app.activeDocument.selection.selectAll();
            app.activeDocument.selection.copy(true);
            app.activeDocument.selection.deselect();
            "success"
        } catch(e) {
            e.message
        }
        """
    elif method == "layer":
        js = """
        try {
            app.activeDocument.activeLayer.copy();
            "success"
        } catch(e) {
            e.message
        }
        """
    
    # Execute copy operation
    result = ps.app.doJavaScript(js)
    if result != "success":
        print(f"Warning: Copy operation failed - {result}")
        return
    
    # Create and activate new document
    paste_doc = ps.app.documents.add(
        width=doc_width,
        height=doc_height,
        resolution=source_doc.resolution,
        name=paste_doc_name,
        mode=source_doc.mode,
        initialFill=DocumentFill.Transparent,
    )
    
    # Paste and position content
    paste_doc.paste()
    print(f"Content copied to new document: {paste_doc_name}")

def main() -> None:
    """Run the example script.
    
    This function demonstrates different copy and paste scenarios:
    1. Copy entire document
    2. Copy merged layers
    3. Copy active layer
    
    Returns:
        None
    """
    with Session() as ps:
        # Store original ruler units
        app = ps.app
        start_ruler_units = app.preferences.rulerUnits
        app.preferences.rulerUnits = Units.Pixels
        
        try:
            # Create source document
            create_sample_document(ps, "Source Document")
            source_doc = app.activeDocument
            
            # Example 1: Copy entire document
            print("\nExample 1: Copying entire document...")
            copy_paste_area(ps, source_doc, paste_doc_name="Full Copy", method="all")
            
            # Example 2: Copy merged layers
            print("\nExample 2: Copying merged layers...")
            copy_paste_area(ps, source_doc, paste_doc_name="Merged Copy", method="merged")
            
            # Example 3: Copy active layer
            print("\nExample 3: Copying active layer...")
            copy_paste_area(ps, source_doc, paste_doc_name="Layer Copy", method="layer")
            
            print("\nProcess completed! Check the following documents in Photoshop:")
            print("1. Source Document (original content)")
            print("2. Full Copy (all layers copied)")
            print("3. Merged Copy (flattened copy)")
            print("4. Layer Copy (active layer only)")
            
        finally:
            # Restore ruler units
            app.preferences.rulerUnits = start_ruler_units

if __name__ == "__main__":
    main()
