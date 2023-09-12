# Import built-in modules
from collections import namedtuple

from ..utils import id2str
from ..utils import str2id


TypeID_proto = namedtuple("TypeID_proto", ["string"])


class TypeID(TypeID_proto):
    """You can initialize a TypeID object with 1 argument: string."""

    @classmethod
    def _packer(cls, obj, index):
        typeid = id2str(obj.getClass(index))
        return cls(typeid)

    def _unpacker(self):
        nid = str2id(self.typeid)
        return (nid,)
