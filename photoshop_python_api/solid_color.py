# Import local modules
from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api._core import Photoshop
from photoshop_python_api.cmyk_color import CMYKColor
from photoshop_python_api.rgb_color import RGBColor


class SolidColor(Photoshop):
    object_name = 'SolidColor'

    def __int__(self):
        super(SolidColor, self).__init__()

    # @property
    # def cmyk(self):
    #     return CMYKColor(self.app.CMYK)
    #
    # @property
    # def gray(self):
    #     return self.app.Gray
    #
    # @property
    # def hsb(self):
    #     return self.app.HSB
    #
    # @property
    # def lab(self):
    #     return self.app.Lab
    #
    # @property
    # def model(self):
    #     return self.app.model
    #
    # @property
    # def nearestWebColor(self):
    #     return self.app.NearestWebColor
    #
    # @property
    # def RGB(self):
    #     return RGBColor(self.app.RGB)
    #
    # @property
    # def isEqual(self, *args, **kwargs):
    #     return self.app.IsEqual(*args, **kwargs)

