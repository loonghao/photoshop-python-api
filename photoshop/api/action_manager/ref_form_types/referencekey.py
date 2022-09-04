'''Defines class ReferenceKey. It handles type mapping in ActionReference.
You can initialize it with 2 arguments: desiredclass, value.'''

from ..utils import *
from ..desc_value_types import TypeID, Enumerated
from photoshop.api.enumerations import ReferenceFormType
from .identifier import Identifier
from .index import Index
from .offset import Offset
from ._marker import marker
from collections import namedtuple

psreftype2str = {
    **{vtype.value:str(vtype)[27:-4] for vtype in ReferenceFormType},
    **{vtype:str(vtype)[27:-4] for vtype in ReferenceFormType},
}

ReferenceKey_proto = namedtuple('ReferenceKey', ['desiredclass', 'value'])

class ReferenceKey(ReferenceKey_proto):
  @classmethod
  def _packer(cls, obj):
    ftype = psreftype2str[obj.getForm()]
    dcls = id2str(obj.getDesiredClass())
    try:
      get_func = getattr(obj, 'get'+ftype)
    except:
      get_func = None
    if ftype == 'Class':
      v = None
    elif ftype == 'Enumerated':
      v = Enumerated(id2str(obj.getEnumeratedType()), id2str(obj.getEnumeratedValue()))
    elif ftype == 'Property':
      v = TypeID(id2str(obj.getProperty()))
    elif ftype == 'Name':
      v = get_func()
    elif ftype in ('Identifier', 'Index', 'Offset'):
      v = globals()[ftype]+get_func()
    return cls(dcls, v)
  def _unpacker(self):
    dcls = str2id(self.desiredclass)
    value = self.value
    if value is None:
      v = value
      ftype = 'Class'
    elif type(value) == TypeID:
      v = value._unpacker()
      ftype = 'Property'
    elif type(value) == marker:
      v = (value.value,)
      ftype = value.name
    elif type(value) == Enumerated:
      v = value._unpacker()
      ftype = 'Enumerated'
    elif type(value) == str:
      v = (value,)
      ftype = 'Name'
    return (ftype, dcls, v)