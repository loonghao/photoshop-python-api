# Import local modules
from photoshop_python_api import save_options
from photoshop_python_api._core import Photoshop
from photoshop_python_api.art_layers import ArtLayers


class Documents(Photoshop):
    def __init__(self):
        super(Documents, self).__init__()

    @property
    def _documents(self):
        return self.adobe.documents

    def add(self):
        return self._documents.Add()

    @property
    def length(self):
        return self._documents.length
