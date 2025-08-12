from photoshop.api._core import Photoshop
from photoshop.api.enumerations import PointKind


class PathPointInfo(Photoshop):
    # The COM API somehow uses "object_name" to recognize this as an object of
    # that type, which allows instantiating this object in Python and then passing
    # it to COM API functions that use objects of that type.
    object_name = "PathPointInfo"

    def __init__(
        self,
        parent: Photoshop | None = None,
        anchor: tuple[float, float] | None = None,
        left_direction: tuple[float, float] | None = None,
        right_direction: tuple[float, float] | None = None,
        kind: PointKind | None = None,
    ):
        super().__init__(parent=parent)

        # Each of anchor, leftDirection and rightDirection have to be set
        # for the point to be valid.
        if anchor:
            self.anchor = anchor

        if left_direction:
            self.leftDirection = left_direction
        elif anchor:
            self.leftDirection = anchor

        if right_direction:
            self.rightDirection = right_direction
        elif anchor:
            self.rightDirection = anchor

        if kind:
            self.kind = kind
        elif left_direction or right_direction:
            self.kind = PointKind.SmoothPoint
        elif anchor:
            self.kind = PointKind.CornerPoint

    @property
    def anchor(self) -> tuple[float, float]:
        return self.app.anchor

    @anchor.setter
    def anchor(self, value: tuple[float, float]) -> None:
        self.app.anchor = value

    @property
    def kind(self) -> PointKind:
        return PointKind(self.app.kind)

    @kind.setter
    def kind(self, value: PointKind) -> None:
        self.app.kind = value

    @property
    def leftDirection(self) -> tuple[float, float]:
        return self.app.leftDirection

    @leftDirection.setter
    def leftDirection(self, value: tuple[float, float]) -> None:
        self.app.leftDirection = value

    @property
    def rightDirection(self) -> tuple[float, float]:
        return self.app.rightDirection

    @rightDirection.setter
    def rightDirection(self, value: tuple[float, float]) -> None:
        self.app.rightDirection = value
