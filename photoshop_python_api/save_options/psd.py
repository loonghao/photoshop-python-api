# Import local modules
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class PhotoshopSaveOptions(Option, Application):
    object_name = 'PhotoshopSaveOptions'

    def __int__(self):
        super(PhotoshopSaveOptions, self).__init__()
        # If true, the alpha channels are saved.
        self.AlphaChannels = False
        # If true, the annotations are save
        self.annotationsProperty = False
        self.layers = True

if __name__ == '__main__':
    p = PhotoshopSaveOptions()

    print p.app
