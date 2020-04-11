"""A record of key-text_font pairs for actions.

such as those included on the Adobe Photoshop Actions menu.
The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""
from photoshop._core import Photoshop


class ActionDescriptor(Photoshop):
    object_name = 'ActionDescriptor'

    def __init__(self):
        super().__init__()

    @property
    def count(self):
        return self.app.count

    def clear(self):
        """Clears the descriptor."""
        self.app.clear()

    def erase(self, key):
        """Erases a key form the descriptor."""
        self.app.erase(key)

    def fromStream(self, value):
        """Create a descriptor from a stream of bytes.

        for reading from disk.

        """
        self.app.fromStream(value)

    def getBoolean(self, key):
        """Gets the text_font of a key of type boolean.

        Args:
            key (str): key of type boolean.

        Returns:
            bool: The text_font of a key of type boolean.

        """
        return self.app.getBoolean(key)

    def getClass(self, key):
        """Gets the text_font of a key of type class.

        Args:
            key (str): The key of type class.

        Returns:
            int: The text_font of a key of type class.

        """
        return self.app.getClass(key)

    def getData(self, key):
        return self.app.getData(key)

    def getDouble(self, key):
        return self.app.getDouble(key)

    def getEnumerationType(self, index):
        return self.app.getEnumerationType(index)

    def getEnumerationValue(self, index):
        return self.app.getEnumerationValue(index)

    def getInteger(self, index):
        return self.app.getInteger(index)

    def getKey(self, index):
        return self.app.getKey(index)

    def getLargeInteger(self, index):
        return self.app.getLargeInteger(index)

    def getList(self, index):
        return self.app.getList(index)

    def getObjectType(self, key):
        return self.app.getObjectType(key)

    def getObjectValue(self, key):
        return self.app.getObjectValue(key)

    def getPath(self, key):
        return self.app.getPath(key)

    def getReference(self, key):
        return self.app.getReference(key)

    def getString(self, key):
        return self.app.getString(key)

    def getType(self, key):
        return self.app.getType(key)

    def getUnitDoubleType(self, key):
        return self.app.getUnitDoubleType(key)

    def getUnitDoubleValue(self, key):
        return self.app.getUnitDoubleValue(key)

    def hasKey(self, key):
        return self.app.hasKey(key)

    def isEqual(self, otherDesc):
        """

        Args:
            otherDesc (photoshop.action_descriptor.ActionDescriptor):

        Returns:

        """
        return self.app.isEqual(otherDesc)

    def putBoolean(self, key, value):
        self.app.putBoolean(key, value)

    def putClass(self, value):
        self.app.putClass(value)

    def putDouble(self, key, value):
        self.app.putDouble(key, value)

    def putEnumerated(self, key, enum_type, value):
        self.app.putEnumerated(key, enum_type, value)

    def putInteger(self, key, value):
        self.app.putInteger(key, value)

    def putLargeInteger(self, key, value):
        self.app.putLargeInteger(key, value)

    def putList(self, key, value):
        self.app.putList(key, value)

    def putObject(self, key, class_id, value):
        self.app.putObject(key, class_id, value)

    def putPath(self, key, value):
        self.app.putPath(key, value)

    def putReference(self, key, value):
        self.app.putReference(key, value)

    def putString(self, key, value):
        self.app.putString(key, value)

    def putUnitDouble(self, key, value):
        self.app.putUnitDouble(key, value)

    def toStream(self):
        """Gets the entire descriptor as as stream of bytes,
        for writing to disk."""
        return self.app.toSteadm()
