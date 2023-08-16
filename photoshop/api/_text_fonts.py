# Import third-party modules
from comtypes import ArgumentError

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.text_font import TextFont


class TextFonts(Photoshop):
    """An installed font."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def __iter__(self):
        for font in self.app:
            yield TextFont(font)

    def __getitem__(self, key: str):
        """Access a given TextFont using dictionary key lookup, must provide the postScriptName."""
        try:
            return TextFont(self.app[key])
        except ArgumentError:
            raise PhotoshopPythonAPIError(f'Could not find a font with postScriptName "{key}"')

    @property
    def _fonts(self):
        return [a for a in self.app]

    def __len__(self):
        return self.length

    @property
    def length(self):
        """The number pf elements in the collection."""
        return len(self._fonts)

    def getByName(self, name: str) -> TextFont:
        """Gets the font by the font name.

        Args:
            name: The name of the font.


        Returns:
            font instance.

        """
        for font in self.app:
            if font.name == name:
                return TextFont(font)
        raise PhotoshopPythonAPIError('Could not find a TextFont named "{name}"')
