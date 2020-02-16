from photoshop._core import Photoshop


class Layer(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def active_layer(self):
        return self.app.ActiveDocument.ActiveLayer

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
