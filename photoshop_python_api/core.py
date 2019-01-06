# Import built-in modules
import _winreg
import os
from shutil import rmtree
from tempfile import mkdtemp

# Import third-party modules
from comtypes.client import CreateObject

# Import local modules
from photoshop_python_api.errors import PhotoshopPythonAPIError


class Core(object):
    _root = 'Photoshop'
    REG_PATH = "Software\\Adobe\\Photoshop"
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
        self.__initialised = True

    def get_application_path(self):
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                              "{}\\{}".format(self.REG_PATH, self.app_id))
        return _winreg.QueryValueEx(key, 'ApplicationPath')[
                   0] + 'Photoshop'

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
            self.app = self._create_object(progress_id, dynamic=True)
        progress_id = self._get_name(names)
        return self._create_object(progress_id, dynamic=True)

    def _get_install_version(self):
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                              self.REG_PATH)
        self.app_id = _winreg.EnumKey(key, 0).split('.')[0]
        return self.app_id

    @staticmethod
    def _create_object(*args, **kwargs):
        return CreateObject(*args, **kwargs)

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

    def run_javascript(self, command):
        dir_ = mkdtemp(prefix='photoshop_python_api_')
        js = os.path.join(dir_, 'temp_script.jsx')
        with open(js, 'w') as file_obj:
            file_obj.write(command)
        self.run_jsx(js)
        rmtree(dir_)
