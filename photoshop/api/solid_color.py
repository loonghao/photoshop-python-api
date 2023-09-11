"""A color definition used in the document.

Maps a color to equivalents in all available color models.

- Used in `Application.backgroundColor` and `foregroundColor` properties, in
`Channel.color`, in `ColorSampler.color`, and in `TextItem.color`
- Passed to `PathItem.fillPath()`, `Selection.fill()`, and `Selection.stroke()`.

"""

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.colors.cmyk import CMYKColor
from photoshop.api.colors.gray import GrayColor
from photoshop.api.colors.hsb import HSBColor
from photoshop.api.colors.lab import LabColor
from photoshop.api.colors.rgb import RGBColor
from photoshop.api.enumerations import ColorModel


class SolidColor(Photoshop):
    """A color definition used in the document."""

    object_name = "SolidColor"

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._flag_as_method(
            "isEqual",
        )

    @property
    def cmyk(self) -> CMYKColor:
        """The CMYK color mode.

        Returns:
            .colors.cmyk.CMYKColor:

        """
        return CMYKColor(self.app.cmyk)

    @cmyk.setter
    def cmyk(self, value: CMYKColor):
        self.app.cmyk = value

    @property
    def gray(self) -> GrayColor:
        return GrayColor(self.app.gray)

    @property
    def hsb(self) -> HSBColor:
        return HSBColor(self.app.hsb)

    @hsb.setter
    def hsb(self, value: HSBColor):
        self.app.hsb = value

    @property
    def lab(self) -> LabColor:
        return LabColor(self.app.lab)

    @lab.setter
    def lab(self, value: LabColor):
        self.app.lab = value

    @property
    def model(self) -> ColorModel:
        """The color model."""
        return ColorModel(self.app.model)

    @model.setter
    def model(self, value: ColorModel):
        """The color model."""
        self.app.model = value

    @property
    def nearestWebColor(self) -> RGBColor:
        """The nearest web color to the current color."""
        return RGBColor(self.app.NearestWebColor)

    @property
    def rgb(self) -> RGBColor:
        """The RGB color mode."""
        return RGBColor(self.app.rgb)

    @rgb.setter
    def rgb(self, value: RGBColor):
        self.app.rgb = value

    def isEqual(self, color: RGBColor):
        """`SolidColor` object is visually equal to the specified color."""
        return self.app.isEqual(color)
