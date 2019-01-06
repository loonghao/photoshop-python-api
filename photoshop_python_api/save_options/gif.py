# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.basic_option import BasicOption


class GIFSaveOptions(BasicOption, Core):
    object_name = 'GIFSaveOptions'

    def __init__(self):
        super(GIFSaveOptions, self).__init__()
        # self.Colors
        # self.Dither
        # self.DitherAmount
        # self.Forced