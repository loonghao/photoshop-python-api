from typing import Any

class ActionList_Iterator:
  def __init__(self, psobj: 'ActionList'):
    self.curobj = psobj
    self.n = -1

  def __next__(self) -> Any:
    self.n += 1
    try:
      elem = self.curobj.uget(self.n)
    except:
      raise StopIteration()
    return elem

  def __repr__(self):
    return '<ActionList_Iterator at index:%d>'%self.n