# Import built-in modules
try:
    # python-2.
    import _winreg as winreg
except ImportError:
    # python-3
    import winreg
import os
from shutil import rmtree
from tempfile import mkdtemp

# Import third-party modules
from comtypes import COMError
from comtypes.client import CreateObject
# Import local modules
from photoshop_python_api.constants import Adobe
from photoshop_python_api.errors import PhotoshopPythonAPIError


class Photoshop:
    _root = 'Photoshop'
    REG_PATH = 'Software\\Adobe\\Photoshop'
    _object_name = 'Application'
    object_name = None

    def __init__(self, ps_version=None, parent=None):
        self._progress_id = None
        version_mappings = Adobe.PHOTOSHOP_VERSION_MAPPINGS
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
            self.app = parent

    def __call__(self, *args, **kwargs):
        return self.app

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
        progress_id = self._get_name(naming_space)
        return self._create_object(progress_id, dynamic=True)

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

    def stringIDToTypeID(self, string):
        return self.app.stringIDToTypeID(string)

    def charIDToTypeID(self, char):
        return self.app.charIDToTypeID(char)

    @property
    def action_descriptor(self):
        name = self._get_name([self._root, 'ActionDescriptor', self.app_id])
        return self._create_object(name)

    def run_jsx(self, jsx):
        """Run a ``.jsx`` in python.

        Args:
            jsx (str): Absolute path of ``.jsx`` file.

        Examples:
            .. code-block:: python

                >>> from photoshop_python_api import Application
                >>> app = Application()
                >>> app.run_jsx("c:/test.jsx")

        """
        try:
            id60 = self.stringIDToTypeID('AdobeScriptAutomation Scripts')
            action = self.action_descriptor
            id61 = self.charIDToTypeID(Adobe.JSCT)
            action.putPath(id61, jsx)
            id62 = self.charIDToTypeID(Adobe.JSMS)
            action.putString(id62, Adobe.NULL)
            self.app.executeAction(id60, action, 2)
        except COMError:
            raise PhotoshopPythonAPIError(
                'The Photoshop is busy, '
                'Please try again.',
            )

    def eval_javascript(self, command):
        """Eval Javascript in python.

        Args:
            command (str): The javascript of Photoshop.

        Examples:
            .. code-block:: python

                >>> from photoshop_python_api import Application
                >>> app = Application()
                >>> jsx = ('var doc = app.activeDocument;'
                ...       'var orig_name = doc.name;'
                ...       'alert(orig_name);')
                >>> app.eval_javascript(jsx)

        """
        dir_ = mkdtemp(prefix='photoshop_python_api_')
        js = os.path.join(dir_, 'temp_script.jsx')
        with open(js, 'w') as file_obj:
            file_obj.write(command)
        self.run_jsx(js)
        rmtree(dir_)
