# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api._basic_option import BasicOption


class BMPSaveOptions(BasicOption, Photoshop):
    object_name = 'BMPSaveOptions'

    def __init__(self):
        super(BMPSaveOptions, self).__init__()
