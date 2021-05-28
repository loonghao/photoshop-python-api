"""Options for saving a document in BMO format."""
# Import local modules
from photoshop.api._core import Photoshop


class BMPSaveOptions(Photoshop):
    object_name = "BMPSaveOptions"

    def __init__(self):
        super().__init__()

    @property
    def alphaChannels(self):
        """State to save the alpha channels."""
        return self.app.alphaChannels

    @alphaChannels.setter
    def alphaChannels(self, value):
        """Sets whether to save the alpha channels or not.

        Args:

        """
        self.app.alphaChannels = value
