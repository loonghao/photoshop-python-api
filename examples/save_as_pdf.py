"""Save current active document as a PDF file."""
# Import built-in modules
import os
from tempfile import mkdtemp

from photoshop import Session
# Import local modules


with Session() as ps:
    option = ps.PDFSaveOptions(jpegQuality=12, layers=True, view=True)
    pdf = os.path.join(mkdtemp(), "test.pdf")
    ps.active_document.saveAs(pdf, option)

with Session() as ps:
    option = ps.PDFSaveOptions()
    option.jpegQuality = 12
    option.layers = True
    option.view = True  # opens the saved PDF in Acrobat.
    pdf = os.path.join(mkdtemp(), "test.pdf")
    ps.active_document.saveAs(pdf, option)
