"""This object provides an array-style mechanism for storing data.

It can be used for low-level access info Photoshop.


"""
# Import local modules
from photoshop.api._core import Photoshop


class ActionList(Photoshop):
    object_name = "ActionList"

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    @property
    def count(self):
        return self.app.count

    def getBoolean(self, index):
        return self.app.getBoolean(index)

    def getClass(self, index):
        return self.app.getClass(index)

    def getData(self, index):
        return self.app.getData(index)

    def getDouble(self, index):
        return self.app.getDouble(index)

    def getEnumerationType(self, index):
        return self.app.getEnumerationType(index)

    def getEnumerationValue(self, index):
        return self.app.getEnumerationValue(index)

    def getInteger(self, index):
        return self.app.getInteger(index)

    def getLargeInteger(self, index):
        return self.app.getLargeInteger(index)

    def getList(self, index):
        return self.app.getList(index)

    def getObjectType(self, index):
        return self.app.getObjectType(index)
