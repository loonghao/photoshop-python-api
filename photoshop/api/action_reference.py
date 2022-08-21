"""This object provides information about what the action is refering to.

For example, when referring to the name of something you might use keyName.
The reference would also need to know what name you are referring to.
In this case you could use classDocument for the name of the document or
classLayer for the name of the layer.
It can be used for low-level access into Contains data associated
with an ActionDescriptor.

"""

# Import built-in modules
from abc import ABC
from abc import abstractmethod

# Import third-party modules
import comtypes

# Import local modules
from photoshop.api._core import Photoshop


class ActionReference(Photoshop, ABC):
    object_name = "ActionReference"

    def __init__(self, parent: comtypes.client.lazybind.Dispatch = None):
        super().__init__(parent=parent)

    @abstractmethod
    def getContainer(self):
        """Implemented in _actionmanager_type_binder.ActionReference"""
        pass

    def getDesiredClass(self) -> int:
        """Gets a number representing the class of the object."""
        return self.app.getDesiredClass()

    def getEnumeratedType(self) -> int:
        """Gets the enumeration type."""
        return self.app.getEnumeratedType()

    def getEnumeratedValue(self) -> int:
        """Gets the enumeration value."""
        return self.app.getEnumeratedValue()

    @abstractmethod
    def getForm(self):
        """Implemented in _actionmanager_type_binder.ActionReference"""
        pass

    def getIdentifier(self) -> int:
        """Gets the identifier value for a reference whose form is identifier."""
        return self.app.getIdentifier()

    def getIndex(self) -> int:
        """Gets the index value for a reference in a list or array."""
        return self.app.getIndex()

    def getName(self) -> str:
        """Gets the name of a reference."""
        return self.app.getName()

    def getOffset(self) -> int:
        """Gets the offset of the object’s index value."""
        return self.app.getOffset()

    def getProperty(self) -> int:
        return self.app.getProperty()

    def putClass(self, desiredClass: int):
        self.app.putClass(desiredClass)

    def putEnumerated(self, desiredClass: int, enumType: int, value: int):
        self.app.putEnumerated(desiredClass, enumType, value)

    def putIdentifier(self, desiredClass: int, value: int):
        self.app.putIdentifier(desiredClass, value)

    def putIndex(self, desiredClass: int, value: int):
        self.app.putIndex(desiredClass, value)

    def putName(self, desiredClass: int, value: str):
        self.app.putName(desiredClass, value)

    def putOffset(self, desiredClass: int, value: int):
        self.app.putOffset(desiredClass, value)

    def putProperty(self, desiredClass: int, value: int):
        self.app.putProperty(desiredClass, value)
