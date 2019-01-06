# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.basic_option import BasicOption


class EPSSaveOptions(BasicOption, Core):
    object_name = 'EPSSaveOptions'

    def __init__(self):
        super(EPSSaveOptions, self).__init__()


