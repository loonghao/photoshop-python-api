# Import local modules
from photoshop._core import Photoshop


class EPSSaveOptions(Photoshop):
    """Options for saving a document in EPS format.

    using the `Document.saveAs()`

    """

    object_name = "EPSSaveOptions"

    def __init__(self):
        super().__init__()

    @property
    def embedColorProfile(self):
        return self.app.embedColorProfile

    @embedColorProfile.setter
    def embedColorProfile(self, boolean):
        self.app.embedColorProfile = boolean
