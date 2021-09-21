"""This class provides all photoshop API core functions."""

# Import built-in modules
import os
import platform
from typing import Any
from typing import List
import winreg

# Import third-party modules
from comtypes.client import CreateObject

# Import local modules
from photoshop.api import constants
from photoshop.api.errors import PhotoshopPythonAPIError


class Photoshop(object):
    _root = "Photoshop"
    REG_PATH = "SOFTWARE\\Adobe\\Photoshop"
    _object_name = "Application"
    object_name: str = None

    def __init__(self, ps_version: str = None, parent: Any = None):
        self._program_name = None
        self._has_parent = False
        version_mappings = constants.PHOTOSHOP_VERSION_MAPPINGS
        self.photoshop_version = os.getenv("PS_VERSION", ps_version)
        if self.photoshop_version:
            # Store current photoshop version.
            os.environ["PS_VERSION"] = self.photoshop_version
        self.app_id = version_mappings.get(self.photoshop_version, "0")
        try:
            self.app = self.instance_app(self.app_id)
        except OSError:
            # get photoshop from registration.
            try:
                self.app = self.instance_app(self._get_program_id())
            except OSError:
                raise PhotoshopPythonAPIError(
                    "Please check if you have Photoshop installed correctly.",
                )
        if parent:
            self.adobe = self.app
            self.app = parent
            self._has_parent = True

    @property
    def typename(self):
        return self.__class__.__name__

    def __call__(self, *args, **kwargs):
        return self.app

    def __str__(self):
        return f"{self.__class__.__name__} <{self._program_name}>"

    def __repr__(self):
        return self

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return getattr(self.app, item)

    @staticmethod
    def open_key(key):
        """Open the register key.

        Args:
            key (str): The key of register.

        Returns:
            str: The handle to the specified key.

        """
        machine_type = platform.machine()
        mappings = {"AMD64": winreg.KEY_WOW64_64KEY}
        platform_type = mappings.get(machine_type, winreg.KEY_WOW64_32KEY)
        try:
            return winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                key,
                access=winreg.KEY_READ | platform_type,
            )
        except FileNotFoundError as err:
            full_reg_path = f"HKEY_LOCAL_MACHINE\\{key}"
            raise PhotoshopPythonAPIError(
                f"Failed to read the registration: <{full_reg_path}>, "
                "please check if you have Photoshop installed correctly."
            ) from err

    def get_application_path(self):
        """str: The absolute path of Photoshop installed location."""
        key = self.open_key(f"{self.REG_PATH}\\{self.get_program_id()}")
        return winreg.QueryValueEx(key, "ApplicationPath")[0]

    def get_plugin_path(self):
        """str: The absolute plugin path of Photoshop."""
        return os.path.join(self.get_application_path(), "Plug-ins")

    def get_presets_path(self):
        """str: The absolute presets path of Photoshop."""
        return os.path.join(self.get_application_path(), "Presets")

    def get_script_path(self):
        """str: The absolute scripts path of Photoshop."""
        return os.path.join(self.get_presets_path(), "Scripts")

    def instance_app(self, ps_id):
        naming_space = [self._root]
        if not self.object_name:
            naming_space.append(self._object_name)
        else:
            naming_space.append(self.object_name)
        naming_space.append(ps_id)
        self._program_name = self._assemble_program_name(naming_space)
        return CreateObject(self._program_name, dynamic=True)

    def get_program_id(self) -> str:
        key = self.open_key(self.REG_PATH)
        index = 0
        while True:
            value = winreg.EnumKey(key, index)
            index += 1
            if value:
                try:
                    self.instance_app(value.split(".")[0])
                except OSError:
                    continue
                return value.split(".")[0]

    def _get_program_id(self) -> str:
        self.app_id = self.get_program_id().split(".")[0]
        return self.app_id

    @staticmethod
    def _assemble_program_name(names: List[str]):
        """Assemble program name of Photoshop.

        Args:
            names (list of str): The name to be assembled.
                .e.g:
                    [
                        'Photoshop',
                        'ActionDescriptor',
                        '140'
                    ]

        Returns:
            str: Assembled name.

        Examples:
            Photoshop.ActionDescriptor
            Photoshop.ActionDescriptor.140
            Photoshop.ActionList
            Photoshop.ActionList.140
            Photoshop.ActionReference
            Photoshop.ActionReference.140
            Photoshop.Application
            Photoshop.Application.140
            Photoshop.BatchOptions
            Photoshop.BatchOptions.140
            Photoshop.BitmapConversionOptions
            Photoshop.BMPSaveOptions
            Photoshop.BMPSaveOptions.140
            Photoshop.CameraRAWOpenOptions
            Photoshop.CameraRAWOpenOptions.140

        """
        return ".".join(names)

    def eval_javascript(self, javascript, Arguments=None, ExecutionMode=None):
        executor = self.app
        if self._has_parent:
            executor = self.adobe
        return executor.doJavaScript(javascript, Arguments, ExecutionMode)
