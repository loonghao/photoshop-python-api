"""A record of key-value pairs for actions, such as those included on the
Adobe Photoshop Actions menu. The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide."""
from photoshop._core import Photoshop


class ActionDescriptor(Photoshop):
    object_name = 'ActionDescriptor'

    def __init__(self):
        super().__init__()

    @property
    def count(self):
        return self.app.count

    def clear(self):
        self.app.clear()

    def erase(self, key):
        return self.app.erase(key)

    def getBoolean(self, key):
        return self.app.getBoolean(key)

    def getClass(self, key):
        return self.app.getClass(key)

    def getDouble(self, key):
        return self.app.getDouble(key)

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

    def getTypeObject(self, index):
        return self.app.getTypeObject(index)

    def getObjectValue(self, index):
        return self.app.getObjectValue(index)

    def getPath(self, index):
        return self.app.getPath(index)

    def getReference(self, index):
        return self.app.getReference(index)

    def getString(self, index):
        return self.app.getString(index)

    def getType(self, index):
        return self.app.getType(index)

    def getUnitDoubleType(self, index):
        return self.app.getUnitDoubleType(index)

    def getUnitDoubleValue(self, index):
        return self.app.getUnitDoubleValue(index)

    def putBoolean(self, key, value):
        self.app.putBoolean(key, value)

    def putClass(self, value):
        self.app.putClass(value)

    def putDouble(self, key, value):
        return self.app.putDouble(key, value)

    def putEnumerated(self, DesiredClass, EnumType, Value):
        return self.app.putEnumerated(DesiredClass, EnumType, Value)

    def putReference(self, key, value):
        return self.app.putReference(key, value)

    def putObject(self, key, classID, value):
        return self.app.putObject(key, classID, value)
