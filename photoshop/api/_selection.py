"""The selected area of the document or layer."""

# Import local modules
from photoshop.api._channel import Channel
from photoshop.api._core import Photoshop
from photoshop.api._document import Document
from photoshop.api.enumerations import (
    AnchorPosition,
    ColorBlendMode,
    SelectionType,
    StrokeLocation,
)
from photoshop.api.solid_color import SolidColor


# pylint: disable=too-many-public-methods, too-many-arguments
class Selection(Photoshop):
    """The selected area of the document."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "clear",
            "contract",
            "copy",
            "cut",
            "deselect",
            "expand",
            "feather",
            "fill",
            "grow",
            "invert",
            "load",
            "makeWorkPath",
            "resize",
            "resizeBoundary",
            "rotate",
            "rotateBoundary",
            "select",
            "selectBorder",
            "selectAll",
            "similar",
            "smooth",
            "store",
            "stroke",
            "translate",
            "translateBoundary",
        )

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        return self.app.bounds

    def parent(self) -> Document:
        return Document(self.app.parent)

    @property
    def solid(self) -> bool:
        return self.app.solid

    def clear(self) -> None:
        """Clears the selection and does not copy it to the clipboard."""
        self.app.clear()

    def contract(self, contract_by: float) -> None:
        """Contracts the selection."""
        self.app.contract(contract_by)

    def copy(self, merge: bool = False) -> None:
        """Copies the selection to the clipboard."""
        self.app.copy(merge)

    def cut(self) -> None:
        """Clears the current selection and copies it to the clipboard."""
        self.app.cut()

    def select(
        self,
        region: tuple[
            tuple[float, float],
            tuple[float, float],
            tuple[float, float],
            tuple[float, float],
        ],
        selection_type: SelectionType | None = None,
        feather: float = 0,
        anti_alias: bool = True,
    ) -> None:
        self.app.select(region, selection_type, feather, anti_alias)

    def deselect(self) -> None:
        """Deselects the current selection."""
        self.app.deselect()

    def expand(self, by: float) -> None:
        """Expands the selection.

        Args:
            by: The amount to expand the selection.

        """
        self.app.expand(by)

    def feather(self, by: float) -> None:
        """Feathers the edges of the selection.

        Args:
            by: The amount to feather the edge.

        """
        self.app.feather(by)

    def fill(
        self,
        fill_type: SolidColor,
        mode: ColorBlendMode | None = None,
        opacity: float | None = None,
        preserve_transparency: bool = False,
    ) -> None:
        """Fills the selection."""
        self.app.fill(fill_type, mode, opacity, preserve_transparency)

    def grow(self, tolerance: int, anti_alias: bool) -> None:
        """Grows the selection to include all adjacent pixels falling within

        The specified tolerance range.

        Args:
            tolerance (int): The tolerance range. Range: 0 to 255.
            anti_alias (bool): If true, anti-aliasing is used.


        """
        self.app.grow(tolerance, anti_alias)

    def invert(self) -> None:
        """Inverts the selection."""
        self.app.invert()

    def load(
        self,
        from_channel: Channel,
        combination: SelectionType | None = None,
        inverting: bool = False,
    ) -> None:
        """Loads the selection from the specified channel."""
        self.app.load(from_channel, combination, inverting)

    def makeWorkPath(self, tolerance: float) -> None:
        """Makes this selection item the workpath for this document."""
        self.app.makeWorkPath(tolerance)

    def resize(
        self, horizontal: float, vertical: float, anchor: AnchorPosition
    ) -> None:
        """Resizes the selected area to the specified dimensions and anchor
        position."""
        self.app.resize(horizontal, vertical, anchor)

    def resizeBoundary(
        self, horizontal: float, vertical: float, anchor: AnchorPosition
    ) -> None:
        """Scales the boundary of the selection."""
        self.app.resizeBoundary(horizontal, vertical, anchor)

    def rotate(self, angle: float, anchor: AnchorPosition) -> None:
        """Rotates the object."""
        self.app.rotate(angle, anchor)

    def rotateBoundary(self, angle: float, anchor: AnchorPosition) -> None:
        """Rotates the boundary of the selection."""
        self.app.rotateBoundary(angle, anchor)

    def selectAll(self) -> None:
        self.app.selectAll()

    def stroke(
        self,
        strokeColor: SolidColor,
        width: int,
        location: StrokeLocation | None = None,
        mode: ColorBlendMode | None = None,
        opacity: int = 100,
        preserveTransparency: bool = False,
    ) -> None:
        """Strokes the selection.

        Args:
            strokeColor (SolidColor): The color to stroke the selection with.
            width (int): The stroke width.
            location (int): The stroke location.
            mode (int): The color blend mode.
            opacity (int): The opacity of the stroke color as a percentage.
                Range: 1 to 100.
            preserveTransparency (bool): If true, preserves transparency.

        """
        self.app.stroke(
            strokeColor, width, location, mode, opacity, preserveTransparency
        )

    def selectBorder(self, width: float) -> None:
        """Selects the selection border only (in the specified width);
        subsequent actions do not affect the selected area within the borders.

        Args:
            width (int): The width of the border selection.

        """
        self.app.selectBorder(width)

    def similar(self, tolerance: int, anti_alias: bool = True) -> None:
        self.app.similar(tolerance, anti_alias)

    def smooth(self, radius: int) -> None:
        """Cleans up stray pixels left inside or outside a color-based
        selection (within the radius specified in pixels)."""
        self.app.smooth(radius)

    def store(
        self, into: Channel, combination: SelectionType = SelectionType.ReplaceSelection
    ) -> None:
        """Saves the selection as a channel."""
        self.app.store(into, combination)

    def translate(self, deltaX: float = 0, deltaY: float = 0) -> None:
        """Moves the object relative to its current position."""
        self.app.translate(deltaX, deltaY)

    def translateBoundary(self, deltaX: float = 0, deltaY: float = 0) -> None:
        """Moves the boundary of selection relative to its current position."""
        self.app.translateBoundary(deltaX, deltaY)
