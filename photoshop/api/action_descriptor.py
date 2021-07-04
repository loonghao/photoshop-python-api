"""A record of key-text_font pairs for actions.

such as those included on the Adobe Photoshop Actions menu.
The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""

# Import built-in modules
from pathlib import Path

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.action_list import ActionList
from photoshop.api.action_reference import ActionReference
from photoshop.api.enumerations import DescValueType


class ActionDescriptor(Photoshop):
    object_name = "ActionDescriptor"

    def __init__(self):
        super().__init__()

    @property
    def count(self):
        """The number of keys contained in the descriptor."""
        return self.app.count

    def clear(self):
        """Clears the descriptor."""
        self.app.clear()

    def erase(self, key: int):
        """Erases a key form the descriptor."""
        self.app.erase(key)

    def fromStream(self, value: str):
        """Create a descriptor from a stream of bytes.

        for reading from disk.

        """
        self.app.fromStream(value)

    def getBoolean(self, key: int) -> int:
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

    def getData(self, key: int) -> int:
        """Gets raw byte data as a string value."""
        return self.app.getData(key)

    def getDouble(self, key: int) -> int:
        """Gets the value of a key of type double."""
        return self.app.getDouble(key)

    def getEnumerationType(self, index: int) -> int:
        """Gets the enumeration type of a key."""
        return self.app.getEnumerationType(index)

    def getEnumerationValue(self, index: int) -> int:
        """Gets the enumeration value of a key."""
        return self.app.getEnumerationValue(index)

    def getInteger(self, index: int) -> int:
        """Gets the value of a key of type integer."""
        return self.app.getInteger(index)

    def getKey(self, index: int) -> int:
        """Gets the ID of the key provided by index."""
        return self.app.getKey(index)

    def getLargeInteger(self, index: int) -> int:
        """Gets the value of a key of type large integer."""
        return self.app.getLargeInteger(index)

    def getList(self, index: int) -> ActionList:
        """Gets the value of a key of type list."""
        return ActionList(self.app.getList(index))

    def getObjectType(self, key: int) -> int:
        """Gets the class ID of an object in a key of type object."""
        return self.app.getObjectType(key)

    def getObjectValue(self, key: int) -> int:
        """Get the class ID of an object in a key of type object."""
        return self.app.getObjectValue(key)

    def getPath(self, key: int) -> Path:
        """Gets the value of a key of type."""
        return Path(self.app.getPath(key))

    def getReference(self, key: int) -> ActionReference:
        """Gets the value of a key of type."""
        return ActionReference(self.app.getReference(key))

    def getString(self, key: int) -> str:
        """Gets the value of a key of type."""
        return self.app.getString(key)

    def getType(self, key: int) -> DescValueType:
        """Gets the type of a key."""
        return DescValueType(self.app.getType(key))

    def getUnitDoubleType(self, key: int) -> int:
        """Gets the unit type of a key of type UnitDouble."""
        return self.app.getUnitDoubleType(key)

    def getUnitDoubleValue(self, key: int) -> int:
        """Gets the unit type of a key of type UnitDouble."""
        return self.app.getUnitDoubleValue(key)

    def hasKey(self, key: int) -> bool:
        """Checks whether the descriptor contains the provided key."""
        return self.app.hasKey(key)

    def isEqual(self, otherDesc) -> bool:
        """Determines whether the descriptor is the same as another descriptor.

        Args:
            otherDesc (.action_descriptor.ActionDescriptor):

        """
        return self.app.isEqual(otherDesc)

    def putBoolean(self, key: int, value: bool):
        """Sets the value for a key whose type is boolean."""
        self.app.putBoolean(key, value)

    def putClass(self, key: int, value: int):
        """Sets the value for a key whose type is class."""
        self.app.putClass(key, value)

    def putData(self, key: int, value: str):
        """Puts raw byte data as a string value."""
        self.app.putData(key, value)

    def putDouble(self, key: int, value: int):
        """Sets the value for a key whose type is double."""
        self.app.putDouble(key, value)

    def putEnumerated(self, key: int, enum_type: int, value: int):
        """Sets the enumeration type and value for a key."""
        self.app.putEnumerated(key, enum_type, value)

    def putInteger(self, key: int, value: int):
        """Sets the value for a key whose type is integer."""
        self.app.putInteger(key, value)

    def putLargeInteger(self, key: int, value: int):
        """Sets the value for a key whose type is large integer."""
        self.app.putLargeInteger(key, value)

    def putList(self, key: int, value: ActionList):
        """Sets the value for a key whose type is an ActionList object."""
        self.app.putList(key, value)

    def putObject(self, key: int, class_id: int, value):
        """Sets the value for a key whose type is an object."""
        self.app.putObject(key, class_id, value)

    def putPath(self, key: int, value: str):
        """Sets the value for a key whose type is path."""
        self.app.putPath(key, value)

    def putReference(self, key: int, value: ActionReference):
        """Sets the value for a key whose type is an object reference."""
        self.app.putReference(key, value)

    def putString(self, key: int, value: str):
        """Sets the value for a key whose type is string."""
        self.app.putString(key, value)

    def putUnitDouble(self, key: int, unit_id: int, value: int):
        """Sets the value for a key whose type is a unit value formatted as
        double."""
        self.app.putUnitDouble(key, unit_id, value)

    def toStream(self) -> str:
        """Gets the entire descriptor as as stream of bytes,
        for writing to disk."""
        return self.app.toSteadm()
