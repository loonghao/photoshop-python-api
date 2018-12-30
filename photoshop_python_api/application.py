# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""

from photoshop_python_api._core import Core
from photoshop_python_api.active_document import ActiveDocument
from photoshop_python_api.solid_color import SolidColor


class Application(Core):
    object_name = 'Application'

    def __init__(self):
        super(Application, self).__init__()

    @property
    def document(self):
        return self.app.Document

    @property
    def active_document(self):
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

    def run_jsx(self, jsx):
        id60 = self.app.stringIDToTypeID("AdobeScriptAutomation Scripts")
        id_ = self._get_name([self._root, 'ActionDescriptor', self.app_id])
        desc12 = self._create_object(id_)
        id61 = self.app.charIDToTypeID("jsCt")
        desc12.putPath(id61, jsx)
        id62 = self.app.charIDToTypeID("jsMs")
        desc12.putString(id62, "null")
        self.app.executeAction(id60, desc12, 2)
