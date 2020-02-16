"""ActionDescriptor of photoshop scripting.

A record of key-value pairs for actions, such as those included on the
Adobe Photoshop Actions menu. The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide.

"""
from photoshop._core import Photoshop


class ActionList(Photoshop):
    object_name = 'ActionList'

    def __init__(self):
        super().__init__()

    @property
    def count(self):
        return self.app.count
