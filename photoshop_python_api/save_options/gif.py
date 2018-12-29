# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class GIFSaveOptions(Option, Application):
    object_name = 'GIFSaveOptions'

    def __init__(self):
        super(GIFSaveOptions, self).__init__()
