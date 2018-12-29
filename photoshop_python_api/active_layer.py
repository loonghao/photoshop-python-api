# Import local modules
from photoshop_python_api.application import Application


class ActiveLayer(Application):
    def __int__(self):
        super(ActiveLayer, self).__init__()

    @property
    def name(self):
        return self.active_layer.Typename

    def add(self):
        self.app.ActiveDocument.ArtLayers.Add()


