"""This object provides information about what the action is refering to.

For example, when referring to the name of something you might use keyName.
The reference would also need to know what name you are referring to.
In this case you could use classDocument for the name of the document or
classLayer for the name of the layer.
It can be used for low-level access into Photoshop.Contains data associated
with an ActionDescriptor.

"""
from photoshop._core import Photoshop


class ActionReference(Photoshop):
    object_name = 'ActionReference'

    def __init__(self):
        super().__init__()

    def getContainer(self):
        return self.app.getContainer()

    def getDesiredClass(self):
        return self.app.getDesiredClass()

    def putName(self, key, value):
        return self.app.putName(key, value)

    def putClass(self, value):
        return self.app.putClass(value)
