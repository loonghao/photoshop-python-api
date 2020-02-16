from photoshop._core import Photoshop
from photoshop.colors.cmyk import CMYKColor
from photoshop.colors.hsb import HSBColor
from photoshop.colors.lab import LabColor
from photoshop.colors.rgb import RGBColor


class SolidColor(Photoshop):
    object_name = 'SolidColor'

    def __init__(self):
        super().__init__()

    @property
    def cmyk(self):
        return CMYKColor(self.app.cmyk)

    @property
    def gray(self):
        return self.app.gray

    @property
    def hsb(self):
        return HSBColor(self.app.hsb)

    @property
    def lab(self):
        return LabColor(self.app.lab)

    @property
    def model(self):
        return self.app.model

    @property
    def nearestWebColor(self):
        return self.app.NearestWebColor

    @property
    def rgb(self):
        return RGBColor(self.app.rgb)

    @property
    def isEqual(self, *args, **kwargs):
        return self.app.IsEqual(*args, **kwargs)
