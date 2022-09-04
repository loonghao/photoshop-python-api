'''Defines class marker. It is the class of Identifier, Index, Offset.
It is INTERNAL. You should not import or initialize it.'''

class marker:
  def __init__(self, name, value=0):
    self.name = name
    self.value = value
  def __add__(self, other):
    return type(self)(self.name, self.value+other)
  def __repr__(self):
    return '%s+%d'%(self.name, self.value)
  def __eq__(self, other):
    try:
      return self.name == other.name and self.value == other.value
    except:
      return False