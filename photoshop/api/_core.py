"""This class provides all photoshop API core functions."""
# Import built-in modules
from contextlib import suppress
from functools import cached_property
from logging import CRITICAL
from logging import DEBUG
from logging import Logger
from logging import getLogger
import os
import platform
from typing import Any
from typing import List
from typing import Optional
import winreg

# Import third-party modules
from comtypes import COMError
from comtypes.client import CreateObject
from comtypes.client.dynamic import _Dispatch as FullyDynamicDispatch
from comtypes.client.lazybind import Dispatch

# Import local modules
from photoshop.api._clsid import resolution_failure_reason
from photoshop.api._clsid import resolve_photoshop_class_id
from photoshop.api.constants import PHOTOSHOP_VERSION_MAPPINGS
from photoshop.api.errors import PhotoshopPythonAPIError


class Photoshop:
    """Core API for all photoshop objects."""

    _root = "Photoshop"
    _reg_path = "SOFTWARE\\Adobe\\Photoshop"
    object_name: str = "Application"

    def __init__(self, ps_version: Optional[str] = None, parent: Any = None):
        """
        Initialize the Photoshop core object.

        Args:
            ps_version: Optional, Photoshop version to look for explicitly in registry.
            parent: Optional, parent instance to use as app object.
        """
        # Establish the initial app and program ID
        ps_version = os.getenv("PS_VERSION", ps_version)
        self._app_id = PHOTOSHOP_VERSION_MAPPINGS.get(ps_version, "")
        self._has_parent, self.adobe, self.app = False, None, None
        # Every COM lookup attempted while resolving this object, kept for error reporting.
        self._resolution_log: List[str] = []

        # Store current photoshop version
        if ps_version:
            os.environ["PS_VERSION"] = ps_version

        # Establish the application object using provided version ID
        if self.app_id:
            self.app = self._get_application_object([self.app_id])
            if not self.app:
                # Attempt unsuccessful
                self._logger.debug(
                    f"Unable to retrieve Photoshop object '{self.typename}' using version '{ps_version}'."
                )

        # Look for version ID in registry data
        if not self.app:
            versions = self._get_photoshop_versions()
            self.app = self._get_application_object(versions)
            if not self.app:
                # All attempts exhausted
                raise PhotoshopPythonAPIError(self._build_resolution_error())

        # Add the parent app object
        if parent:
            self.adobe = self.app
            self.app = parent
            self._has_parent = True

    def __repr__(self):
        return self

    def __call__(self, *args, **kwargs):
        return self.app

    def __str__(self):
        return f"{self.__class__.__name__} <{self.program_name}>"

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return getattr(self.app, item)

    """
    * Debug Logger
    """

    @cached_property
    def _debug(self) -> bool:
        """bool: Enable DEBUG level in logger if PS_DEBUG environment variable is truthy."""
        return bool(os.getenv("PS_DEBUG", "False").lower() in ["y", "t", "on", "yes", "true"])

    @cached_property
    def _logger(self) -> Logger:
        """Logger: Logging object for warning output."""
        logr = getLogger("photoshop")
        logr.setLevel(DEBUG if self._debug else CRITICAL)
        return logr

    """
    * Properties
    """

    @property
    def typename(self) -> str:
        """str: Current typename."""
        return self.__class__.__name__

    @property
    def program_name(self) -> str:
        """str: Formatted program name found in the Windows Classes registry, e.g. Photoshop.Application.140.

        Examples:
            - Photoshop.ActionDescriptor
            - Photoshop.ActionDescriptor.140
            - Photoshop.ActionList
            - Photoshop.ActionList.140
            - Photoshop.ActionReference
            - Photoshop.ActionReference.140
            - Photoshop.Application
            - Photoshop.Application.140
            - Photoshop.BatchOptions
            - Photoshop.BatchOptions.140
            - Photoshop.BitmapConversionOptions
            - Photoshop.BMPSaveOptions
            - Photoshop.BMPSaveOptions.140
            - Photoshop.CameraRAWOpenOptions
            - Photoshop.CameraRAWOpenOptions.140
        """
        if self.app_id:
            return f"{self._root}.{self.object_name}.{self.app_id}"
        return f"{self._root}.{self.object_name}"

    @property
    def app_id(self) -> str:
        """str: Photoshop version ID from Windows registry, e.g. 180."""
        return self._app_id

    @app_id.setter
    def app_id(self, value: str):
        self._app_id = value

    """
    * Private Methods
    """

    def _flag_as_method(self, *names: str):
        """
        * This is a hack for Photoshop's broken COM implementation.
        * Photoshop does not implement 'IDispatch::GetTypeInfo', so when
        getting a field from the COM object, comtypes will first try
        to fetch it as a property, then treat it as a method if it fails.
        * In this case, Photoshop does not return the proper error code, since it
        blindly treats the property getter as a method call.
        * Fortunately, comtypes provides a way to explicitly flag methods.
        """
        if isinstance(self.app, FullyDynamicDispatch):
            self.app._FlagAsMethod(*names)

    def _get_photoshop_versions(self) -> List[str]:
        """Retrieve a list of Photoshop version ID's from registry."""
        with suppress(OSError, IndexError):
            key = self._open_key(self._reg_path)
            key_count = winreg.QueryInfoKey(key)[0]
            versions = [winreg.EnumKey(key, i).split(".")[0] for i in range(key_count)]
            # Sort from latest version to oldest, use blank version as a fallback
            return [*sorted(versions, reverse=True), ""]
        self._logger.debug("Unable to find Photoshop version number in HKEY_LOCAL_MACHINE registry!")
        return []

    def _get_application_object(self, versions: List[str] = None) -> Optional[Dispatch]:
        """
        Try each version string until a valid Photoshop application Dispatch object is returned.

        Installations that publish no versioned ProgID, such as portable or relocated copies of
        Photoshop, are resolved through their CLSID once every ProgID lookup has failed.

        Args:
            versions: List of Photoshop version ID's found in registry.

        Returns:
            Photoshop application Dispatch object.

        Raises:
            OSError: If a Dispatch object wasn't resolved.
        """
        for v in versions:
            self.app_id = v
            with suppress(OSError):
                return CreateObject(self.program_name, dynamic=True)
            self._resolution_log.append(f"Program ID '{self.program_name}' could not be created.")
        return self._create_object_from_class_id()

    def _create_object_from_class_id(self) -> Optional[Dispatch]:
        """
        Create the automation object straight from its CLSID.

        Some Photoshop installations never publish the versioned ``Photoshop.<Class>.<version>``
        ProgIDs and only register a bare CLSID. Those classes are still perfectly creatable, so
        fall back to resolving the CLSID instead of reporting Photoshop as missing.

        Returns:
            Photoshop application Dispatch object, or None if no CLSID could be created.
        """
        try:
            class_id = resolve_photoshop_class_id(self.object_name)
        except Exception as error:
            # Resolving reads the registry and may instantiate automation objects. A failure
            # there must not replace the diagnosis below with an unrelated traceback.
            self._resolution_log.append(f"Class ID lookup for '{self.object_name}' failed: {error!r}.")
            self._logger.debug(f"Class ID lookup for '{self.typename}' raised {error!r}.")
            return None
        if not class_id:
            reason = resolution_failure_reason(self.object_name)
            self._resolution_log.append(f"No CLSID is registered for '{self.object_name}': {reason}")
            return None
        with suppress(OSError, COMError):
            return CreateObject(class_id, dynamic=True)
        self._resolution_log.append(f"CLSID '{class_id}' for '{self.object_name}' could not be created.")
        self._logger.debug(f"Unable to create Photoshop object '{self.typename}' from CLSID {class_id}.")
        return None

    def _build_resolution_error(self) -> str:
        """Build the message raised when no Photoshop automation object could be resolved."""
        attempts = "\n".join(f"  - {entry}" for entry in self._resolution_log)
        return (
            f"Unable to resolve the Photoshop COM object '{self.typename}'.\n"
            f"{attempts}\n"
            "Please check if you have Photoshop installed correctly.\n"
            "Class IDs are cached for the lifetime of the process; call "
            "photoshop.api._clsid.reset_cache() if Photoshop was started or upgraded "
            "after this process began."
        )

    """
    * Public Methods
    """

    def get_application_path(self) -> str:
        """str: The absolute path of Photoshop installed location."""
        key = self.open_key(f"{self._reg_path}\\{self.program_id}")
        return winreg.QueryValueEx(key, "ApplicationPath")[0]

    def get_plugin_path(self) -> str:
        """str: The absolute plugin path of Photoshop."""
        return os.path.join(self.application_path, "Plug-ins")

    def get_presets_path(self) -> str:
        """str: The absolute presets path of Photoshop."""
        return os.path.join(self.application_path, "Presets")

    def get_script_path(self) -> str:
        """str: The absolute scripts path of Photoshop."""
        return os.path.join(self.presets_path, "Scripts")

    def eval_javascript(self, javascript: str, Arguments: Any = None, ExecutionMode: Any = None) -> str:
        """Instruct the application to execute javascript code."""
        executor = self.adobe if self._has_parent else self.app
        return executor.doJavaScript(javascript, Arguments, ExecutionMode)

    """
    * Private Static Methods
    """

    @staticmethod
    def _open_key(key: str) -> winreg.HKEYType:
        """Open the register key.

        Args:
            key: Photoshop application key path.

        Returns:
            The handle to the specified key.

        Raises:
            OSError: if registry key cannot be read.
        """
        machine_type = platform.machine()
        mappings = {"AMD64": winreg.KEY_WOW64_64KEY}
        access = winreg.KEY_READ | mappings.get(machine_type, winreg.KEY_WOW64_32KEY)
        try:
            return winreg.OpenKey(key=winreg.HKEY_LOCAL_MACHINE, sub_key=key, access=access)
        except FileNotFoundError as err:
            raise OSError(
                "Failed to read the registration: <{path}>\n"
                "Please check if you have Photoshop installed correctly.".format(path=f"HKEY_LOCAL_MACHINE\\{key}")
            ) from err
