from typing import Sequence

import pytest

from photoshop.api.enumerations import PointKind, ShapeOperation, ToolType
from photoshop.api.path_item import PathItem
from photoshop.api.path_point_info import PathPointInfo
from photoshop.api.solid_color import SolidColor
from photoshop.api.sub_path_info import SubPathInfo
from photoshop.session import Session


class TestPathItems:
    """Test path items."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = Session(action="new_document", auto_close=True)
        self.session.run_action()
        self.app = self.session.app
        self.doc = self.session.active_document

        self.point_anchors = ((0, 0.0), (10.1, 0.0), (5, 5))

        self.path_item = self._create_path("test_path", self.point_anchors)

        yield
        self.session.close()

    def _create_path(
        self, name: str, point_anchors: Sequence[tuple[float, float]]
    ) -> PathItem:
        point_infos: list[PathPointInfo] = [
            PathPointInfo(anchor=anchor) for anchor in point_anchors
        ]

        last_anchor = point_anchors[-1]
        left = (last_anchor[0] + 1, last_anchor[1])
        right = (last_anchor[0], last_anchor[1] - 1)

        last_point = point_infos[-1]
        last_point.kind = PointKind.SmoothPoint
        last_point.leftDirection = left
        last_point.rightDirection = right

        sub_path = SubPathInfo(entire_sub_path=point_infos)

        return self.doc.pathItems.add(name=name, entire_path=(sub_path,))

    def test_path_item(self) -> None:
        for sub_path in self.path_item.subPathItems:
            assert ShapeOperation(sub_path.operation)
            assert isinstance(sub_path.closed, bool)
            for point in sub_path.pathPoints:
                assert isinstance(point.anchor, tuple)
                assert len(point.anchor) == 2
                assert PointKind(point.kind)
        solid_color = SolidColor()
        solid_color.rgb.red = 100
        solid_color.rgb.green = 100
        solid_color.rgb.blue = 100
        self.path_item.fillPath(solid_color)
        self.path_item.strokePath(ToolType.Blur)

    def test_path_removal(self) -> None:
        n_paths = 5
        for i in range(n_paths):
            self._create_path(f"test_{i}", self.point_anchors)

        path_items = self.doc.pathItems

        path_items_len = len(path_items)
        assert path_items_len >= n_paths
        path_items[0].remove()
        path_items["test_3"].remove()
        assert len(path_items) == path_items_len - 2
        path_items.removeAll()
        assert len(path_items) == 0
