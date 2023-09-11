"""This object provides information about what the action is refering to.

For example, when referring to the name of something you might use keyName.
The reference would also need to know what name you are referring to.
In this case you could use classDocument for the name of the document or
classLayer for the name of the layer.
It can be used for low-level access into Contains data associated
with an ActionDescriptor.

"""
# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import ReferenceFormType


class ActionReference(Photoshop):
    """Contains data describing a referenced Action.

    The action reference object is part of the Action Manager functionality.
    For details on using the Action Manager, see the Photoshop Scripting Guide.

    """

    object_name = "ActionReference"

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._flag_as_method(
            "getContainer",
            "getDesiredClass",
            "getEnumeratedType",
            "getEnumeratedValue",
            "getForm",
            "getIdentifier",
            "getIndex",
            "putName",
            "putClass",
            "putEnumerated",
            "putIdentifier",
            "putIndex",
            "putOffset",
            "putProperty",
        )

    def getContainer(self):
        return self.app.getContainer()

    def getDesiredClass(self):
        return self.app.getDesiredClass()

    def getEnumeratedType(self) -> int:
        return self.app.getEnumeratedType()

    def getEnumeratedValue(self) -> int:
        return self.app.getEnumeratedValue()

    def getForm(self) -> ReferenceFormType:
        """Gets the form of this action reference."""
        return ReferenceFormType(self.app.getForm())

    def getIdentifier(self) -> int:
        """Gets the identifier value for a reference whose form is
        identifier."""
        return self.app.getIdentifier()

    def getIndex(self) -> int:
        """Gets the index value for a reference in a list or array,"""
        return self.app.getIndex()

    def putName(self, key, value):
        return self.app.putName(key, value)

    def putClass(self, value):
        return self.app.putClass(value)

    def putEnumerated(self, desired_class, enum_type, value):
        """Puts an enumeration type and ID into a reference along with the
        desired class for the reference."""
        return self.app.putEnumerated(desired_class, enum_type, value)

    def putIdentifier(self, desired_class, value):
        return self.app.putIdentifier(desired_class, value)

    def putIndex(self, desired_class, value):
        return self.app.putIndex(desired_class, value)

    def putOffset(self, desired_class, value):
        return self.app.putOffset(desired_class, value)

    def putProperty(self, desired_class, value):
        return self.app.putProperty(desired_class, value)
