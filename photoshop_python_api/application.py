# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
import pywintypes
from win32com.client import Dispatch, GetActiveObject


class Application(object):
    object_name = 'Application'
    _root = 'Photoshop'

    def __init__(self, ps_version='2017'):
        self._version_id_mappings = {
            '2017': '110',
            'cs6': '60'
        }
        self.version = ps_version
        self.app_id = self._version_id_mappings.get(self.version)
        self.progress_id = self._get_name(
            [self._root, self.object_name, self.app_id])
        try:
            self.app = GetActiveObject(self.progress_id)
        except pywintypes.com_error:
            self.app = Dispatch(self.progress_id)

    @property
    def document(self):
        return self.app.Document

    @property
    def active_document(self):
        return self.app.ActiveDocument

    @property
    def active_layer(self):
        return self.app.ActiveLayer

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)
