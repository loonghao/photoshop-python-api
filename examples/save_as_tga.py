"""Example of saving documents as TGA files in Photoshop.

This example demonstrates how to:
1. Save documents in TGA format
2. Configure TGA save options
3. Handle alpha channels
4. Set compression options

Key concepts:
- TGA export
- Save options
- Alpha channel handling
- Resolution settings
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Configure TGA save options
    tga_options = ps.TargaSaveOptions()
    tga_options.alphaChannels = True
    tga_options.resolution = ps.TargaBitsPerPixels.TWENTYFOUR
    tga_options.rleCompression = True
    
    # Generate output path
    output_path = os.path.join(os.path.dirname(__file__), "output.tga")
    
    # Save document as TGA
    doc.saveAs(output_path, tga_options, True)
    
    # Save another version with different settings
    tga_options.resolution = ps.TargaBitsPerPixels.THIRTYTWO
    output_path_32 = os.path.join(os.path.dirname(__file__), "output_32bit.tga")
    doc.saveAs(output_path_32, tga_options, True)
