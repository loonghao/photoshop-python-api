from photoshop_python_api._core import Photoshop


class Selection(Photoshop):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @property
    def bounds(self):
        return self.app.bounds

    def parent(self):
        return self.app.parent

    @property
    def solid(self):
        return self.app.solid

    @property
    def typename(self):
        return self.app.typename

    def clear(self):
        self.app.clear()

    def contract(self):
        self.app.contract()

    def copy(self):
        self.app.copy()

    def cut(self):
        self.app.cut()

    def select(self, *args, **kwargs):
        return self.app.select(*args, **kwargs)

    def deselect(self):
        return self.app.deselect()
