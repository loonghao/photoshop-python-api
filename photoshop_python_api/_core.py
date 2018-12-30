# Import built-in modules
import _winreg
import os

# Import third-party modules
from comtypes.client import CreateObject


class PhotoshopPythonAPIError(Exception):
    pass


class Core(object):
    _root = 'Photoshop'
    _object_name = 'Application'
    object_name = None
    sub_object_name = None

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
                                        self._get_install_version())
        try:
            self.ps = self.instance_app(self.app_id)
        except WindowsError:
            try:
                self.ps = self.instance_app(self._get_install_version())
            except WindowsError:
                raise PhotoshopPythonAPIError('Please check if you have '
                                              'Photoshop installed correctly.')

    def instance_app(self, ps_id):
        names = [self._root]
        if not self.object_name:
            names.append(self._object_name)
        else:
            names.append(self.object_name)
        if self.sub_object_name:
            names.append(self.sub_object_name)
        names.append(ps_id)
        if self.object_name:
            progress_id = self._get_name(names)
            self.app = self._create_object(progress_id)
        progress_id = self._get_name(names)
        return self._create_object(progress_id)

    def _get_install_version(self):
        key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                              r"Software\Adobe\Photoshop")
        self.app_id = _winreg.EnumKey(key, 0).split('.')[0]
        return self.app_id

    @staticmethod
    def _create_object(*args, **kwargs):
        return CreateObject(*args, **kwargs)

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)
