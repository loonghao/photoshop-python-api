# Import local modules
from photoshop_python_api import save_options
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layers import ArtLayers
from photoshop_python_api.documents import Documents
from photoshop_python_api.errors import COMError
from photoshop_python_api.document import Document


class ActiveDocument(Document):
    def __int__(self):
        super(ActiveDocument, self).__init__()
