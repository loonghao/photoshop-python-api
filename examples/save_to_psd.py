"""Example of saving documents as PSD files in Photoshop.

This example demonstrates how to:
1. Save documents in PSD format
2. Configure PSD save options
3. Preserve layer information
4. Handle compatibility settings

Key concepts:
- PSD format
- Layer preservation
- Save options
- File compatibility
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Configure PSD save options
    psd_options = ps.PhotoshopSaveOptions()
    psd_options.alphaChannels = True
    psd_options.annotations = True
    psd_options.layers = True
    psd_options.spotColors = True
    
    # Generate output path
    output_path = os.path.join(os.path.dirname(__file__), "output.psd")
    
    # Save document as PSD
    doc.saveAs(output_path, psd_options, True)
