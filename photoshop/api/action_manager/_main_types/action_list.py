# Import built-in modules
from abc import ABC
from abc import abstractclassmethod
from typing import Any

from ._type_mapper import pack
from ._type_mapper import parsetype
from ._type_mapper import unpack
from .action_list_iterator import ActionList_Iterator


class ActionList(ABC):
    """A vessel for my extra utils.
    You should not use, and cannot initialize it
    because it is an abstract class."""

    @abstractclassmethod
    def load(cls, alist: list, namespace: dict):  # pass globals() for namespace
        new = cls()
        for v in alist:
            # py37 compat
            try:
                val = eval(r'v if (dtype := parsetype(v)) == "others" else namespace[dtype].load(v)')  # noqa
            except SyntaxError:
                val = v if parsetype(v) == "others" else namespace[parsetype(v)].load(v)
            new.uput(val)
        return new

    @property
    def dtype(self) -> str:
        if len(self) == 0:
            return None
        valtype = self.getType(0)
        typestr = str(valtype)[14:-4]
        return typestr

    def uget(self, index: int) -> Any:
        """Get an element in an ActionList, no matter its type."""
        val = pack(self, index)
        return val

    def uput(self, val: Any):
        """Put an element into an ActionList, no matter its type."""
        typestr, args = unpack(val)
        # ActionList type checking
        # py37 compat
        try:
            assert eval(
                r"True if (dtype := self.dtype) is None else dtype == typestr"
            ), "ActionList can only hold things of the same type"
        except SyntaxError:
            assert (
                True if self.dtype is None else self.dtype == typestr
            ), "ActionList can only hold things of the same type"
        put_func = getattr(self, "put" + typestr)
        put_func(*args)

    def __len__(self):
        return self.count

    def __iter__(self) -> ActionList_Iterator:
        return ActionList_Iterator(self)

    def dump(self) -> list:
        """Convert an ActionList to a python object."""
        # This is a list comprehension.
        dlist = [(elem.dump() if hasattr(elem, "dump") else elem) for elem in self]
        return dlist
