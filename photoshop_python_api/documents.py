# Import local modules
from photoshop_python_api.active_document import ActiveDocument
from photoshop_python_api.active_layer import ActiveLayer
from photoshop_python_api.application import Application


class Documents(Application):
    def __init__(self):
        super(Documents, self).__init__()

    @property
    def active_layer(self):
        return ActiveLayer()

    def add(self, *args, **kwargs):
        self.app.Documents.Add(*args, **kwargs)
        return self.active_document

    def close(self, **kwargs):
        return self.active_document.close(**kwargs)

    def add_art_layer(self):
        doc_ref = self.add()
        return doc_ref.ArtLayers.Add()

    def open(self, *args, **kwargs):
        super(Documents, self).open(*args, **kwargs)
        return self.active_document


    @property
    def active_document(self):
        return ActiveDocument()
