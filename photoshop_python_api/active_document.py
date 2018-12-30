# Import local modules
from photoshop_python_api.application import Application


class ActiveDocument(Application):
    def __int__(self):
        super(ActiveDocument, self).__init__()


    @property
    def layer_sets(self):
        return self.active_document.layer_sets

    @property
    def width(self):
        return self.active_document.width

    @property
    def typename(self):
        return self.active_document.typename

    @property
    def selection(self):
        return self.active_document.selection

    @property
    def saved(self):
        return self.active_document.saved

    @property
    def resolution(self):
        return self.active_document.resolution

    @property
    def quick_mask_mode(self):
        return self.active_document.quickMaskMode

    @property
    def path(self):
        return self.active_document.fullName

    @path.setter
    def path(self, path):
        self.active_document.fullName = path

    def save_as(self, *args, **kwargs):
        self.active_document.SaveAs(*args, **kwargs)

    def save(self):
        self.active_document.Save()

    def add_art_layers(self):
        return self.active_document.ArtLayers.Add()

    def close(self):
        """Closes the document."""
        self.active_document.Close()

    def flatten(self):
        """Flattens all layers."""
        return self.active_document.Flatten()

    def merge_visible_layers(self):
        """Flattens all visible layers in the document."""
        return self.active_document.MergeVisibleLayers()

    def crop(self, **kwargs):
        return self.active_document.Crop(**kwargs)

    def duplicate(self, name, merge_layers_only=False):
        return self.active_document.Duplicate(name, merge_layers_only)

    def resize_image(self, width, height, resolution=72, psAutomatic=8):
        """Changes the size of the image.

        Args:
            width: The desired width of the image.
            height: The desired height of the image.
            resolution: The resolution (in pixels per inch)

        Returns:

        """
        return self.active_document.ResizeImage(width, height, resolution,
                                                psAutomatic)
