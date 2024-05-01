"""Get document by document name from documents."""
# Import third-party modules
import examples._psd_files as psd  # Import from examples.
from photoshop import Session
# Import local modules


PSD_FILE = psd.get_psd_files()
slate_template = PSD_FILE["slate_template.psd"]
with Session(slate_template, action="open", auto_close=True) as ps:
    for doc in ps.app.documents:
        print(doc.name)
    print(ps.app.documents.getByName("slate_template.psd").fullName)
