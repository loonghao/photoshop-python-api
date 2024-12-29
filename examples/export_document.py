"""Example of exporting a Photoshop document to different formats.

This example demonstrates how to:
1. Save documents in different formats (JPG, PNG)
2. Configure export quality settings
3. Handle file paths and naming
4. Use save options for different formats

Key concepts:
- File format conversion
- Export quality control
- Save options configuration
- File path handling
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Get the directory of current script
    current_dir = os.path.dirname(__file__)
    
    # Save as JPG with high quality
    jpg_opt = ps.JPEGSaveOptions(quality=12)
    jpg_path = os.path.join(current_dir, "output.jpg")
    doc.saveAs(jpg_path, jpg_opt)
    
    # Save as PNG with transparency
    png_opt = ps.PhotoshopSaveOptions()
    png_path = os.path.join(current_dir, "output.png")
    doc.saveAs(png_path, png_opt)
