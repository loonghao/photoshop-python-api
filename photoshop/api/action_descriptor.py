"""A record of key-text_font pairs for actions.

such as those included on the Adobe Photoshop Actions menu.
The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""

# Import local modules
from os import PathLike

from photoshop.api._core import Photoshop
from photoshop.api.action_list import ActionList
from photoshop.api.action_reference import ActionReference
from photoshop.api.base_action import BaseAction


class ActionDescriptor(BaseAction):
    """A record of key-value pairs for actions, such as those included on the Adobe Photoshop Actions menu.

    The ActionDescriptor class is part of the Action Manager functionality.
    For more details on the Action Manager, see the Photoshop Scripting Guide.

    """

    object_name = "ActionDescriptor"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "erase",
            "fromStream",
            "hasKey",
            "isEqual",
            "putBoolean",
            "putClass",
            "putData",
            "putDouble",
            "putEnumerated",
            "putInteger",
            "putLargeInteger",
            "putList",
            "putObject",
            "putPath",
            "putReference",
            "putString",
            "putUnitDouble",
            "toSteadm",
        )

    def erase(self, key: int) -> None:
        """Erases a key form the descriptor."""
        self.app.erase(key)

    def fromStream(self, value: str) -> None:
        """Create a descriptor from a stream of bytes,
        for reading from disk."""
        self.app.fromStream(value)

    def hasKey(self, key: int) -> bool:
        """Checks whether the descriptor contains the provided key."""
        return self.app.hasKey(key)

    def isEqual(self, otherDesc: "ActionDescriptor") -> bool:
        """Determines whether the descriptor is the same as another descriptor.

        Args:
            otherDesc (.action_descriptor.ActionDescriptor):

        """
        return self.app.isEqual(otherDesc)

    def putBoolean(self, key: int, value: bool) -> None:
        """Sets the value for a key whose type is boolean."""
        self.app.putBoolean(key, value)

    def putClass(self, key: int, value: int) -> None:
        """Sets the value for a key whose type is class."""
        self.app.putClass(key, value)

    def putData(self, key: int, value: str) -> None:
        """Puts raw byte data as a string value."""
        self.app.putData(key, value)

    def putDouble(self, key: int, value: float) -> None:
        """Sets the value for a key whose type is double."""
        self.app.putDouble(key, value)

    def putEnumerated(self, key: int, enum_type: int, value: int) -> None:
        """Sets the enumeration type and value for a key."""
        self.app.putEnumerated(key, enum_type, value)

    def putInteger(self, key: int, value: int) -> None:
        """Sets the value for a key whose type is integer."""
        self.app.putInteger(key, value)

    def putLargeInteger(self, key: int, value: int) -> None:
        """Sets the value for a key whose type is large integer."""
        self.app.putLargeInteger(key, value)

    def putList(self, key: int, value: "ActionList") -> None:
        """Sets the value for a key whose type is an ActionList object."""
        self.app.putList(key, value)

    def putObject(self, key: int, class_id: int, value: "ActionDescriptor") -> None:
        """Sets the value for a key whose type is an object."""
        self.app.putObject(key, class_id, value)

    def putPath(self, key: int, value: str | PathLike[str]) -> None:
        """Sets the value for a key whose type is path."""
        self.app.putPath(key, str(value))

    def putReference(self, key: int, value: ActionReference) -> None:
        """Sets the value for a key whose type is an object reference."""
        self.app.putReference(key, value)

    def putString(self, key: int, value: str) -> None:
        """Sets the value for a key whose type is string."""
        self.app.putString(key, value)

    def putUnitDouble(self, key: int, unit_id: int, value: float) -> None:
        """Sets the value for a key whose type is a unit value formatted as
        double."""
        self.app.putUnitDouble(key, unit_id, value)

    def toStream(self) -> str:
        """Gets the entire descriptor as as stream of bytes,
        for writing to disk."""
        return self.app.toSteadm()
