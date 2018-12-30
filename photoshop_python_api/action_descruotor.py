from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api.application import Application


class ActionDescriptor(BasicOption, Application):
    object_name = 'ActionDescriptor'

    def __init__(self):
        super(ActionDescriptor, self).__init__()

