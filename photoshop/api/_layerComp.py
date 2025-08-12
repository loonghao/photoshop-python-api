# Import local modules
from typing import TYPE_CHECKING

from photoshop.api._core import Photoshop

if TYPE_CHECKING:
    from photoshop.api._document import Document


class LayerComp(Photoshop):
    """A snapshot of a state of the layers in a document (can be used to view different page layouts or compostions)."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "apply",
            "recapture",
            "remove",
            "resetfromComp",
        )

    @property
    def appearance(self) -> bool:
        return self.app.appearance

    @appearance.setter
    def appearance(self, value: bool) -> None:
        self.app.appearance = value

    @property
    def childLayerCompState(self) -> bool:
        return self.app.childLayerCompState

    @childLayerCompState.setter
    def childLayerCompState(self, value: bool) -> None:
        self.app.childLayerCompState = value

    @property
    def comment(self) -> str:
        return self.app.comment

    @comment.setter
    def comment(self, text: str) -> None:
        self.app.comment = text

    @property
    def name(self) -> str:
        return self.app.name

    @name.setter
    def name(self, text: str) -> None:
        self.app.name = text

    @property
    def parent(self) -> "Document":
        from ._document import Document

        return Document(self.app.parent)

    @property
    def position(self) -> bool:
        return self.app.position

    @position.setter
    def position(self, value: bool) -> None:
        self.app.position = value

    @property
    def selected(self) -> bool:
        """True if the layer comp is currently selected."""
        return self.app.selected

    @selected.setter
    def selected(self, value: bool) -> None:
        self.app.selected = value

    @property
    def visibility(self) -> bool:
        """True to use layer visibility settings."""
        return self.app.visibility

    @visibility.setter
    def visibility(self, value: bool) -> None:
        self.app.visibility = value

    def apply(self) -> None:
        """Applies the layer comp to the document."""
        self.app.apply()

    def recapture(self) -> None:
        """Recaptures the current layer state(s) for this layer comp."""
        self.app.recapture()

    def remove(self) -> None:
        """Deletes the layerComp object."""
        self.app.remove()

    def resetfromComp(self) -> None:
        """Resets the layer comp state to thedocument state."""
        self.app.resetfromComp()
