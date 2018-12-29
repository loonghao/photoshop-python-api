# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from photoshop_python_api.application import Application


class ActiveDocument(Application):
    def __int__(self):
        super(ActiveDocument, self).__init__()
        
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

    def save(self, *args, **kwargs):
        self.active_document.Save(*args, **kwargs)

    def add_art_layers(self):
        return self.active_document.ArtLayers.Add()

    def close(self, **kwargs):
        self.active_document.Close(**kwargs)

    # def Export(self, Options, *args, **kwargs):
    #     self.active_document.ActiveDocument.Export(*args, **kwargs)

    def add_text(self, text_item, **kwargs):
        layer = self.add_art_layers()
        text_item = text_item
