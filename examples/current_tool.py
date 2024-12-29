"""Demonstrates how to work with Photoshop tools.

This example shows how to:
1. Get the current tool
2. Change tools
3. List available tools
4. Set tool options
"""

from __future__ import annotations

import os
from tempfile import mkdtemp

from photoshop import Session

def print_current_tool(ps):
    """Print information about the current tool.
    
    Args:
        ps: Photoshop session object
    """
    current_tool = ps.app.currentTool
    print(f"Current tool: {current_tool}")

def set_tool(ps, tool_name):
    """Set the current tool.
    
    Args:
        ps: Photoshop session object
        tool_name: Name of the tool to set
    """
    try:
        ps.app.currentTool = tool_name
        print(f"Changed to tool: {tool_name}")
    except Exception as e:
        print(f"Error setting tool {tool_name}: {e}")

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
        name="Tool Example",
    )
    
    # Add a layer to work with
    layer = doc.artLayers.add()
    layer.name = "Test Layer"
    
    return doc

def set_tool_options(ps, doc):
    """Set various tool options.
    
    Args:
        ps: Photoshop session object
        doc: Target document
    """
    # Set ruler units to pixels
    js_code = """
    try {
        app.preferences.rulerUnits = Units.PIXELS;
        app.preferences.typeUnits = TypeUnits.PIXELS;
        "success"
    } catch(e) { e.message }
    """
    result = ps.app.doJavaScript(js_code)
    print(f"Set preferences: {result}")
    
    # Set layer opacity
    try:
        doc.activeLayer.opacity = 50
        print("Set layer opacity to 50%")
    except Exception as e:
        print(f"Error setting opacity: {e}")

def main():
    """Run the example script."""
    with Session() as ps:
        try:
            # Create sample document
            doc = create_sample_document(ps)
            print("Created sample document")
            
            # Print current tool
            print_current_tool(ps)
            
            # Try different tools
            tools = [
                "moveTool",  # Move tool
                "marqueeRectTool",  # Rectangular marquee tool
                "marqueeEllipTool",  # Elliptical marquee tool
                "lassoTool",  # Lasso tool
                "magicWandTool",  # Magic wand tool
                "cropTool",  # Crop tool
                "eyedropperTool",  # Eyedropper tool
                "paintbrushTool",  # Brush tool
                "eraserTool",  # Eraser tool
                "typeCreateOrEditTool",  # Type tool
            ]
            
            print("\nTrying different tools:")
            for tool in tools:
                set_tool(ps, tool)
            
            # Set tool options
            print("\nSetting tool options:")
            set_tool_options(ps, doc)
            
            # Save the document
            temp_dir = mkdtemp()
            output_path = os.path.join(temp_dir, "tool_example.psd")
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
