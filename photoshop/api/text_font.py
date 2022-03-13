# Import local modules
from photoshop.api._core import Photoshop


class TextFont(Photoshop):
    """An installed font."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @property
    def family(self) -> str:
        """The font family"""
        return self.app.family

    @property
    def name(self):
        """The name of the font."""
        return self.app.name

    @property
    def postScriptName(self):
        """The PostScript name of the font."""
        return self.app.postScriptName

    @property
    def style(self):
        """The font style."""
        return self.app.style
