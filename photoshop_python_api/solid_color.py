# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api._basic_option import BasicOption


class SolidColor(BasicOption, Application):
    object_name = 'SolidColor'

    def __int__(self):
        super(SolidColor, self).__init__()
