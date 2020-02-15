from photoshop_python_api._core import Photoshop


class SolidColor(Photoshop):
    object_name = 'SolidColor'

    def __init__(self):
        super().__init__()

    @property
    def cmyk(self):
        return self.app.cmyk

    @property
    def gray(self):
        return self.app.gray

    @property
    def hsb(self):
        return self.app.hbs

    @property
    def lab(self):
        return self.app.lab

    @property
    def model(self):
        return self.app.model

    @property
    def nearestWebColor(self):
        return self.app.NearestWebColor

    @property
    def rgb(self):
        return self.app.rgb

    @property
    def isEqual(self, *args, **kwargs):
        return self.app.IsEqual(*args, **kwargs)
