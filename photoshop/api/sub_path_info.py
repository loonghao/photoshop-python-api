from typing import Iterator, Sequence

from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ShapeOperation
from photoshop.api.path_point_info import PathPointInfo


class SubPathInfo(Photoshop):
    object_name = "SubPathInfo"

    def __init__(
        self,
        parent: Photoshop | None = None,
        entire_sub_path: Sequence[PathPointInfo] | None = None,
        closed: bool = True,
        operation: ShapeOperation = ShapeOperation.ShapeAdd,
    ):
        super().__init__(parent=parent)

        if entire_sub_path:
            self.entireSubPath = entire_sub_path
        self.closed = closed
        self.operation = operation

    @property
    def closed(self) -> bool:
        return self.app.closed

    @closed.setter
    def closed(self, value: bool) -> None:
        self.app.closed = value

    @property
    def entireSubPath(self) -> Iterator[PathPointInfo]:
        for point in self.app.entireSubPath:
            yield PathPointInfo(point)

    @entireSubPath.setter
    def entireSubPath(self, value: Sequence[PathPointInfo]) -> None:
        self.app.entireSubPath = value

    @property
    def operation(self) -> ShapeOperation:
        return ShapeOperation(self.app.operation)

    @operation.setter
    def operation(self, value: ShapeOperation) -> None:
        self.app.operation = value
