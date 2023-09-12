"""Defines class ReferenceKey. It handles type mapping in ActionReference.
You can initialize it with 2 arguments: desiredclass, value."""

# Import built-in modules
from collections import namedtuple

# Import local modules
from photoshop.api.enumerations import ReferenceFormType

from ..desc_value_types import Enumerated
from ..desc_value_types import TypeID
from ..utils import id2str
from ..utils import str2id
from ._marker import marker

# Identifier, Index, Offset are used by getting them in globals().
from .identifier import Identifier  # noqa: F401
from .index import Index  # noqa: F401
from .offset import Offset  # noqa: F401


psreftype2str = {
    **{vtype.value: str(vtype)[27:-4] for vtype in ReferenceFormType},
    **{vtype: str(vtype)[27:-4] for vtype in ReferenceFormType},
}

ReferenceKey_proto = namedtuple("ReferenceKey", ["desiredclass", "value"])


class ReferenceKey(ReferenceKey_proto):
    @classmethod
    def _packer(cls, obj):
        ftype = psreftype2str[obj.getForm()]
        dcls = id2str(obj.getDesiredClass())
        try:
            get_func = getattr(obj, "get" + ftype)
        except BaseException:
            get_func = None
        if ftype == "Class":
            v = None
        elif ftype == "Enumerated":
            v = Enumerated(
                id2str(obj.getEnumeratedType()),
                id2str(obj.getEnumeratedValue()),
            )  # noqa
        elif ftype == "Property":
            v = TypeID(id2str(obj.getProperty()))
        elif ftype == "Name":
            v = get_func()
        elif ftype in ("Identifier", "Index", "Offset"):
            v = globals()[ftype] + get_func()
        return cls(dcls, v)

    def _unpacker(self):
        dcls = str2id(self.desiredclass)
        value = self.value
        if value is None:
            v = value
            ftype = "Class"
        elif type(value) == TypeID:
            v = value._unpacker()
            ftype = "Property"
        elif type(value) == marker:
            v = (value.value,)
            ftype = value.name
        elif type(value) == Enumerated:
            v = value._unpacker()
            ftype = "Enumerated"
        elif type(value) == str:
            v = (value,)
            ftype = "Name"
        return (ftype, dcls, v)
