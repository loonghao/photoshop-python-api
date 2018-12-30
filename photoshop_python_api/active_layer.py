# Import local modules
from photoshop_python_api._core import Core


class ActiveLayer(Core):
    def __int__(self):
        super(ActiveLayer, self).__init__()

    @property
    def name(self):
        return self.active_layer.Typename

    def add(self):
        self.ps.ActiveDocument.ArtLayers.Add()


