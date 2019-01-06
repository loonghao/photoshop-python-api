# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from comtypes import COMError


class PhotoshopPythonAPIError(Exception):
    pass


class  PhotoshopPythonAPICOMError(COMError):
    pass
