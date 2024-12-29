"""Example of saving documents as PDF files in Photoshop.

This example demonstrates how to:
1. Save documents in PDF format
2. Configure PDF save options
3. Handle PDF compression settings
4. Set PDF compatibility options

Key concepts:
- PDF export
- Save options
- File compression
- PDF settings
"""

# Import built-in modules
import os

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Configure PDF save options
    pdf_options = ps.PDFSaveOptions()
    pdf_options.alphaChannels = True
    pdf_options.embedColorProfile = True
    pdf_options.embedFonts = True
    pdf_options.layers = False
    pdf_options.optimizeForWeb = True
    pdf_options.view = False
    
    # Generate output path
    output_path = os.path.join(os.path.dirname(__file__), "output.pdf")
    
    # Save document as PDF
    doc.saveAs(output_path, pdf_options, True)
