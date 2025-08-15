# Import built-in modules
from typing import Iterator
from typing import TypeVar
from typing import overload

# Import third-party modules
from comtypes import ArgumentError
from comtypes import COMError

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.text_font import TextFont


T = TypeVar("T")


class TextFonts(Photoshop):
    """An installed font."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    """
    MAGIC METHODS
    """

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator[TextFont]:
        for font in self.app:
            yield TextFont(font)

    def __contains__(self, name: str) -> bool:
        """Check if a font is installed. Lookup by font postScriptName (fastest) or name.

        Args:
            name: Name or postScriptName of the font to look for.

        Returns:
            bool: True if font is found, otherwise False.
        """
        # Look for postScriptName
        if self.get(name):
            return True
        # Look for name (slow)
        for font in self:
            try:
                if font.name == name:
                    return True
            except COMError:
                continue
        return False

    def __getitem__(self, key: str) -> TextFont:
        """Access a given TextFont using dictionary key lookup, must provide the postScriptName.

        Args:
            key: The postScriptName of the font.

        Returns:
            TextFont instance.

        """
        try:
            return TextFont(self.app[key])
        except ArgumentError:
            raise PhotoshopPythonAPIError(f'Could not find a font with postScriptName "{key}"')

    """
    METHODS
    """

    @overload
    def get(self, key: str, default: T) -> TextFont | T:
        ...

    @overload
    def get(self, key: str) -> TextFont | None:
        ...

    def get(self, key: str, default: T | None = None) -> TextFont | T | None:
        """
        Accesses a given TextFont using dictionary key lookup of postScriptName, returns default if not found.

        Args:
            key: The postScriptName of the font.
            default: Value to return if font isn't found.

        Returns:
            TextFont instance.

        """
        try:
            return TextFont(self.app[key])
        except (KeyError, ArgumentError):
            return default

    def getByName(self, name: str) -> TextFont | None:
        """Gets the font by the font name.

        Args:
            name: The name of the font.


        Returns:
            font instance.

        """
        for font in self.app:
            if font.name == name:
                return TextFont(font)

    """
    PROPERTIES
    """

    @property
    def length(self) -> int:
        """The number pf elements in the collection."""
        return len(list(self.app))
