from ..ref_form_types import ReferenceKey

class ActionReference_Iterator:
  def __init__(self, psobj: 'ActionReference'):
    self.curobj = psobj
    self.init = True
    self.n = -1

  def __next__(self) -> ReferenceKey:
    self.n += 1
    if self.init:
      self.init = False
      return ReferenceKey._packer(self.curobj)
    self.curobj = self.curobj.getContainer()
    try:
      self.curobj.getContainer()
    except:
      raise StopIteration
    return ReferenceKey._packer(self.curobj)

  def __repr__(self):
    return '<ActionReference_Iterator at index:%d>'%self.n