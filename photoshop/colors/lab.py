from photoshop._core import Photoshop


class LabColor(Photoshop):

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def A(self):
        return self.parent.A

    @A.setter
    def A(self, value):
        self.parent.A = value

    @property
    def B(self):
        return self.parent.B

    @B.setter
    def B(self, value):
        print(value)
        self.parent.B = value
