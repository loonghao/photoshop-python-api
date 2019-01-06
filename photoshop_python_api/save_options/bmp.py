# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.basic_option import BasicOption


class BMPSaveOptions(BasicOption, Core):
    object_name = 'BMPSaveOptions'

    def __init__(self):
        super(BMPSaveOptions, self).__init__()
