# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api._basic_option import BasicOption


class JPEGSaveOptions(BasicOption, Application):
    object_name = 'JPEGSaveOptions'

    def __init__(self):
        super(JPEGSaveOptions, self).__init__()
        self.Quality = 1
