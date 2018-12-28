# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
import pywintypes
from win32com.client import Dispatch, GetActiveObject


class Application(object):
    def __init__(self, version='2017'):
        defaunt = 'Photoshop.Application'
        self._version_id_mappings = {
            '2017': '110',
            'cs6': '60'
        }
        self.version = version
        self.app_id = self._version_id_mappings.get(self.version)

        self._mappings = {
            '2017': '{}.{}'.format(defaunt, self.app_id),
            'cs6': '{}.{}'.format(defaunt, self.app_id)
        }
        self.dll_version = self._mappings.get(self.version, defaunt)
        try:
            self.app = GetActiveObject(self.dll_version)
        except pywintypes.com_error:
            self.app = Dispatch(self.dll_version)
        # self.dd = GetActiveObject("Photoshop")
