# Import built-in modules
from typing import TYPE_CHECKING

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ChannelType
from photoshop.api.solid_color import SolidColor


if TYPE_CHECKING:
    # Import local modules
    from photoshop.api._document import Document


# pylint: disable=too-many-public-methods
class Channel(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "duplicate",
            "merge",
        )

    @property
    def color(self) -> SolidColor:
        return SolidColor(self.app.color)

    @color.setter
    def color(self, value: SolidColor) -> None:
        self.app.color = value

    @property
    def histogram(self) -> tuple[int, ...]:
        return self.app.histogram

    @histogram.setter
    def histogram(self, value: tuple[int, ...]) -> None:
        self.app.histogram = value

    @property
    def kind(self) -> ChannelType:
        return ChannelType(self.app.kind)

    @kind.setter
    def kind(self, value: ChannelType) -> None:
        self.app.kind = value

    @property
    def opacity(self) -> float:
        return self.app.opacity

    @opacity.setter
    def opacity(self, value: float) -> None:
        self.app.opacity = value

    @property
    def visible(self) -> bool:
        return self.app.visible

    @visible.setter
    def visible(self, value: bool) -> None:
        self.app.visible = value

    @property
    def name(self) -> str:
        return self.app.name

    def duplicate(self, targetDocument: "Document | None" = None) -> "Channel":
        return Channel(self.app.duplicate(targetDocument))

    def merge(self) -> None:
        self.app.merge()

    def remove(self) -> None:
        self.eval_javascript(f'app.activeDocument.channels.getByName("{self.name}").remove()')
