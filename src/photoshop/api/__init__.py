"""Python API for Photoshop."""

from . import constants
from .action_descriptor import ActionDescriptor
from .action_reference import ActionReference
from .application import Application
from .colors import CMYKColor, GrayColor, HSBColor, LabColor, RGBColor
from .enumerations import *
from .errors import PhotoshopPythonAPICOMError, PhotoshopPythonAPIError
from .event_id import EventID
from .open_options import EPSOpenOptions
from .save_options import (BMPSaveOptions, ExportOptionsSaveForWeb,
                           GIFSaveOptions, JPEGSaveOptions, PDFSaveOptions,
                           PhotoshopSaveOptions, PNGSaveOptions,
                           TargaSaveOptions, TiffSaveOptions)
from .solid_color import SolidColor
from .text_item import TextItem

__all__ = [
    "ActionDescriptor",
    "ActionReference",
    "Application",
    "constants",
    "enumerations",
    "PhotoshopPythonAPIError",
    "PhotoshopPythonAPICOMError",
    "CMYKColor",
    "GrayColor",
    "HSBColor",
    "LabColor",
    "RGBColor",
    "SolidColor",
    "EventID",
    "BMPSaveOptions",
    "GIFSaveOptions",
    "JPEGSaveOptions",
    "PDFSaveOptions",
    "ExportOptionsSaveForWeb",
    "PNGSaveOptions",
    "PhotoshopSaveOptions",
    "TiffSaveOptions",
    "TargaSaveOptions",
    "EPSOpenOptions",
    "TextItem",
]
