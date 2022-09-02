from .action_reference_iterator import ActionReference_Iterator
from ..ref_form_types import ReferenceKey
from abc import ABC, abstractclassmethod

class ActionReference(ABC):
  '''A vessel for my extra utils.'''

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
    target = self
    for i in range(index+1):
      try:
        target = target.getContainer()
      except:
        raise IndexError('index out of range')
    return ReferenceKey._packer(target)

  def uput(self, rkey: ReferenceKey):
    assert type(rkey) == ReferenceKey
    ftype, dcls, v = rkey._unpacker()
    put_func = getattr(self, 'put'+ftype)
    args = (dcls,) if v is None else (dcls, *v)
    put_func(*args)

  def dump(self) -> list:
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