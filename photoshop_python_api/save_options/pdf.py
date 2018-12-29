# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from photoshop_python_api.application import Application
from photoshop_python_api.save_options.option import Option


class PDFSaveOptions(Option, Application):
    object_name = 'PDFSaveOptions'

    def __init__(self):
        super(PDFSaveOptions, self).__init__()


