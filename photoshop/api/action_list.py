"""This object provides an array-style mechanism for storing data.

It can be used for low-level access info Photoshop.


"""

# Import local modules
from os import PathLike
from typing import TYPE_CHECKING

from photoshop.api._core import Photoshop
from photoshop.api.action_reference import ActionReference
from photoshop.api.base_action import BaseAction

if TYPE_CHECKING:
    from photoshop.api.action_descriptor import ActionDescriptor


class ActionList(BaseAction):
    """The list of commands that comprise an Action.

    (such as an Action created using the Actions palette in the Adobe Photoshop application).
    The action list object is part of the Action Manager functionality.
    For details on using the Action Manager, see the Photoshop Scripting Guide.

    """

    object_name = "ActionList"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
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

    def putBoolean(self, value: bool) -> None:
        """Sets the value for a key whose type is boolean."""
        self.app.putBoolean(value)

    def putClass(self, value: int) -> None:
        """Sets the value for a key whose type is class."""
        self.app.putClass(value)

    def putData(self, value: str) -> None:
        """Puts raw byte data as a string value."""
        self.app.putData(value)

    def putDouble(self, value: float) -> None:
        """Sets the value for a key whose type is double."""
        self.app.putDouble(value)

    def putEnumerated(self, enum_type: int, value: int) -> None:
        """Sets the enumeration type and value for a key."""
        self.app.putEnumerated(enum_type, value)

    def putInteger(self, value: int) -> None:
        """Sets the value for a key whose type is integer."""
        self.app.putInteger(value)

    def putLargeInteger(self, value: int) -> None:
        """Sets the value for a key whose type is large integer."""
        self.app.putLargeInteger(value)

    def putList(self, value: "ActionList") -> None:
        """Sets the value for a key whose type is an ActionList object."""
        self.app.putList(value)

    def putObject(self, class_id: int, value: "ActionDescriptor") -> None:
        """Sets the value for a key whose type is an object."""
        self.app.putObject(class_id, value)

    def putPath(self, value: str | PathLike[str]) -> None:
        """Sets the value for a key whose type is path."""
        self.app.putPath(str(value))

    def putReference(self, value: ActionReference) -> None:
        """Sets the value for a key whose type is an object reference."""
        self.app.putReference(value)

    def putString(self, value: str) -> None:
        """Sets the value for a key whose type is string."""
        self.app.putString(value)

    def putUnitDouble(self, unit_id: int, value: float) -> None:
        """Sets the value for a key whose type is a unit value formatted as
        double."""
        self.app.putUnitDouble(unit_id, value)

    def toStream(self) -> str:
        """Gets the entire descriptor as as stream of bytes,
        for writing to disk."""
        return self.app.toSteadm()
