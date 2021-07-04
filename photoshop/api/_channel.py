# Import local modules
from photoshop.api._core import Photoshop


# pylint: disable=too-many-public-methods
class Channel(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def color(self):
        return self.app.color

    @color.setter
    def color(self, value):
        self.app.color = value

    @property
    def histogram(self):
        return self.app.histogram

    @histogram.setter
    def histogram(self, value):
        self.app.histogram = value

    @property
    def kind(self):
        return self.app.kind

    @kind.setter
    def kind(self, value):
        self.app.kind = value

    @property
    def opacity(self):
        return self.app.opacity

    @opacity.setter
    def opacity(self, value):
        self.app.opacity = value

    @property
    def visible(self):
        return self.app.visible

    @visible.setter
    def visible(self, value):
        self.app.visible = value

    @property
    def name(self):
        return self.app.name

    def duplicate(self, targetDocument=None):
        self.app.duplicate(targetDocument)

    def merge(self):
        self.app.merge()

    def remove(self):
        channel = f'app.activeDocument.channels.getByName("{self.name}")'
        self.eval_javascript(f"{channel}.remove()")
