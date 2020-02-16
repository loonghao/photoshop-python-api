# Import local modules
from photoshop.document import Document


class ActiveDocument(Document):
    def __int__(self, parent):
        super().__init__(parent=parent)
