# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api._basic_option import BasicOption


class EPSSaveOptions(BasicOption, Photoshop):
    object_name = 'EPSSaveOptions'

    def __init__(self):
        super(EPSSaveOptions, self).__init__()


