# Import local modules
from photoshop.api._core import Photoshop


class TextFont(Photoshop):
    """An installed font."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def family(self) -> str:
        """The font family"""
        return self.app.family

    @property
    def name(self) -> str:
        """The name of the font."""
        return self.app.name

    @property
    def postScriptName(self) -> str:
        """The PostScript name of the font."""
        return self.app.postScriptName

    @property
    def style(self) -> str:
        """The font style."""
        return self.app.style
