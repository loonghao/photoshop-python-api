# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api.document import Document


class Documents(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def add(self):
        return Document(self.app.add())

    @property
    def length(self):
        return self.app.length

    def getByName(self, document_name):
        return self.app.getByName(document_name)
