from ..utils import *
from collections import namedtuple

TypeID_proto = namedtuple('TypeID_proto', ['string'])

class TypeID(TypeID_proto):
  '''You can initialize a TypeID object with 1 argument: string.'''
  @classmethod
  def _packer(cls, obj, index):
    typeid = id2str(obj.getClass(index))
    return cls(typeid)
  def _unpacker(self):
    nid = str2id(self.typeid)
    return (nid,)