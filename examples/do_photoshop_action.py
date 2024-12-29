"""Demonstrates how to work with Photoshop actions.

This example shows how to:
1. List available actions
2. Run actions
3. Apply text watermark directly
"""

from __future__ import annotations

import os
from tempfile import mkdtemp

from photoshop import Session
from photoshop.api import enumerations

def list_actions(ps):
    """List available actions and action sets.
    
    Args:
        ps: Photoshop session object
    """
    js_code = """
    try {
        var result = [];
        // List action sets
        for (var i = 0; i < app.actionSets.length; i++) {
            var set = app.actionSets[i];
            result.push("Action Set: " + set.name);
            
            // List actions in the set
            for (var j = 0; j < set.actions.length; j++) {
                var action = set.actions[j];
                result.push("  - Action: " + action.name);
            }
        }
        result.join("\\n");
    } catch(e) {
        e.message;
    }
    """
    result = ps.app.doJavaScript(js_code)
    print("\nAvailable Actions:")
    print(result if result else "No actions found")

def add_watermark(ps, doc, text="Watermark"):
    """Add a text watermark to the document.
    
    Args:
        ps: Photoshop session object
        doc: Target document
        text: Watermark text
    """
    try:
        # Create text layer
        layer = doc.artLayers.add()
        layer.kind = enumerations.LayerKind.TextLayer
        
        # Set text properties
        text_item = layer.textItem
        text_item.contents = text
        text_item.size = 48  # points
        
        # Set color to white
        text_color = ps.SolidColor()
        text_color.rgb.red = 255
        text_color.rgb.green = 255
        text_color.rgb.blue = 255
        text_item.color = text_color
        
        # Set opacity
        layer.opacity = 50
        
        # Center the text
        text_item.position = [doc.width/2, doc.height/2]
        
        print(f"Added watermark: {text}")
    except Exception as e:
        print(f"Error adding watermark: {e}")

def create_sample_document(ps):
    """Create a sample document to work with.
    
    Args:
        ps: Photoshop session object
        
    Returns:
        The created document
    """
    # Create new document
    doc = ps.app.documents.add(
        width=800,
        height=600,
        resolution=72,
        name="Action Example",
    )
    
    # Add some content (colored background)
    color = ps.SolidColor()
    color.rgb.red = 0
    color.rgb.green = 100
    color.rgb.blue = 200
    
    doc.selection.selectAll()
    doc.selection.fill(color)
    doc.selection.deselect()
    
    return doc

def main():
    """Run the example script."""
    with Session() as ps:
        try:
            # Create sample document
            doc = create_sample_document(ps)
            print("Created sample document")
            
            # List available actions
            list_actions(ps)
            
            # Add watermark directly
            add_watermark(ps, doc, "Sample Watermark")
            
            # Save the document
            temp_dir = mkdtemp()
            output_path = os.path.join(temp_dir, "watermark_example.psd")
            doc.saveAs(output_path, ps.PhotoshopSaveOptions())
            print(f"\nDocument saved to: {output_path}")
        
        finally:
            if doc:
                try:
                    doc.close()
                except Exception as e:
                    print(f"Warning: Error while closing document - {e}")

if __name__ == "__main__":
    main()
