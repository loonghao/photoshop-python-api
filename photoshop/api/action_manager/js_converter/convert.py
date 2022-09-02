from .node_execjs import execjs
from .injection_js import injection
from ..utils import str2id, id2str, str2hash, hash2str
from ..desc_value_types import *
from ..ref_form_types import *
import json

def toid(string):
  head = str(string)[:7]
  if head  == 'CharID_':
    out = TypeID(id2str(str2hash(string[7:].ljust(4))))
  elif head == 'StrnID_':
    out = TypeID(string[7:])
  else:
    out = string
  return out

def unhead(string):
  head = str(string)[:7]
  if head  == 'CharID_':
    out = id2str(str2hash(string[7:].ljust(4)))
  elif head == 'StrnID_':
    out = string[7:]
  else:
    out = string
  return out

str2getpacker = {
    'UnitDouble':lambda x: UnitDouble(unhead(x['unit']), x['double']),
    'Enumerated':lambda x: Enumerated(unhead(x['enumtype']), unhead(x['enumval'])),
    'TypeID': lambda x: toid(x['string']),
    'ActionDescriptor':lambda x: parsedict(x),
    'ActionReference':lambda x: parseref(x),
    'ActionList':lambda x: parselist(x),
    }
str2refgetpacker = {
    'default':lambda x: ReferenceKey(unhead(x['DesiredClass']), unhead(x['Value'])),
    'Enumerated':lambda x: ReferenceKey(unhead(x['DesiredClass']), Enumerated(unhead(x['Value']['enumtype']), unhead(x['Value']['enumval']))),
    'Identifier':lambda x: ReferenceKey(unhead(x['DesiredClass']), Identifier+int(x['Value'])),
    'Index':lambda x: ReferenceKey(unhead(x['DesiredClass']), Index+int(x['Value'])),
    'Offset':lambda x: ReferenceKey(unhead(x['DesiredClass']), Offset+int(x['Value'])),
    'Property':lambda x: ReferenceKey(unhead(x['DesiredClass']), toid(x['Value'])),
    }

def parsedict(tdict):
  if not '_classID' in tdict:
    tdict['_classID'] = None
  else:
    tdict['_classID'] = unhead(tdict['_classID'])
  pdict = {unhead(k):(
    str2getpacker[v['type']](v) \
    if type(v) == dict \
    else v
  ) for k,v in tdict.items()}
  del pdict['type']
  return pdict

def parselist(tdict):
  d2l = [tdict[str(i)] for i in range(tdict['len'])]
  plist = [(
    str2getpacker[e['type']](e) \
    if type(e) == dict \
    else e
  ) for e in d2l]
  return plist

def parseref(tdict):
  d2l = [tdict[str(i)] for i in range(tdict['len'])]
  plist = ['!ref']
  plist.extend(
    [(
      str2refgetpacker[val['type']](e) \
      if type(val := e['Value']) == dict \
      else str2refgetpacker['default'](e)\
    )for e in d2l]
  )
  return plist

def json2obj(jsont):
  obj_init = json.loads(jsont)
  obj_desc = parsedict(obj_init['ActionDescriptor']) if 'ActionDescriptor' in obj_init else None
  obj_operation = unhead(obj_init['Operation'])
  obj_option = obj_init['Option']
  return (obj_operation,obj_desc,obj_option)

def dump(jst):
  jsi = injection + '\n' + jst
  jsont = execjs(jsi)
  objs = [json2obj(j) for j in jsont.split('END OF JSON') if j != '\n']
  return objs
  