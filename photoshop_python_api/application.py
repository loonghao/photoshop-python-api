# Import built-in modules
import _winreg
import os

# Import third-party modules
from comtypes.client import CreateObject


class PhotoshopPythonAPIError(Exception):
    pass


class Application(object):
    _root = 'Photoshop'
    _object_name = 'Application'
    object_name = None

    def __init__(self, ps_version=None):
        self.mappings = {
            '2019': '130',
            '2018': '120',
            '2017': '110',
            'cs6': '60'
        }
        self.app = None
        self.version = os.getenv('PS_VERSION', ps_version)
        self.app_id = self.mappings.get(self.version,
                                        self._get_photoshop_version())
        try:
            self.ps = self.instance_photoshop(self.app_id)
        except WindowsError:
            try:
                self.ps = self.instance_photoshop(
                    self._get_photoshop_version())
            except WindowsError:
                raise PhotoshopPythonAPIError('Please check if you have '
                                              'Photoshop installed correctly.')

    def instance_photoshop(self, ps_id):
        progress_id = self._get_name([self._root, self._object_name, ps_id])
        if self.object_name:
            progress_id = self._get_name(
                [self._root, self._object_name, ps_id])
            self.app = self._create_object(progress_id)
        return self._create_object(progress_id, dynamic=True)

    def _get_photoshop_version(self):
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                              r"Software\Adobe\Photoshop")
        self.app_id = _winreg.EnumKey(key, 0).split('.')[0]
        return self.app_id

    @staticmethod
    def _create_object(*args, **kwargs):
        return CreateObject(*args, **kwargs)

    @property
    def document(self):
        return self.ps.Document

    @property
    def active_document(self):
        return self.ps.ActiveDocument

    @property
    def active_layer(self):
        return self.ps.ArtLayer

    def active_layer_set(self):
        return self.ps.LayerSets

    @property
    def preferences(self):
        return self.ps.Preferences

    def open(self, *args, **kwargs):
        self.ps.Open(*args, **kwargs)

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)

    def run_jsx(self, jsx):
        id60 = self.ps.stringIDToTypeID("AdobeScriptAutomation Scripts")
        id_ = self._get_name([self._root, 'ActionDescriptor', self.app_id])
        desc12 = self._create_object(id_)
        id61 = self.ps.charIDToTypeID("jsCt")
        desc12.putPath(id61, jsx)
        id62 = self.ps.charIDToTypeID("jsMs")
        desc12.putString(id62, "null")
        self.ps.executeAction(id60, desc12, 2)
