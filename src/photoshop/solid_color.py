from photoshop._core import Photoshop
from photoshop.colors.cmyk import CMYKColor
from photoshop.colors.hsb import HSBColor
from photoshop.colors.lab import LabColor
from photoshop.colors.rgb import RGBColor


class SolidColor(Photoshop):
    object_name = 'SolidColor'

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Initialize color.
        self.rgb = RGBColor(self.app.rgb)
        self.cmyk = CMYKColor(self.app.cmyk)
        self.hsb = HSBColor(self.app.hsb)
        self.lab = LabColor(self.app.lab)

    @property
    def cmyk(self):
        """

        Returns:
            photoshop.colors.cmyk.CMYKColor:

        """
        return CMYKColor(self.app.cmyk)

    @cmyk.setter
    def cmyk(self, value):
        self.app.cmyk = value

    @property
    def gray(self):
        return self.app.gray

    @property
    def hsb(self):
        return HSBColor(self.app.hsb)

    @hsb.setter
    def hsb(self, value):
        self.app.hsb = value

    @property
    def lab(self):
        return LabColor(self.app.lab)

    @lab.setter
    def lab(self, value):
        self.app.lab = value

    @property
    def model(self):
        return self.app.model

    @property
    def nearestWebColor(self):
        return self.app.NearestWebColor

    @property
    def rgb(self):
        return RGBColor(self.app.rgb)

    @rgb.setter
    def rgb(self, value):
        self.app.rgb = value

    def isEqual(self, color):
        return self.app.isEqual(color)
