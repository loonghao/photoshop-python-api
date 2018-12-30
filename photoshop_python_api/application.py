# Import built-in modules
import _winreg
import os

# Import third-party modules
from comtypes.client import CreateObject


class PhotoshopPythonAPIError(Exception):
    pass

class Application(object):
    _root = 'Photoshop'
    object_name = 'Application'

    def __init__(self, ps_version=None):
        self.mappings = {
            '2019': '130',
            '2018': '120',
            '2017': '110',
            'cs6': '60'
        }
        self.version = os.getenv('PS_VERSION', ps_version)
        self.app_id = self.mappings.get(self.version,
                                        self._get_photoshop_version())
        try:
            self.app = self.instance_photoshop(self.app_id)
        except WindowsError:
            try:
                self.app = self.instance_photoshop(self._get_photoshop_version())
            except WindowsError:
                raise PhotoshopPythonAPIError('Please check if you have '
                                              'Photoshop installed correctly.')

    def instance_photoshop(self, ps_id):
        progress_id = self._get_name([self._root, self.object_name, ps_id])
        return CreateObject(progress_id, dynamic=True)

    @staticmethod
    def _get_photoshop_version():
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                              r"Software\Adobe\Photoshop")
        return _winreg.EnumKey(key, 0).split('.')[0]

    @property
    def document(self):
        return self.app.Document

    @property
    def active_document(self):
        return self.app.ActiveDocument

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

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)
