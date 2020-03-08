try:
    # python-2.
    import _winreg as winreg
except ImportError:
    # python-3
    import winreg
import os

from comtypes import COMError
from comtypes.client import CreateObject
from photoshop import constants
from photoshop.errors import PhotoshopPythonAPIError


class Photoshop(object):
    _root = 'Photoshop'
    REG_PATH = 'Software\\Adobe\\Photoshop'
    _object_name = 'Application'
    object_name = None

    def __init__(self, ps_version=None, parent=None):
        self._progress_id = None
        version_mappings = constants.PHOTOSHOP_VERSION_MAPPINGS
        self.photoshop_version = os.getenv('PS_VERSION', ps_version)
        version = self._get_install_version()
        self.app_id = version_mappings.get(self.photoshop_version, version)
        try:
            self.app = self.instance_app(self.app_id)
        except OSError:
            try:
                self.app = self.instance_app(self._get_install_version())
            except OSError:
                raise PhotoshopPythonAPIError(
                    'Please check if you have '
                    'Photoshop installed correctly.',
                )
        if parent:
            self.adobe = self.app
            self.app = parent

    @property
    def typename(self):
        return self.__class__.__name__

    def __call__(self, *args, **kwargs):
        return self.app

    def __str__(self):
        return f'{self.__class__.__name__} <{self._progress_id}>'

    def __repr__(self):
        return self

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return getattr(self.app, item)

    def get_application_path(self):
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            f'{self.REG_PATH}\\{self.app_id}',
        )
        return winreg.QueryValueEx(key, 'ApplicationPath')[0] + 'Photoshop'

    def instance_app(self, ps_id):
        naming_space = [self._root]
        if not self.object_name:
            naming_space.append(self._object_name)
        else:
            naming_space.append(self.object_name)
        naming_space.append(ps_id)
        self._progress_id = self._get_name(naming_space)
        return self._create_object(self._progress_id, dynamic=True)

    def _get_install_version(self):
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            self.REG_PATH,
        )
        self.app_id = winreg.EnumKey(key, 0).split('.')[0]
        return self.app_id

    @staticmethod
    def _create_object(*args, **kwargs):
        return CreateObject(*args, **kwargs)

    @staticmethod
    def _get_name(list_):
        return '.'.join(list_)

    def eval_javascript(self, javascript, Arguments=None, ExecutionMode=None):
        return self.adobe.doJavaScript(javascript, Arguments, ExecutionMode)
