# Import local modules
from photoshop.api._core import Photoshop


class LabColor(Photoshop):
    """A Lab color specification."""

    object_name = "LabColor"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def A(self) -> float:
        return self.app.A

    @A.setter
    def A(self, value: float) -> None:
        self.app.A = value

    @property
    def B(self) -> float:
        return self.app.B

    @B.setter
    def B(self, value: float) -> None:
        self.app.B = value

    @property
    def L(self) -> float:
        return self.app.L

    @L.setter
    def L(self, value: float) -> None:
        self.app.L = value
