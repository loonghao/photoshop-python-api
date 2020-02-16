# Import local modules
from photoshop._core import Photoshop
from photoshop.document import Document


class Documents(Photoshop):
    def __init__(self, parent):
        # super().__init__(parent=parent)
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    def add(self, *args, **kwargs):
        return Document(self.app.add(*args, **kwargs))

    @property
    def length(self):
        return len([doc for doc in self.app])

    def getByName(self, document_name):
        return self.app.getByName(document_name)
