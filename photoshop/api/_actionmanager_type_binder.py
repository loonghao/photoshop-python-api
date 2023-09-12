"""This file enables type communication without circular import.

We just put type-irrelevant codes in one file then inherit it in this file and add type-relevant codes.

"""


# Import local modules
from photoshop.api.action_descriptor import ActionDescriptor as AD_proto
from photoshop.api.action_list import ActionList as AL_proto
from photoshop.api.action_manager._main_types.action_descriptor import (
    ActionDescriptor as AD_utils_proto,
)
from photoshop.api.action_manager._main_types.action_list import (
    ActionList as AL_utils_proto,
)
from photoshop.api.action_manager._main_types.action_reference import (
    ActionReference as AR_utils_proto,
)
from photoshop.api.action_reference import ActionReference as AR_proto
from photoshop.api.enumerations import DescValueType
from photoshop.api.enumerations import ReferenceFormType


class ActionDescriptor(AD_proto, AD_utils_proto):
    @classmethod
    def load(cls, adict: dict) -> "ActionDescriptor":
        """Convert a python object to an ActionDescriptor"""
        return super().load(adict, globals())

    def __init__(self, parent=None, classID=None):
        self.classID = classID
        super().__init__(parent=parent)

    def getType(self, key: int) -> DescValueType:
        """Gets the type of a key."""
        return DescValueType(self.app.getType(key))

    def getObjectValue(self, key: int) -> "ActionDescriptor":
        """Gets the value of a key of type object."""
        return ActionDescriptor(parent=self.app.getObjectValue(key))

    def getList(self, key: int) -> "ActionList":
        """Gets the value of a key of type list."""
        return ActionList(parent=self.app.getList(key))

    def getReference(self, key: int) -> "ActionReference":
        """Gets the value of a key of type ActionReference."""
        return ActionReference(parent=self.app.getReference(key))


class ActionList(AL_proto, AL_utils_proto):
    @classmethod
    def load(cls, alist: list) -> "ActionList":
        """Convert a python object to an ActionList"""
        return super().load(alist, globals())

    def getType(self, index: int) -> DescValueType:
        """Gets the type of a list element."""
        return DescValueType(self.app.getType(index))

    def getObjectValue(self, index: int) -> "ActionDescriptor":
        """Gets the value of a list element of type object."""
        return ActionDescriptor(parent=self.app.getObjectValue(index))

    def getList(self, index: int) -> "ActionList":
        """Gets the value of a list element of type list."""
        return ActionList(parent=self.app.getList(index))

    def getReference(self, index: int) -> "ActionReference":
        """Gets the value of a list element of type ActionReference."""
        return ActionReference(parent=self.app.getReference(index))


class ActionReference(AR_proto, AR_utils_proto):
    @classmethod
    def load(cls, adict: dict) -> "ActionReference":
        """Convert a python object to an ActionReference"""
        return super().load(adict)

    def getForm(self) -> ReferenceFormType:
        """Gets the form of this action reference."""
        return ReferenceFormType(self.app.getForm())

    def getContainer(self) -> "ActionReference":
        """Gets a reference contained in this reference.
        Container references provide additional pieces to the reference.
        This looks like another reference, but it is actually part of the same reference."""
        return ActionReference(parent=self.app.getContainer())
