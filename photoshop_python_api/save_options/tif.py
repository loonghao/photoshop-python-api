# Import local modules
from photoshop_python_api._core import Photoshop
from photoshop_python_api._basic_option import BasicOption


class TiffSaveOptions(BasicOption, Photoshop):
    object_name = 'TiffSaveOptions'

    def __int__(self):
        super(TiffSaveOptions, self).__init__()
