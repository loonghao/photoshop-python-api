# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api._basic_option import BasicOption


class PDFSaveOptions(BasicOption, Photoshop):
    object_name = 'PDFSaveOptions'

    def __init__(self):
        super(PDFSaveOptions, self).__init__()


