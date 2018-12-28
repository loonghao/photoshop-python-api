# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from photoshop_python_api.application import Application


class ActiveDocument(Application):

    @property
    def path(self):
        return self.app.ActiveDocument.fullName

    @path.setter
    def path(self, path):
        self.app.ActiveDocument.fullName = path

    def save_as(self, *args, **kwargs):
        self.app.ActiveDocument.SaveAs(*args, **kwargs)

    def add_art_layers(self):
        return self.app.ActiveDocument.ArtLayers.Add()

    def add_text(self, text_item, **kwargs):
        layer = self.add_art_layers()
        text_item = text_item
