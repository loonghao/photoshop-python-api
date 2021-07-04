# Import local modules
from photoshop.api._core import Photoshop


class EPSOpenOptions(Photoshop):
    """Options for saving a document in EPS format.

    using the `Document.saveAs()`

    """

    object_name = "EPSOpenOptions"

    def __init__(self):
        super().__init__()

    @property
    def antiAlias(self):
        return self.app.antiAlias

    @property
    def constrainProportions(self):
        return self.app.constrainProportions

    @property
    def height(self):
        return self.app.height

    @property
    def mode(self):
        return self.app.mode

    @property
    def resolution(self):
        return self.app.resolution

    @property
    def width(self):
        return self.app.width

    @property
    def embedColorProfile(self):
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, boolean):
        self.app.embedColorProfile = boolean
