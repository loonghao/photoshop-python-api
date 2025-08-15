# Import built-in modules
from typing import TYPE_CHECKING

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import PointKind


if TYPE_CHECKING:
    # Import local modules
    from photoshop.api.sub_path_item import SubPathItem


class PathPoint(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def anchor(self) -> tuple[float, float]:
        return self.app.anchor

    @property
    def kind(self) -> PointKind:
        return PointKind(self.app.kind)

    @property
    def leftDirection(self) -> tuple[float, float]:
        return self.app.leftDirection

    @property
    def parent(self) -> "SubPathItem":
        # Import local modules
        from photoshop.api.sub_path_item import SubPathItem

        return SubPathItem(self.app.parent)

    @property
    def rightDirection(self) -> tuple[float, float]:
        return self.app.rightDirection
