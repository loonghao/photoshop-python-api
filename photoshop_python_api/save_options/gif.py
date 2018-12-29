# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api._basic_option import BasicOption


class GIFSaveOptions(BasicOption, Application):
    object_name = 'GIFSaveOptions'

    def __init__(self):
        super(GIFSaveOptions, self).__init__()
