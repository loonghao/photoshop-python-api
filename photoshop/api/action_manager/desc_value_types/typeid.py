from ..utils import *
from collections import namedtuple

TypeID_proto = namedtuple('TypeID_proto', ['string'])

class TypeID(TypeID_proto):
  @classmethod
  def _packer(cls, obj, index):
    typeid = id2str(obj.getClass(index))
    return cls(typeid)
  def _unpacker(self):
    nid = str2id(self.typeid)
    return (nid,)