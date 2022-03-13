# Import local modules
from photoshop.api._core import Photoshop


class LabColor(Photoshop):
    """A Lab color specification."""

    object_name = "LabColor"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def A(self):
        return round(self.app.A)

    @A.setter
    def A(self, value):
        self.app.A = value

    @property
    def B(self):
        return round(self.app.B)

    @B.setter
    def B(self, value):
        self.app.B = value

    @property
    def L(self):
        return round(self.app.L)

    @L.setter
    def L(self, value):
        self.app.L = value
