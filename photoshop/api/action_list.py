"""This object provides an array-style mechanism for storing data.

It can be used for low-level access info Photoshop.


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


class ActionList(Photoshop, ABC):
    """This object provides an array-style mechanism for storing data. It can be used for low-level access into Photoshop.
    This object is ideal when storing data of the same type. All items in the list must be of the same type."""

    object_name = "ActionList"

    def __init__(self, parent: comtypes.client.lazybind.Dispatch = None):
        super().__init__(parent=parent)

    @property
    def count(self):
        return self.app.count

    def clear(self):
        """Clears the list."""
        self.app.clear()

    def getBoolean(self, index: int) -> bool:
        """Gets the value of a list element of type boolean."""
        return self.app.getBoolean(index)

    def getClass(self, index: int) -> int:
        """Gets the value of a list element of type class."""
        return self.app.getClass(index)

    def getData(self, index: int) -> bytes:
        """Gets raw byte data as a string value."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            return self.app.getData(index)
        except BaseException:
            return None

    def getDouble(self, index: int) -> float:
        """Gets the value of a list element of type double."""
        return self.app.getDouble(index)

    def getEnumerationType(self, index: int) -> int:
        """Gets the enumeration type of a list element."""
        return self.app.getEnumerationType(index)

    def getEnumerationValue(self, index: int) -> int:
        """Gets the enumeration value of a list element."""
        return self.app.getEnumerationValue(index)

    def getInteger(self, index: int) -> int:
        """Gets the value of a list element of type integer."""
        return self.app.getInteger(index)

    def getLargeInteger(self, index: int) -> int:
        """Gets the value of a list element of type large integer."""
        return self.app.getLargeInteger(index)

    @abstractmethod
    def getList(self, index):
        """Implemented in _actionmanager_type_binder.ActionList"""
        pass

    def getObjectType(self, index: int) -> int:
        """Gets the class ID of a list element of type object."""
        return self.app.getObjectType(index)

    @abstractmethod
    def getObjectValue(self, index):
        """Implemented in _actionmanager_type_binder.ActionList"""
        pass

    def getPath(self, index: int) -> pathlib.Path:
        """Gets the value of a list element of type File."""
        return pathlib.Path(self.app.getPath(index))

    @abstractmethod
    def getReference(self, index):
        """Implemented in _actionmanager_type_binder.ActionList"""
        pass

    def getString(self, index: int) -> str:
        """Gets the value of a list element of type string."""
        return self.app.getString(index)

    @abstractmethod
    def getType(self, index):
        """Implemented in _actionmanager_type_binder.ActionList"""
        pass

    def getUnitDoubleType(self, index: int) -> int:
        """Gets the unit value type of a list element of type Double."""
        return self.app.getUnitDoubleType(index)

    def getUnitDoubleValue(self, index: int) -> float:
        """Gets the unit value of a list element of type double."""
        return self.app.getUnitDoubleValue(index)

    def putBoolean(self, value: bool):
        """Appends a new value, true or false."""
        self.app.putBoolean(value)

    def putClass(self, value: int):
        """Appends a new value, a class or data type."""
        self.app.putClass(value)

    def putData(self, value: bytes):
        """Appends a new value, a string containing raw byte data."""
        warnings.warn(DATAFUNC_WARN, category=PendingDeprecationWarning)
        try:
            self.app.putData(value)
        except BaseException:
            pass

    def putDouble(self, value: float):
        """Appends a new value, a double."""
        self.app.putDouble(value)

    def putEnumerated(self, enumType: int, value: int):
        """Appends a new value, an enumerated (constant) value."""
        self.app.putEnumerated(enumType, value)

    def putInteger(self, value: int):
        """Appends a new value, an integer."""
        if value.bit_length() <= 32:
            self.app.putInteger(value)
        else:
            self.app.putLargeInteger(value)

    def putLargeInteger(self, value: int):
        """Appends a new value, a large integer."""
        self.app.putLargeInteger(value)

    def putList(self, value):
        """Appends a new value, a nested action list."""
        assert value.typename == "ActionList"
        self.app.putList(value)

    def putObject(self, classID: int, value):
        """Appends a new value, an object."""
        assert value.typename == "ActionDescriptor"
        self.app.putObject(classID, value)

    def putPath(self, value: pathlib.Path):
        """Appends a new value, a path."""
        self.app.putPath(str(value))

    def putReference(self, value):
        """Appends a new value, a reference to an object created in the script."""
        assert value.typename == "ActionReference"
        self.app.putReference(value)

    def putString(self, value: str):
        """Appends a new value, a string."""
        self.app.putString(value)

    def putUnitDouble(self, classID: int, value: float):
        """Appends a new value, a unit/value pair"""
        self.app.putUnitDouble(classID, value)
