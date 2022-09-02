from ._type_mapper import *
from ..utils import *
from .action_descriptor_iterator import ActionDescriptor_Iterator
from typing import Any
from abc import ABC, abstractclassmethod

class ActionDescriptor:
  '''A vessel for my extra utils.'''

  @abstractclassmethod
  def load(cls, adict: dict, namespace: dict):  # pass globals() for namespace
    clsid = adict['_classID'] \
      if '_classID' in adict \
      else None
    new = cls(classID=clsid)
    for k,v in adict.items():
      if k == '_classID':
        continue
      v = v \
        if (dtype := parsetype(v)) == 'others' \
        else namespace[dtype].load(v)
      new.uput(k,v)
    return new

  def uget(self, key: str) -> Any:
    keyid = str2id(key)
    val = pack(self, keyid)
    return val

  def uput(self, key: str, val: Any):
    keyid = str2id(key)
    typestr, args = unpack(val)
    put_func = getattr(self, 'put'+typestr)
    put_func(keyid, *args)

  def __len__(self):
    return self.count

  def __iter__(self) -> ActionDescriptor_Iterator:
    return ActionDescriptor_Iterator(self)

  def __contains__(self, key):
    keys = [key for key in self]
    return key in keys

  def dump(self) -> dict:
    #This is a dict comprehension.
    ddict = {'_classID':self.classID}
    ddict.update({
      key:(
        value.dump() \
          if hasattr(value := self.uget(key), 'dump') \
          else value
      ) for key in self
    })
    return ddict

  def _unpacker(self) -> tuple:
    value = self
    if self.classID is None:
      raise RuntimeError('Do not use old methods and new methods mixedly.')
    clsid = str2id(self.classID)
    return (clsid, value)