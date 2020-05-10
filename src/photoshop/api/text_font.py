from ._core import Photoshop


class TextFont(Photoshop):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @property
    def family(self):
        return self.app.family

    @property
    def name(self):
        return self.app.name

    @property
    def postScriptName(self):
        return self.app.postScriptName

    @property
    def style(self):
        return self.app.style
