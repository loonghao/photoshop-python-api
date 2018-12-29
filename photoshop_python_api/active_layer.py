# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from application import Application


class ActiveLayer(Application):
    def __int__(self):
        super(ActiveLayer, self).__init__()

    def add(self):
        self.app.ActiveDocument.ArtLayers.Add()


