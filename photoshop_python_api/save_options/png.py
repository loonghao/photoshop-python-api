# Import local modules
from photoshop_python_api._basic_option import BasicOption
from photoshop_python_api.application import Application


class ExportOptionsSaveForWeb(BasicOption, Application):
    object_name = 'ExportOptionsSaveForWeb'

    def __init__(self):
        super(ExportOptionsSaveForWeb, self).__init__()
        self.Format = 13  # PNG
        self.PNG8 = False  # Sets it to PNG-24 bit


class PNGSaveOptions(BasicOption, Application):
    object_name = 'PNGSaveOptions'

    def __init__(self):
        super(PNGSaveOptions, self).__init__()
        self.Interlaced = False
        self.Compression = True

