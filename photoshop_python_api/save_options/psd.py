# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class PhotoshopSaveOptions(Option, Application):
    object_name = 'PhotoshopSaveOptions'

    def __int__(self):
        super(PhotoshopSaveOptions, self).__init__()


if __name__ == '__main__':
    p = PhotoshopSaveOptions()

    print p.app
