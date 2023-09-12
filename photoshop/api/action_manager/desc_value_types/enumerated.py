# Import built-in modules
from collections import namedtuple

from ..utils import id2str
from ..utils import str2id


Enumerated_proto = namedtuple("Enumerated_proto", ["type", "value"])


class Enumerated(Enumerated_proto):
    """You can initialize an Enumerated object with 2 arguments: type, value."""

    @classmethod
    def _packer(cls, obj, index):
        type = id2str(obj.getEnumerationType(index))
        value = id2str(obj.getEnumerationValue(index))
        return cls(type, value)

    def _unpacker(self):
        typeid = str2id(self.type)
        valueid = str2id(self.value)
        return (typeid, valueid)
