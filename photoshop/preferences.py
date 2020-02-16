from photoshop._core import Photoshop


class Preferences(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def rulerUnits(self):
        return self.app.rulerUnits

    @rulerUnits.setter
    def rulerUnits(self, value):
        self.app.rulerUnits = value
