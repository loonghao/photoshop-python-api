# Import built-in modules
from __future__ import annotations

from typing import Any, Union

# Import third-party modules
from comtypes import ArgumentError, COMError

# Import local modules
from photoshop.api._collection_base import CollectionBase
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.text_font import TextFont


class TextFonts(CollectionBase[TextFont]):
    """The collection of installed fonts in Photoshop.
    
    This class represents all the fonts installed in the system and available to
    Photoshop. It provides methods to:
    - Access fonts by name or postScriptName
    - Check if a font is installed
    - Iterate over all available fonts
    """
    
    """
    MAGIC METHODS
    """
    
    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        for font in self.app:
            yield self._wrap_item(font)

    def __contains__(self, name: str) -> bool:
        """Check if a font is installed. Lookup by font postScriptName (fastest) or name.
        
        Args:
            name: Name or postScriptName of the font to look for
            
        Returns:
            bool: True if font is found, otherwise False
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
            return self._wrap_item(self.app[key])
        except ArgumentError:
            raise PhotoshopPythonAPIError(f'Could not find a font with postScriptName "{key}"')

    """
    METHODS
    """
    
    def get(self, key: str, default: Any = None) -> Union[TextFont, Any]:
        """Get a font by its postScriptName, return default if not found.
        
        Args:
            key: The postScriptName of the font
            default: Value to return if font isn't found
            
        Returns:
            TextFont: The font if found, otherwise the default value
        """
        try:
            return self._wrap_item(self.app[key])
        except (KeyError, ArgumentError):
            return default

    def getByName(self, name: str) -> TextFont:
        """Get a font by its display name.
        
        Args:
            name: The display name of the font
            
        Returns:
            TextFont: The font with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no font with the specified name is found
        """
        for font in self:
            if font.name == name:
                return font
        raise PhotoshopPythonAPIError(f'Could not find a font named "{name}"')

    def _wrap_item(self, item: Any) -> TextFont:
        """Wrap a COM font object in a TextFont instance.
        
        Args:
            item: The COM font object to wrap
            
        Returns:
            TextFont: The wrapped font
        """
        return TextFont(item)

    """
    PROPERTIES
    """
    
    @property
    def length(self) -> int:
        """The number pf elements in the collection."""
        return len(self.app)
