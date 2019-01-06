# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
# Import built-in modules
import os
from shutil import rmtree
from tempfile import mkdtemp

# Import local modules
from photoshop_python_api.core import Core
from photoshop_python_api.active_document import ActiveDocument
from photoshop_python_api.document import Document
from photoshop_python_api.solid_color import SolidColor


class Application(Core):
    object_name = 'Application'

    def __init__(self):
        super(Application, self).__init__()

    @property
    def document(self):
        return Document()

    @property
    def activeDocument(self):
        return ActiveDocument()

    @property
    def background_color(self):
        return SolidColor()

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

