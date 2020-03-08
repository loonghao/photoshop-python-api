from photoshop._core import Photoshop


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

    def fill(self, fillType, mode, opacity, preserveTransparency):
        """Fills the selection.

        Args:
            fillType (str): The color or history state with which to fill the
                object.
            mode (): The color blend mode.
            opacity (int): The opacity as a percentage. Range: 1 to 100.
            preserveTransparency (bool): If true, perserves transparencies.

        """
        return self.app.fill(fillType, mode, opacity, preserveTransparency)

    def grow(self, tolerance, antiAlias):
        """Grows the selection to include all adjacent pixels falling within

        the specified tolerance range.

        Args:
            tolerance (int): The tolerance range. Range: 0 to 255.
            antiAlias (bool): If true, anti-aliasing is used.


        """
        return self.app.grow(tolerance, antiAlias)

    def stroke(self, strokeColor, width, location, mode, opacity,
               preserveTransparency):
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
        return self.app.stroke(strokeColor, width, location, mode, opacity,
                               preserveTransparency)

    def selectBorder(self, width):
        """Selects the selection border only (in the specified width);
        subsequent actions do not affect the selected area within the borders.

        Args:
            width (int): The width of the border selection.

        """
        return self.app.selectBorder(width)
