"""This class provides all photoshop API core functions."""


# Import built-in modules
from __future__ import annotations

import os
import winreg
from contextlib import suppress
from functools import cached_property
from logging import CRITICAL, DEBUG, Logger, getLogger
from typing import Any, List, Optional

# Import third-party modules
from comtypes.client import CreateObject
from comtypes.client.dynamic import _Dispatch as FullyDynamicDispatch
from comtypes.client.lazybind import Dispatch

# Import local modules
from photoshop.api.constants import PHOTOSHOP_VERSION_MAPPINGS
from photoshop.api.errors import PhotoshopPythonAPIError


class Photoshop:
    """Core API for all photoshop objects."""

    _root = "Photoshop"
    _reg_path = "SOFTWARE\\Adobe\\Photoshop"
    object_name: str = "Application"

    def __init__(self, ps_version: Optional[str] = None, parent: Any = None):
        """Initialize the Photoshop core object.

        Args:
            ps_version: Optional, Photoshop version to look for explicitly in registry.
            parent: Optional, parent instance to use as app object.

        """
        # Establish the initial app and program ID
        ps_version = os.getenv("PS_VERSION", ps_version)
        self._app_id = PHOTOSHOP_VERSION_MAPPINGS.get(ps_version, "")
        self._has_parent, self.adobe, self.app = False, None, None

        # Store current photoshop version
        if ps_version:
            os.environ["PS_VERSION"] = ps_version

        # Establish the application object using provided version ID
        if self.app_id:
            self.app = self._get_application_object([self.app_id])
            if not self.app:
                # Attempt unsuccessful
                self._logger.debug(
                    f"Unable to retrieve Photoshop object '{self.typename}' using version '{ps_version}'.",
                )

        # Look for version ID in registry data
        if not self.app:
            versions = self._get_photoshop_versions()
            self.app = self._get_application_object(versions)
            if not self.app:
                # All attempts exhausted
                raise PhotoshopPythonAPIError("Please check if you have Photoshop installed correctly.")

        # Add the parent app object
        if parent:
            self.adobe = self.app
            self.app = parent
            self._has_parent = True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.app(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.typename}"

    def __getattribute__(self, item: str) -> Any:
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
        return os.getenv("PS_DEBUG", "").lower() in ("true", "1", "t")

    @cached_property
    def _logger(self) -> Logger:
        """Logger: Logging object for warning output."""
        logr = getLogger(self.typename)
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
        """str: Formatted program name found in the Windows Classes registry, e.g. Photoshop.Application.140."""
        if self.app_id:
            return f"{self._root}.{self.object_name}.{self.app_id}"
        return f"{self._root}.{self.object_name}"

    @property
    def app_id(self) -> str:
        """str: Photoshop version ID from Windows registry, e.g. 180."""
        return self._app_id

    @app_id.setter
    def app_id(self, value: str) -> None:
        self._app_id = value

    """
    * Private Methods
    """

    def _flag_as_method(self, *names: str) -> None:
        """* This is a hack for Photoshop's broken COM implementation.
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

    def _get_application_object(self, versions: Optional[List[str]] = None) -> Optional[Dispatch]:
        """Try each version string until a valid Photoshop application Dispatch object is returned.

        Args:
            versions: List of Photoshop version ID's found in registry.

        Returns:
            Photoshop application Dispatch object.

        Raises:
            OSError: If a Dispatch object wasn't resolved.

        """
        if versions is None:
            versions = []
        for v in versions:
            self.app_id = v
            with suppress(OSError):
                return CreateObject(self.program_name, dynamic=True)
        return None

    """
    * Public Methods
    """

    def get_application_path(self) -> str:
        """str: The absolute path of Photoshop installed location."""
        key = self._open_key(f"{self._reg_path}\\{self.app_id}")
        return winreg.QueryValueEx(key, "ApplicationPath")[0]

    def get_plugin_path(self) -> str:
        """str: The absolute plugin path of Photoshop."""
        key = self._open_key(f"{self._reg_path}\\{self.app_id}\\PluginPath")
        return winreg.QueryValueEx(key, "")[0]

    def get_presets_path(self) -> str:
        """str: The absolute presets path of Photoshop."""
        key = self._open_key(f"{self._reg_path}\\{self.app_id}\\PresetsPath")
        return winreg.QueryValueEx(key, "")[0]

    def get_script_path(self) -> str:
        """str: The absolute scripts path of Photoshop."""
        key = self._open_key(f"{self._reg_path}\\{self.app_id}\\ScriptPath")
        return winreg.QueryValueEx(key, "")[0]

    def eval_javascript(self, javascript: str, Arguments: Any = None, ExecutionMode: Any = None) -> Any:
        """Instruct the application to execute javascript code."""
        return self.app.DoJavaScript(javascript, Arguments, ExecutionMode)

    """
    * Private Static Methods
    """

    @staticmethod
    def _open_key(key: str) -> Any:
        """Open the register key.

        Args:
            key: Photoshop application key path.

        Returns:
            The handle to the specified key.

        Raises:
            OSError: if registry key cannot be read.

        """
        try:
            return winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
        except OSError:
            raise OSError(f"Unable to find registry key: {key}")
