# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api._basic_option import BasicOption


class PDFSaveOptions(BasicOption, Application):
    object_name = 'PDFSaveOptions'

    def __init__(self):
        super(PDFSaveOptions, self).__init__()


