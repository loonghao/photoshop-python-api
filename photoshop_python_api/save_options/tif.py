# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class TiffSaveOptions(Option, Application):
    object_name = 'TiffSaveOptions'

    def __int__(self):
        super(TiffSaveOptions, self).__init__()
