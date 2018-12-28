# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from win32com.client import Dispatch

from photoshop_python_api.application import Application


class SaveOptions(Application):

    @property
    def tiff(self):
        return Dispatch('Photoshop.TiffSaveOptions.{}'.format(self.app_id))

    @property
    def psd(self):
        return Dispatch('Photoshop.PhotoshopSaveOptions.{}'.format(self.app_id))


if __name__ == '__main__':
    s = SaveOptions()
    print s.app
