# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
import os

# Import local modules
from photoshop_python_api._core import Photoshop
# Import built-in modules
from photoshop_python_api.active_document import ActiveDocument
from photoshop_python_api.document import Document
from photoshop_python_api.solid_color import SolidColor


class Application(Photoshop):
    object_name = 'Application'

    def __init__(self, version=None):
        super(Application, self).__init__(version)

    @property
    def document(self):
        return Document()

    @property
    def activeDocument(self):
        return ActiveDocument()

    @property
    def backgroundColor(self):
        return SolidColor

    @property
    def active_layer(self):
        return self.app.ArtLayer

    def active_layer_set(self):
        return self.app.LayerSets

    @property
    def preferences(self):
        return self.app.Preferences

    def open(self, *args, **kwargs):
        self.app.Open(*args, **kwargs)

    @staticmethod
    def system(command):
        os.system(command)
