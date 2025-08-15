# Import built-in modules
from pathlib import Path
from typing import TYPE_CHECKING

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.action_reference import ActionReference
from photoshop.api.enumerations import DescValueType


if TYPE_CHECKING:
    # Import local modules
    from photoshop.api.action_descriptor import ActionDescriptor
    from photoshop.api.action_list import ActionList


class BaseAction(Photoshop):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "clear",
            "getBoolean",
            "getClass",
            "getData",
            "getDouble",
            "getEnumerationType",
            "getEnumerationValue",
            "getInteger",
            "getKey",
            "getLargeInteger",
            "getList",
            "getObjectType",
            "getObjectValue",
            "getPath",
            "getReference",
            "getString",
            "getType",
            "getUnitDoubleType",
            "getUnitDoubleValue",
        )

    @property
    def count(self) -> int:
        """The number of keys contained in the descriptor."""
        return self.app.count

    def clear(self) -> None:
        """Clears the descriptor."""
        self.app.clear()

    def getBoolean(self, key: int) -> bool:
        """Gets the text_font of a key of type boolean.

        Args:
            key (str): key of type boolean.

        Returns:
            bool: The text_font of a key of type boolean.

        """
        return self.app.getBoolean(key)

    def getClass(self, key: int) -> int:
        """Gets the text_font of a key of type class.

        Args:
            key (str): The key of type class.

        Returns:
            int: The text_font of a key of type class.

        """
        return self.app.getClass(key)

    def getData(self, key: int) -> str:
        """Gets raw byte data as a string value."""
        return self.app.getData(key)

    def getDouble(self, key: int) -> float:
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

    def getList(self, index: int) -> "ActionList":
        """Gets the value of a key of type list."""
        # Import local modules
        from photoshop.api.action_list import ActionList

        return ActionList(self.app.getList(index))

    def getObjectType(self, key: int) -> int:
        """Gets the class ID of an object in a key of type object."""
        return self.app.getObjectType(key)

    def getObjectValue(self, key: int) -> "ActionDescriptor":
        """Get the class ID of an object in a key of type object."""
        from .action_descriptor import ActionDescriptor

        return ActionDescriptor(self.app.getObjectValue(key))

    def getPath(self, key: int) -> Path:
        """Gets the value of a key of type File."""
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

    def getUnitDoubleValue(self, key: int) -> float:
        """Gets the unit type of a key of type UnitDouble."""
        return self.app.getUnitDoubleValue(key)

    def hasKey(self, key: int) -> bool:
        """Checks whether the descriptor contains the provided key."""
        return self.app.hasKey(key)
