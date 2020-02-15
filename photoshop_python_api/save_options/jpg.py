# Import local modules
from photoshop_python_api._core import Photoshop


class JPEGSaveOptions(Photoshop):
    object_name = 'JPEGSaveOptions'

    def __init__(self):
        super().__init__()
        print()
        # print(self.)

    @property
    def quality(self):
        return self.app.quality

    @quality.setter
    def quality(self, value):
        self.app.quality = value

    @property
    def formatOptions(self):
        """The download format to use."""
        return self.app.formatOptions

    @property
    def matte(self):
        """The color to use to fill anti-aliased edges adjacent to transparent
        areas of the image. Default: white.

        References:
            https://theiviaxx.github.io/photoshop-docs/Photoshop/JPEGSaveOptions/matte.html#jpegsaveoptions-matte

        """
        return self.app.matte

    @property
    def scans(self):
        return self.app.scans
