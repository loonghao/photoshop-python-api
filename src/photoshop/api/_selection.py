# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ColorBlendMode
from photoshop.api.enumerations import SelectionType
from photoshop.api.solid_color import SolidColor


# pylint: disable=too-many-public-methods, too-many-arguments
class Selection(Photoshop):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @property
    def bounds(self):
        return self.app.bounds

    def parent(self):
        return self.app.parent

    @property
    def solid(self):
        return self.app.solid

    @property
    def typename(self):
        return self.app.typename

    def clear(self):
        self.app.clear()

    def contract(self):
        self.app.contract()

    def copy(self):
        self.app.copy()

    def cut(self):
        self.app.cut()

    def select(self, *args, **kwargs):
        return self.app.select(*args, **kwargs)

    def deselect(self):
        return self.app.deselect()

    def expand(self, by):
        """Expands the selection.

        Args:
            by (int): The amount to expand the selection.

        """
        self.app.expand(by)

    def feather(self, by):
        """Feathers the edges of the selection.

        Args:
            by (int): The amount to feather the edge.

        """
        return self.app.feather(by)

    def fill(
        self,
        fill_type: SolidColor,
        mode: ColorBlendMode = None,
        opacity=None,
        preserve_transparency=None,
    ):
        """Fills the selection."""
        return self.app.fill(fill_type, mode, opacity, preserve_transparency)

    def grow(self, tolerance, anti_alias):
        """Grows the selection to include all adjacent pixels falling within

        The specified tolerance range.

        Args:
            tolerance (int): The tolerance range. Range: 0 to 255.
            anti_alias (bool): If true, anti-aliasing is used.


        """
        return self.app.grow(tolerance, anti_alias)

    def invert(self):
        """Inverts the selection."""
        self.app.invert()

    def load(self, from_channel, combination, inverting):
        """Loads the selection from the specified channel."""
        return self.app.load(from_channel, combination, inverting)

    def makeWorkPath(self, tolerance):
        """Makes this selection item the workpath for this document."""
        self.app.makeWorkPath(tolerance)

    def resize(self, horizontal, vertical, anchor):
        """Resizes the selected area to the specified dimensions and anchor
        position."""
        self.app.resize(horizontal, vertical, anchor)

    def resizeBoundary(self, horizontal, vertical, anchor):
        """Scales the boundary of the selection."""
        self.app.resizeBoundary(horizontal, vertical, anchor)

    def rotate(self, angle, anchor):
        """Rotates the object."""
        self.app.rotate(angle, anchor)

    def rotateBoundary(self, angle, anchor):
        """Rotates the boundary of the selection."""
        self.app.rotateBoundary(angle, anchor)

    def stroke(self, strokeColor, width, location, mode, opacity, preserveTransparency):
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
        return self.app.stroke(
            strokeColor, width, location, mode, opacity, preserveTransparency
        )

    def selectBorder(self, width):
        """Selects the selection border only (in the specified width);
        subsequent actions do not affect the selected area within the borders.

        Args:
            width (int): The width of the border selection.

        """
        return self.app.selectBorder(width)

    def similar(self, tolerance, antiAlias):
        return self.app.similar(tolerance, antiAlias)

    def smooth(self, radius):
        """Cleans up stray pixels left inside or outside a color-based
        selection (within the radius specified in pixels)."""
        return self.app.smooth(radius)

    def store(self, into, combination=SelectionType.ReplaceSelection):
        """Saves the selection as a channel."""
        return self.app.store(into, combination)

    def translate(self, deltaX, deltaY):
        """Moves the object relative to its current position."""
        return self.app.translate(deltaX, deltaY)

    def translateBoundary(self, deltaX, deltaY):
        """Moves the boundary of selection relative to its current position."""
        return self.app.translateBoundary(deltaX, deltaY)
