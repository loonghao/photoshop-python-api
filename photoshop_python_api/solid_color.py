from photoshop_python_api._core import Photoshop
from photoshop_python_api.colors.cmyk_color import CMYKColor
from photoshop_python_api.colors.lab_color import LabColor
from photoshop_python_api.colors.rgb_color import RGBColor
from photoshop_python_api.colors.hsb import HSBColor


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
