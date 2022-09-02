from ._type_mapper import *
from ..utils import *
from .action_list_iterator import ActionList_Iterator
from typing import Any
from abc import ABC, abstractclassmethod

class ActionList(ABC):
  '''A vessel for my extra utils.'''

  @abstractclassmethod
  def load(cls, alist: list, namespace: dict):  # pass globals() for namespace
    new = cls()
    for v in alist:
      v = v \
        if (dtype := parsetype(v)) == 'others' \
        else namespace[dtype].load(v)
      new.uput(v)
    return new

  @property
  def dtype(self) -> str:
    if len(self) == 0:
      return None
    valtype = self.getType(0)
    typestr = str(valtype)[14:-4]
    return typestr

  def uget(self, index: int) -> Any:
    val = pack(self, index)
    return val

  def uput(self, val: Any):
    typestr, args = unpack(val)
    #ActionList type checking
    assert True if (dtype := self.dtype) is None else dtype == typestr, \
      'ActionList can only hold things of the same type'
    put_func = getattr(self, 'put'+typestr)
    put_func(*args)

  def __len__(self):
    return self.count

  def __iter__(self) -> ActionList_Iterator:
    return ActionList_Iterator(self)

  def dump(self) -> list:
    #This is a list comprehension.
    dlist = [
      (
        elem.dump() \
          if hasattr(elem, 'dump') \
          else elem
      ) for elem in self
    ]
    return dlist