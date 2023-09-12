"""Maybe the core of this submodule.
Handles almost all type mappings. (Some else are in ReferenceKey.)
This module is INTERNAL. You should not import functions from it."""

# Import built-in modules
import pathlib

from ..desc_value_types import Enumerated
from ..desc_value_types import TypeID
from ..desc_value_types import UnitDouble
from ..utils import id2str


__all__ = ["unpack", "pack", "parsetype"]

pytype2str = {
    bool: "Boolean",
    int: "Integer",
    float: "Double",
    str: "String",
    pathlib.WindowsPath: "Path",
    Enumerated: "Enumerated",
    UnitDouble: "UnitDouble",
    TypeID: "Class",
    "ActionDescriptor": "Object",
    "ActionList": "List",
    "ActionReference": "Reference",
}

str2pytype = {
    "Enumerated": Enumerated,
    "UnitDouble": UnitDouble,
    "Class": TypeID,
}


def unpack(val):
    vtype = val.typename if hasattr(val, "typename") else type(val)
    typestr = pytype2str[vtype]
    try:
        args = val._unpacker()
    except BaseException:
        args = (val,)
    return (typestr, args)


def pack(obj, index):  # "index" means id of key string or list index.
    valtype = obj.getType(index)
    typestr = str(valtype)[14:-4]
    typestr = "Path" if typestr == "Alias" else typestr
    if typestr == "Data":
        # No plan to support RawType because it seldom runs successfully
        # and is seldom used in regular scripting.
        return None
    if typestr in str2pytype:
        pytype = str2pytype[typestr]
        val = pytype._packer(obj, index)
    elif typestr == "Object":
        val = obj.getObjectValue(index)
        val.classID = id2str(obj.getObjectType(index))
    else:
        get_func = getattr(obj, "get" + typestr)
        val = get_func(index)
    return val


def parsetype(obj):
    if type(obj) == dict:
        dtype = "ActionDescriptor"
    elif type(obj) == list:
        first = obj[0] if obj else None
        if first == "!ref":
            dtype = "ActionReference"
        else:
            dtype = "ActionList"
    else:
        dtype = "others"
    return dtype
