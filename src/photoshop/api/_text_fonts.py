# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.text_font import TextFont


class TextFonts(Photoshop):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def __iter__(self):
        for font in self.app:
            yield TextFont(font)

    @property
    def _fonts(self):
        return [a for a in self.app]

    def __len__(self):
        return self.length

    @property
    def length(self):
        """The number pf elements in the collection."""
        return len(self._fonts)

    def getByName(self, name):
        """Gets the font by the font name.

        Args:
            name (str): The name of the font.


        Returns:
            Font

        """
        for font in self.app:
            if font.name == name:
                return TextFont(font)
        raise PhotoshopPythonAPIError('Could not find a TextFont named "{name}"')
