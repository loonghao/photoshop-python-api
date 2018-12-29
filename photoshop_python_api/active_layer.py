# Import local modules
from photoshop_python_api.application import Application


class ActiveLayer(Application):
    def __int__(self):
        super(ActiveLayer, self).__init__()

    def add(self):
        self.app.ActiveDocument.ArtLayers.Add()


