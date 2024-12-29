"""Demonstrates various image cropping techniques in Photoshop.

This example shows different ways to crop images, including:
1. Basic cropping with bounds
2. Cropping with aspect ratio
3. Cropping with resolution
4. Center-based cropping
"""

from __future__ import annotations

import os
from tempfile import mkdtemp

from photoshop import Session

def create_sample_document(ps, width=800, height=600):
    """Create a sample document with some content.
    
    Args:
        ps: Photoshop session object
        width: Document width in pixels
        height: Document height in pixels
        
    Returns:
        The created document
    """
    # Create a new document
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=72,
        name="Crop Example",
    )
    
    # Add background content using JavaScript
    js_code = """
    try {
        var doc = app.activeDocument;
        
        // Create a solid color layer
        var layer = doc.artLayers.add();
        layer.name = "Background";
        
        // Set color
        var color = new SolidColor();
        color.rgb.red = 255;
        color.rgb.green = 200;
        color.rgb.blue = 0;
        
        // Fill the layer
        doc.selection.selectAll();
        doc.selection.fill(color);
        doc.selection.deselect();
        
        "success"
    } catch(e) {
        e.message
    }
    """
    result = ps.app.doJavaScript(js_code)
    if result != "success":
        print(f"Warning: Background creation failed - {result}")
    
    return doc

def crop_with_bounds(ps, doc):
    """Crop the document using bounds.
    
    Args:
        ps: Photoshop session object
        doc: Target document
    """
    # Crop from all sides by 100 pixels
    doc.crop([100, 100, doc.width - 100, doc.height - 100])
    print("Applied bounds-based crop")

def crop_with_aspect_ratio(ps, doc):
    """Crop the document to a specific aspect ratio.
    
    Args:
        ps: Photoshop session object
        doc: Target document
    """
    # Crop to 16:9 aspect ratio
    target_width = doc.width
    target_height = int(target_width * 9 / 16)
    
    # Calculate vertical offset to center the crop
    y_offset = (doc.height - target_height) // 2
    
    doc.crop([0, y_offset, target_width, y_offset + target_height])
    print("Applied aspect ratio crop (16:9)")

def crop_with_resolution(ps, doc):
    """Crop the document and change its resolution.
    
    Args:
        ps: Photoshop session object
        doc: Target document
    """
    # First set the resolution
    doc.resolution = 300
    
    # Then crop and resize
    doc.crop(
        bounds=[0, 0, doc.width, doc.height],
        width=1920,
        height=1080,
    )
    print("Applied resolution crop (1920x1080 @ 300dpi)")

def center_crop(ps, doc, target_size):
    """Crop the document from the center.
    
    Args:
        ps: Photoshop session object
        doc: Target document
        target_size: Tuple of (width, height) for the target size
    """
    target_width, target_height = target_size
    
    # Calculate offsets to center the crop
    x_offset = (doc.width - target_width) // 2
    y_offset = (doc.height - target_height) // 2
    
    doc.crop([
        x_offset,
        y_offset,
        x_offset + target_width,
        y_offset + target_height,
    ])
    print(f"Applied center crop to {target_width}x{target_height}")

def main():
    """Run the example script."""
    with Session() as ps:
        doc = None
        try:
            # Create sample document
            doc = create_sample_document(ps)
            print("Created sample document")
            
            # Save original
            temp_dir = mkdtemp()
            original_path = os.path.join(temp_dir, "original.psd")
            doc.saveAs(original_path, ps.PhotoshopSaveOptions())
            print(f"Saved original to: {original_path}")
            
            # Try different crop methods
            crop_methods = [
                ("bounds", lambda: crop_with_bounds(ps, doc)),
                ("aspect", lambda: crop_with_aspect_ratio(ps, doc)),
                ("resolution", lambda: crop_with_resolution(ps, doc)),
                ("center", lambda: center_crop(ps, doc, (400, 400))),
            ]
            
            for name, crop_func in crop_methods:
                # Create new document for each crop
                if doc:
                    doc.close()
                doc = create_sample_document(ps)
                
                # Apply crop
                crop_func()
                
                # Save result
                output_path = os.path.join(temp_dir, f"crop_{name}.psd")
                doc.saveAs(output_path, ps.PhotoshopSaveOptions())
                print(f"Saved {name} crop to: {output_path}")
        
        finally:
            # Close the last document if it exists
            try:
                if doc and ps.app.documents.length > 0:
                    doc.close()
            except Exception as e:
                print(f"Warning: Error while closing document - {e}")

if __name__ == "__main__":
    main()
