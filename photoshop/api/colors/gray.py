"""Defines a gray color, used in the `SolidColor` object."""
# Import local modules
from photoshop.api._core import Photoshop


class GrayColor(Photoshop):
    object_name = "GrayColor"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def gray(self) -> float:
        """The gray value."""
        return self.app.gray

    @gray.setter
    def gray(self, value: float):
        """The gray value."""
        self.app.gray = value
