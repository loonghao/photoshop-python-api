from photoshop._core import Photoshop


class LabColor(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def A(self):
        return self.app.A

    @A.setter
    def A(self, value):
        self.app.A = value

    @property
    def B(self):
        return self.app.B

    @B.setter
    def B(self, value):
        print(value)
        self.app.B = value

    @property
    def L(self):
        return self.app.L

    @L.setter
    def L(self, value):
        self.app.L = value
