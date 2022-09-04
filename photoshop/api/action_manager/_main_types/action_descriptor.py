# Import built-in modules
from abc import ABC
from abc import abstractclassmethod
from typing import Any

from ..utils import id2str
from ..utils import str2id
from ._type_mapper import pack
from ._type_mapper import parsetype
from ._type_mapper import unpack
from .action_descriptor_iterator import ActionDescriptor_Iterator


class ActionDescriptor(ABC):
    """A vessel for my extra utils.
    You should not use, and cannot initialize it
    because it is an abstract class."""

    @abstractclassmethod
    def load(cls, adict: dict, namespace: dict):  # pass globals() for namespace
        clsid = adict["_classID"] if "_classID" in adict else None
        new = cls(classID=clsid)
        for k, v in adict.items():
            if k == "_classID":
                continue
            # py37 compat
            try:
                val = eval(r'v if (dtype := parsetype(v)) == "others" else namespace[dtype].load(v)')  # noqa
            except SyntaxError:
                val = v if parsetype(v) == "others" else namespace[parsetype(v)].load(v)
            new.uput(k, val)
        return new

    def uget(self, key: str) -> Any:
        """Get a value of a key in an ActionDescriptor, no matter its type."""
        keyid = str2id(key)
        val = pack(self, keyid)
        return val

    def uput(self, key: str, val: Any):
        """Put a value of a key into an ActionDescriptor, no matter its type."""
        keyid = str2id(key)
        typestr, args = unpack(val)
        put_func = getattr(self, "put" + typestr)
        put_func(keyid, *args)

    def __len__(self):
        return self.count

    def __iter__(self) -> ActionDescriptor_Iterator:
        return ActionDescriptor_Iterator(self)

    def items(self) -> ((str, Any)):
        keyids = (self.getKey(n) for n in range(len(self)))
        return ((id2str(keyid), pack(self, keyid)) for keyid in keyids)

    def __contains__(self, key):
        keys = [key for key in self]
        return key in keys

    def dump(self) -> dict:
        """Convert an ActionDescriptor to a python object."""
        # This is a dict comprehension.
        ddict = {"_classID": self.classID}
        ext = {k: (v.dump() if hasattr(v, "dump") else v) for k, v in self.items()}
        ddict.update(ext)
        return ddict

    def _unpacker(self) -> tuple:
        value = self
        if self.classID is None:
            raise RuntimeError("Do not use old methods and new methods mixedly.")
        clsid = str2id(self.classID)
        return (clsid, value)
