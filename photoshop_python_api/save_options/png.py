from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class ExportOptionsSaveForWeb(Option, Application):
    object_name = 'ExportOptionsSaveForWeb'

    def __init__(self):
        super(ExportOptionsSaveForWeb, self).__init__()
        self.Format = 13  # PNG
        self.PNG8 = False  # Sets it to PNG-24 bit


class PNGSaveOptions(Option, Application):
    object_name = 'ExportOptionsSaveForWeb'

    def __init__(self):
        super(PNGSaveOptions, self).__init__()
