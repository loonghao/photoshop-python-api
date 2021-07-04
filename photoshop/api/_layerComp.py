# Import local modules
from photoshop.api._core import Photoshop


class LayerComp(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    @property
    def appearance(self):
        return self.app.appearance

    @appearance.setter
    def appearance(self, value):
        self.app.appearance = value

    @property
    def childLayerCompState(self):
        return self.app.childLayerCompState

    @childLayerCompState.setter
    def childLayerCompState(self, value):
        self.app.childLayerCompState = value

    @property
    def comment(self):
        return self.app.comment

    @comment.setter
    def comment(self, text):
        self.app.comment = text

    @property
    def name(self):
        return self.app.name

    @name.setter
    def name(self, text):
        self.app.name = text

    @property
    def parent(self):
        return self.app.parent

    @property
    def position(self):
        return self.app.position

    @position.setter
    def position(self, value):
        self.app.position = value

    @property
    def selected(self):
        """True if the layer comp is currently selected."""
        return self.app.selected

    @selected.setter
    def selected(self, value):
        self.app.selected = value

    @property
    def typename(self):
        return self.app.typename

    @property
    def visibility(self):
        """True to use layer visibility settings."""
        return self.app.visibility

    @visibility.setter
    def visibility(self, value):
        self.app.visibility = value

    def apply(self):
        """Applies the layer comp to the document."""
        self.app.apply()

    def recapture(self):
        """Recaptures the current layer state(s) for this layer comp."""
        self.app.recapture()

    def remove(self):
        """Deletes the layerComp object."""
        self.app.remove()

    def resetfromComp(self):
        """Resets the layer comp state to thedocument state."""
        self.app.resetfromComp()
