from photoshop.api._core import Photoshop

__all__ = ['str2id', 'id2str']

class app(Photoshop):
  typename = 'Application'
  def str2id(self, string: str) -> int:
    return self.app.stringIDToTypeID(string)
  def id2str(self, number: int) -> str:
    return self.app.typeIDToStringID(number)

converter = app()

def str2hash(x: str) -> int:
  '''Convert charID to typeID.'''
  assert len(x) == 4
  x = x.replace(' ', '\x20')
  return int.from_bytes(bytes(x, encoding='utf-8'), byteorder='big')

def hash2str(x: int) -> str:
  '''Convert typeID to charID.'''
  assert len(hex(x)) == 10
  return x.to_bytes(length=4, byteorder='big').decode()

def str2id(psstr: str) -> str:
  '''Convert charID or stringID to typeID'''
  assert type(psstr) == str
  if len(psstr) == 4:
    typeid = str2hash(psstr)
    try:
      restr = converter.id2str(psstr)
    except:
      restr = ''
    if not restr:
      typeid = converter.str2id(psstr)
  else:
    typeid = converter.str2id(psstr)
  return typeid

def id2str(typeid: int) -> str:
  '''Convert typeID to stringID'''
  return converter.id2str(typeid)