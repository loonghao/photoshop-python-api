# Import local modules
from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api._core import Core


class SolidColor(BasicOption, Core):
    object_name = 'SolidColor'

    def __int__(self):
        super(SolidColor, self).__init__()

    @property
    def CMYK(self):
        return self.app.CMYK

    @property
    def gray(self):
        return self.app.gray

    @property
    def hsb(self):
        return self.app.hsb

    @property
    def lab(self):
        return self.app.lab

    @property
    def model(self):
        return self.app.model

    @property
    def nearestWebColor(self):
        return self.app.nearestWebColor

    @property
    def RGB(self):
        return self.app.RGB

    @property
    def isEqual(self, *args, **kwargs):
        return self.app.isEqual(*args, **kwargs)
