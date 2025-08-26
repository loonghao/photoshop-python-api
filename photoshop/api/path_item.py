# Import built-in modules
from typing import TYPE_CHECKING, Iterator

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ColorBlendMode, PathKind, SelectionType, ToolType
from photoshop.api.solid_color import SolidColor
from photoshop.api.sub_path_item import SubPathItem


if TYPE_CHECKING:
    # Import local modules
    from photoshop.api._document import Document


class PathItem(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "deselect",
            "duplicate",
            "fillPath",
            "makeClippingPath",
            "makeSelection",
            "delete",
            "select",
            "strokePath",
        )

    @property
    def kind(self) -> PathKind:
        return PathKind(self.app.kind)

    @kind.setter
    def kind(self, value: PathKind) -> None:
        self.app.kind = value

    @property
    def name(self) -> str:
        return self.app.name

    @name.setter
    def name(self, value: str) -> None:
        self.app.name = value

    @property
    def parent(self) -> "Document":
        # Import local modules
        from photoshop.api._document import Document

        return Document(self.app.parent)

    @property
    def subPathItems(self) -> Iterator[SubPathItem]:
        for sub_path in self.app.subPathItems:
            yield SubPathItem(sub_path)

    def deselect(self) -> None:
        self.app.deselect()

    def duplicate(self, name: str | None = None) -> None:
        name = name if name else f"Duplicate of {self.name}"
        return self.app.duplicate(name)

    def fillPath(
        self,
        fill_color: SolidColor,
        mode: ColorBlendMode | None = None,
        opacity: float = 100,
        preserve_transparency: bool = False,
        feather: float = 0,
        whole_path: bool = True,
        anti_alias: bool = True,
    ) -> None:
        return self.app.fillPath(
            fill_color,
            mode,
            opacity,
            preserve_transparency,
            feather,
            whole_path,
            anti_alias,
        )

    def makeClippingPath(self, flatness: float) -> None:
        return self.app.makeClippingPath(flatness)

    def makeSelection(
        self,
        feather: float = 0,
        anti_alias: bool = True,
        operation: SelectionType | None = None,
    ) -> None:
        return self.app.makeSelection(feather, anti_alias, operation)

    def remove(self) -> None:
        return self.app.delete()

    def select(self) -> None:
        return self.app.select()

    def strokePath(self, tool: ToolType, simulate_pressure: bool = False) -> None:
        return self.app.strokePath(tool, simulate_pressure)
