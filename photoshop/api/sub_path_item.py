from typing import TYPE_CHECKING, Iterator

from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ShapeOperation
from photoshop.api.path_point import PathPoint

if TYPE_CHECKING:
    from photoshop.api.path_item import PathItem


class SubPathItem(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def closed(self) -> bool:
        return self.app.closed

    @property
    def operation(self) -> ShapeOperation:
        return ShapeOperation(self.app.operation)

    @property
    def parent(self) -> "PathItem":
        from photoshop.api.path_item import PathItem

        return PathItem(self.app.parent)

    @property
    def pathPoints(self) -> Iterator[PathPoint]:
        for point in self.app.pathPoints:
            yield PathPoint(point)
