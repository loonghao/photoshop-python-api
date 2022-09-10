"""TypeID conversion utilities of this submodule."""

# Import built-in modules
import warnings
from functools import wraps

# Import local modules
from photoshop.api._core import Photoshop


__all__ = ["str2id", "id2str"]


class AppAgent(Photoshop):
    """Partially reimplement the Application class
    in this file to avoid circular import."""

    typename = "Application"

    def str2id(self, string: str) -> int:
        return self.app.stringIDToTypeID(string)

    def id2str(self, number: int) -> str:
        return self.app.typeIDToStringID(number)


converter = None


def requireapp(func):
    """A simple decorator that initializes the global
    app instance when the decorated function is called."""

    @wraps(func)
    def wrapped(*args, **kwargs):
        global converter
        if converter is None:
            converter = AppAgent()
        return func(*args, **kwargs)

    return wrapped


def str2hash(x: str) -> int:
    """Convert charID to typeID."""
    assert len(x) == 4
    x = x.replace(" ", "\x20")
    return int.from_bytes(bytes(x, encoding="utf-8"), byteorder="big")


def hash2str(x: int) -> str:
    """Convert typeID to charID."""
    assert len(hex(x)) == 10
    return x.to_bytes(length=4, byteorder="big").decode()


# Current approach of str2id is not perfect, it will face some "collisions".
# This means, if there exists a charID which is the same as another stringID,
# it will cause a "collision".
# For example charID 'From' -> stringID 'from'
#         and charID 'from' -> stringID 'originalAddressAttr'
# We can know when this will happen by prescanning the cpp header
# "PITerminology.h" and "PIStringTerminology.h".
# Prescanned collisions are stored here. If you suffer from collisions that
# str2id cannot handle, please open an issue.

collisions = {
    "chr": ("Cpy ", "From", "Type"),
    "str": ("copyEvent", "originalAddressAttr", "class"),
    "collision": ("copy", "from", "type"),
}

COLLISION_WARNING = """
You are using a string that is a collision of stringID and charID.
On this situation, str2id will consider this string as stringID. If you encounter COMerror
on app.executeAction() later, you can try to replace this string(%s) with its corresponding
charID(%s). If you are sure you want to use it as stringID and suppress this warning,
replace this string(%s) with its corresponding stringID(%s).
If this warning doesn't solve you problem, please open an issue."""


@requireapp
def str2id(psstr: str) -> str:
    """Convert charID or stringID to typeID"""
    assert type(psstr) == str
    if len(psstr) == 4:
        try:
            search = collisions["collision"].index(psstr)
            warnstr = COLLISION_WARNING % (
                repr(collisions["collision"][search]),
                repr(collisions["chr"][search]),
                repr(collisions["collision"][search]),
                repr(collisions["str"][search]),
            )
            warnings.warn(warnstr, category=RuntimeWarning)
        except ValueError:
            pass  # I know what I am doing.
        typeid = str2hash(psstr)
        try:
            restr = converter.id2str(typeid)
        except BaseException:
            restr = ""
        if not restr:
            typeid = converter.str2id(psstr)
    else:
        typeid = converter.str2id(psstr)
    return typeid


@requireapp
def id2str(typeid: int) -> str:
    """Convert typeID to stringID"""
    result = converter.id2str(typeid)
    try:
        search = collisions["collision"].index(result)
        return collisions["chr"][search]
    except ValueError:
        return result
