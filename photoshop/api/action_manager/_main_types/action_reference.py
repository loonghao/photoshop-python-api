from .action_reference_iterator import ActionReference_Iterator
from ..ref_form_types import ReferenceKey
from abc import ABC, abstractclassmethod

class ActionReference(ABC):
  '''A vessel for my extra utils.
  You should not use, and cannot initialize it
  because it is an abstract class.'''

  @abstractclassmethod
  def load(cls, alist: list):
    new = cls()
    # pack into a list if is a single key
    alist = [alist] \
      if type(alist) == ReferenceKey \
      else alist
    for rkey in alist:
      if rkey == '!ref':
        continue
      new.uput(rkey)
    return new

  def uget(self, index: int) -> ReferenceKey:
    '''Get a key in an ActionReference as ReferenceKey, no matter its type.'''
    target = self
    for i in range(index+1):
      try:
        target = target.getContainer()
      except:
        raise IndexError('index out of range')
    return ReferenceKey._packer(target)

  def uput(self, rkey: ReferenceKey):
    '''Put a ReferenceKey into an ActionReference, no matter its type.'''
    assert type(rkey) == ReferenceKey
    ftype, dcls, v = rkey._unpacker()
    put_func = getattr(self, 'put'+ftype)
    args = (dcls,) if v is None else (dcls, *v)
    put_func(*args)

  def dump(self) -> list:
    '''Convert an ActionReference to a python object.'''
    target = self
    tlist = ['!ref']
    tlist.extend([elem for elem in self])
    return tlist

  def __len__(self):
    rlen = 1; target = self
    while True:
      try:
        target = target.getContainer(); rlen += 1
      except:
        rlen -= 1; break
    return rlen

  def __iter__(self) -> ActionReference_Iterator:
    return ActionReference_Iterator(self)