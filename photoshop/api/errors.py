# Import third-party modules
from __future__ import annotations

from comtypes import COMError


class PhotoshopPythonAPIError(Exception):
    pass


class PhotoshopPythonAPICOMError(COMError):
    pass


__all__ = ["PhotoshopPythonAPICOMError", "PhotoshopPythonAPIError"]
