# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class JPEGSaveOptions(Option, Application):
    object_name = 'JPEGSaveOptions'

    def __init__(self):
        super(JPEGSaveOptions, self).__init__()
        self.Quality = 1
