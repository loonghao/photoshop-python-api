"""A record of key-value pairs for actions, such as those included on the
Adobe Photoshop Actions menu. The ActionDescriptor class is part of the Action
Manager functionality. For more details on the Action Manager,
see the Photoshop Scripting Guide."""
from photoshop_python_api.basic_option import BasicOption
from photoshop_python_api.core import Core


class ActionDescriptor(BasicOption, Core):
    object_name = 'ActionDescriptor'

    def __init__(self):
        super(ActionDescriptor, self).__init__()
