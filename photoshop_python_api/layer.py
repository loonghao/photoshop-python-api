# Import local modules
from photoshop_python_api._core import Photoshop


class Layer(Photoshop):
    def __init__(self):
        super(Layer, self).__init__()

    @property
    def active_layer(self):
        print dir(self.adobe.ActiveDocument)
        return self.adobe.ActiveDocument.ActiveLayer

    @property
    def all_locked(self):
        return self.active_layer.AllLocked

    @property
    def blend_mode(self):
        return self.active_layer.BlendMode

    @property
    def bounds(self):
        return self.active_layer.bounds

    @property
    def BoundsNoEffects(self):
        return self.active_layer.BoundsNoEffects
