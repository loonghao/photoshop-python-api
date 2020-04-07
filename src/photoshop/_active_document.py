# Import local modules
from photoshop._document import Document


class ActiveDocument(Document):
    def __init__(self, parent):
        super().__init__(parent=parent)
