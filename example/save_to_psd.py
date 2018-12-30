
from photoshop_python_api.document import Document
from photoshop_python_api.save_options import JPEGSaveOptions
documents = Document()
# create new documents
doc = documents.art_layers
# add new artlayers
doc.add()
options = JPEGSaveOptions()
# save to psd
documents.save_as('c:/te222221st.jpg', options, as_copy=True)
