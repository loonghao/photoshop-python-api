"""A record of key-data pairs for actions.

such as those included on the Adobe Photoshop Actions menu.
The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""

# Import built-in modules
from abc import ABC
from abc import abstractmethod
import pathlib
import warnings

# Import third-party modules
import comtypes

# Import local modules
from photoshop.api._core import Photoshop


DATAFUNC_WARN = """fromSteam, toStream, getData, putData is seldom performed successfully (even in native js, for
example https://github.com/drsong2000/CRYENGINE/blob/release/Tools/photoshop/UltimateTextureSaver/Install/xtools/xlib/
xml/atn2bin.jsx#L753-L769), and is deprecated. In fact, searching in github shows that these 4 functions are barely
used in regular photoshop scripting. If you have found the criteria of these functions, please open an issue."""


class ActionDescriptor(Photoshop, ABC):
    """This object provides a dictionary-style mechanism for storing data as key-value pairs. It can be used for
    low-level access into Photoshop."""

    object_name = "ActionDescriptor"

    def __init__(self, parent: comtypes.client.lazybind.Dispatch = None):
        super().__init__(parent=parent)

    @property
    def count(self):
        """The number of keys contained in the descriptor."""
        return self.app.count

    def clear(self):
        """Clears the descriptor."""
        self.app.clear()

    def isEqual(self, otherDesc):
        """Determines whether the descriptor is the same as another descriptor."""
        assert otherDesc.typename == "ActionDescriptor"
        return self.app.isEqual(otherDesc)

    def __eq__(self, other):
        try:
            return self.isEqual(other)
        except AssertionError:
            return False

    def erase(self, key: int):
        """Erases a key from the descriptor."""
        self.erase(key)

    def fromStream(self, value: str):
        """Creates a descriptor from a stream of bytes; for reading from disk."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            self.app.fromStream(bytes.decode(value))
        except BaseException:
            pass

    def toStream(self) -> str:
        """Gets the entire descriptor as a stream of bytes, for writing to disk."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            return self.app.toStream()
        except BaseException:
            return None

    def getKey(self, index: int) -> int:
        """Gets the ID of the Nth key, provided by index."""
        return self.app.getKey(index)

    def getBoolean(self, key: int) -> bool:
        """Gets the value of a key of type boolean."""
        return self.app.getBoolean(key)

    def getClass(self, key: int) -> int:
        """Gets the value of a key of type class."""
        return self.app.getClass(key)

    def getData(self, key: int) -> str:
        """Gets raw byte data as a string value."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            return self.app.getData(key)
        except BaseException:
            return None

    def getDouble(self, key: int) -> float:
        """Gets the value of a key of type double."""
        return self.app.getDouble(key)

    def getEnumerationType(self, key: int) -> int:
        """Gets the enumeration type of a key."""
        return self.app.getEnumerationType(key)

    def getEnumerationValue(self, key: int) -> int:
        """Gets the enumeration value of a key."""
        return self.app.getEnumerationValue(key)

    def getInteger(self, key: int) -> int:
        """Gets the value of a key of type integer."""
        return self.app.getInteger(key)

    def getLargeInteger(self, key: int) -> int:
        """Gets the value of a key of type large integer."""
        return self.app.getLargeInteger(key)

    @abstractmethod
    def getList(self, key):
        """Implemented in _actionmanager_type_binder.ActionDescriptor"""
        pass

    def getObjectType(self, key: int) -> int:
        """Gets the class ID of an object in a key of type object."""
        return self.app.getObjectType(key)

    @abstractmethod
    def getObjectValue(self, key):
        """Implemented in _actionmanager_type_binder.ActionDescriptor"""
        pass

    def getPath(self, key: int) -> pathlib.WindowsPath:
        """Gets the value of a key of type File."""
        return pathlib.Path(self.app.getPath(key))

    @abstractmethod
    def getReference(self, key):
        """Implemented in _actionmanager_type_binder.ActionDescriptor"""
        pass

    def getString(self, key: int) -> str:
        """Gets the value of a key of type string."""
        return self.app.getString(key)

    @abstractmethod
    def getType(self, key):
        """Implemented in _actionmanager_type_binder.ActionDescriptor"""
        pass

    def getUnitDoubleType(self, key: int) -> int:
        """Gets the unit type of a key of type UnitDouble."""
        return self.app.getUnitDoubleType(key)

    def getUnitDoubleValue(self, key: int) -> int:
        """Gets the unit type of a key of type UnitDouble."""
        return self.app.getUnitDoubleValue(key)

    def putBoolean(self, key: int, value: bool):
        """Sets the value for a key whose type is boolean."""
        self.app.putBoolean(key, value)

    def putClass(self, key: int, value: int):
        """Sets the value for a key whose type is class."""
        self.app.putClass(key, value)

    def putData(self, key: int, value: str):
        """Puts raw byte data as a string value."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            self.app.putData(key, value)
        except BaseException:
            pass

    def putDouble(self, key: int, value: int):
        """Sets the value for a key whose type is double."""
        self.app.putDouble(key, value)

    def putEnumerated(self, key: int, enumType: int, value: int):
        """Sets the enumeration type and value for a key."""
        self.app.putEnumerated(key, enumType, value)

    def putInteger(self, key: int, value: int):
        """Sets the value for a key whose type is integer."""
        if value.bit_length() <= 32:
            self.app.putInteger(key, value)
        else:
            self.app.putLargeInteger(key, value)

    def putLargeInteger(self, key: int, value: int):
        """Sets the value for a key whose type is large integer."""
        self.app.putLargeInteger(key, value)

    def putList(self, key: int, value):
        """Sets the value for a key whose type is an ActionList object."""
        assert value.typename == "ActionList"
        self.app.putList(key, value)

    def putObject(self, key: int, classID: int, value):
        """Sets the value for a key whose type is an object, represented by an Action Descriptor."""
        assert value.typename == "ActionDescriptor"
        self.app.putObject(key, classID, value)

    def putPath(self, key: int, value: pathlib.WindowsPath):
        """Sets the value for a key whose type is path."""
        self.app.putPath(key, str(value))

    def putReference(self, key: int, value):
        """Sets the value for a key whose type is an object reference."""
        assert value.typename == "ActionReference"
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
