#Format it like json!
#Just literal processing.

def jformat(astr, indent=4, prefix=None):
  all_am_keywords = [  # noqa: F405
    'str2id',
    'id2str',
    'Enumerated',
    'TypeID',
    'UnitDouble',
    'Identifier',
    'Index',
    'Offset',
    'ReferenceKey',
    'dumpjs',
    'jprint',
    'jformat',
  ]
  nstr = ''
  indent_level = 0
  insmall = False
  insquote = False
  indquote = False
  aftercomma = False
  for i in range(len(astr)):
    char = astr[i]
    if aftercomma:
      aftercomma = False
      if char == ' ':
        continue
    if char == '(':
      insmall = True
    if char == ')':
      insmall = False
    if char == '"':
      insquote = not insquote
    if char == '\'':
      indquote = not indquote
    if insquote or indquote:
      nstr += char
      continue
    if char in ',[]{}':
      if char == ',' and not insmall:
        char = char+'\n'+' '*(indent*indent_level)
        aftercomma = True
      if char in '[{':
        indent_level += 1
        char = char+'\n'+' '*(indent*indent_level)
      if char in ']}':
        indent_level -= 1
        char = '\n'+' '*(indent*indent_level)+char
    nstr += char
  if not prefix is None:
    for kwd in all_am_keywords:
      nstr = nstr.replace(kwd, prefix+'.'+kwd)
  return nstr

def jprint(obj, indent=4):
  print(jformat(repr(obj), indent=indent))