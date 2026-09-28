"""Resolve Photoshop automation class IDs when no versioned ProgID is published.

A regular Photoshop installation publishes a versioned ProgID for every automation class
(``Photoshop.ActionDescriptor.190`` and friends), which is what this library resolves
classes through. Some installations -- notably portable or relocated copies -- register
the very same classes under a bare CLSID with no ProgID at all. Those classes are
perfectly creatable, but every ``Photoshop.<Class>`` lookup fails.

This module resolves a coclass name to its CLSID for those installations:

1. Photoshop's own type library is read and indexed. The type library ships with
   Photoshop and declares every automation coclass by name, so this route is exact
   and instantiating anything is not required.
2. If the type library is unavailable, the CLSIDs registered as Photoshop local
   servers are instantiated and asked for their coclass name through
   ``IDispatch::GetTypeInfo``. This only depends on Photoshop itself and is used as a
   last resort, because it instantiates one automation object per candidate CLSID and
   costs roughly a second per candidate.

Both routes are read-only with respect to Photoshop's registration, and results are
cached for the lifetime of the process.
"""

# Import built-in modules
from contextlib import suppress
import os
import platform
from typing import Dict
from typing import List
from typing import Optional
import winreg

# Import third-party modules
from comtypes import CLSCTX_LOCAL_SERVER
from comtypes import COMError
from comtypes import CoCreateInstance
from comtypes import GUID
from comtypes import typeinfo
from comtypes.automation import IDispatch


_PHOTOSHOP_EXE = "photoshop.exe"
_APPLICATION_REG_PATH = "SOFTWARE\\Adobe\\Photoshop"

# Cached lookups, keyed by coclass name. ``None`` records a coclass that could not be
# resolved so a failing lookup is not repeated for every wrapper instantiation.
_CLASS_ID_CACHE: Dict[str, Optional[str]] = {}
_TYPE_LIBRARY_COCLASSES: Optional[List[Dict[str, str]]] = None
_PROBED_COCLASSES: Optional[Dict[str, str]] = None


def resolve_photoshop_class_id(object_name: str) -> Optional[str]:
    """Return the CLSID of a Photoshop coclass, or None when it cannot be resolved.

    Args:
        object_name: Photoshop coclass name, e.g. ``ActionDescriptor``.

    Returns:
        The CLSID formatted as ``{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}``, or None.
    """
    with suppress(KeyError):
        return _CLASS_ID_CACHE[object_name]
    class_id = _lookup_class_id(object_name)
    _CLASS_ID_CACHE[object_name] = class_id
    return class_id


def reset_cache() -> None:
    """Forget every cached lookup. Only useful for tests and long lived processes."""
    _CLASS_ID_CACHE.clear()
    global _TYPE_LIBRARY_COCLASSES
    global _PROBED_COCLASSES
    _TYPE_LIBRARY_COCLASSES = None
    _PROBED_COCLASSES = None


def _lookup_class_id(object_name: str) -> Optional[str]:
    """Look a coclass up in the type libraries first, then on the live automation server."""
    for coclasses in _get_type_library_coclasses():
        with suppress(KeyError):
            return coclasses[object_name]
    return _get_probed_coclasses().get(object_name)


def _get_type_library_coclasses() -> List[Dict[str, str]]:
    """Return every Photoshop type library's coclasses, richest library first."""
    global _TYPE_LIBRARY_COCLASSES
    if _TYPE_LIBRARY_COCLASSES is None:
        coclasses = [_read_coclasses(path) for path in _iter_type_library_paths(_get_photoshop_install_dirs())]
        # A Photoshop install can register several type libraries, some of which only
        # declare a single application class. Prefer the most complete one.
        _TYPE_LIBRARY_COCLASSES = sorted((entry for entry in coclasses if entry), key=len, reverse=True)
    return _TYPE_LIBRARY_COCLASSES


def _get_probed_coclasses() -> Dict[str, str]:
    """Return coclass names reported by the registered Photoshop CLSIDs themselves."""
    global _PROBED_COCLASSES
    if _PROBED_COCLASSES is None:
        coclasses: Dict[str, str] = {}
        for class_id, _ in _iter_photoshop_local_servers():
            name = _probe_coclass_name(class_id)
            if name:
                coclasses.setdefault(name, class_id)
        _PROBED_COCLASSES = coclasses
    return _PROBED_COCLASSES


def _read_coclasses(type_library_path: str) -> Dict[str, str]:
    """Index the coclasses declared by a type library.

    Args:
        type_library_path: Absolute path of a type library (``.tlb``, ``.8li``, ...).

    Returns:
        Mapping of coclass name to CLSID, empty when the library cannot be read.
    """
    coclasses: Dict[str, str] = {}
    with suppress(OSError, COMError):
        library = typeinfo.LoadTypeLibEx(type_library_path)
        for index in range(library.GetTypeInfoCount()):
            if library.GetTypeInfoType(index) != typeinfo.TKIND_COCLASS:
                continue
            info = library.GetTypeInfo(index)
            name = _normalize_coclass_name(info.GetDocumentation(-1)[0] or "")
            if name:
                coclasses.setdefault(name, str(info.GetTypeAttr().guid))
    return coclasses


def _probe_coclass_name(class_id: str) -> Optional[str]:
    """Instantiate a CLSID and read its coclass name back from its type information.

    Args:
        class_id: CLSID to instantiate.

    Returns:
        The coclass name, or None when the CLSID cannot be created or does not report one.
    """
    with suppress(OSError, COMError):
        com_object = CoCreateInstance(GUID(class_id), interface=IDispatch, clsctx=CLSCTX_LOCAL_SERVER)
        name = _normalize_coclass_name(com_object.GetTypeInfo(0, 0).GetDocumentation(-1)[0] or "")
        return name or None
    return None


def _normalize_coclass_name(name: str) -> str:
    """Strip the decoration ``IDispatch`` type information puts around coclass names.

    ``ITypeInfo::GetDocumentation`` reports the coclass as ``_ActionDescriptor`` while the
    type library names the very same coclass ``ActionDescriptor``.

    Args:
        name: Raw coclass name.

    Returns:
        The undecorated coclass name.
    """
    return name.lstrip("_")


def _get_photoshop_install_dirs() -> List[str]:
    """Return every directory Photoshop is installed in."""
    directories = [path for path in _iter_application_path_dirs() if path]
    if not directories:
        # Installations that never wrote the Adobe application key still register their
        # automation classes, so fall back to the directory the local servers live in.
        for _, executable in _iter_photoshop_local_servers():
            _add_unique(directories, os.path.dirname(executable))
    return directories


def _iter_application_path_dirs():
    """Yield the install directories recorded under ``HKLM\\SOFTWARE\\Adobe\\Photoshop``."""
    key = _open_key(winreg.HKEY_LOCAL_MACHINE, _APPLICATION_REG_PATH)
    if key is None:
        return
    with key:
        for version in _iter_sub_keys(key):
            with suppress(OSError):
                with winreg.OpenKey(key, version) as version_key:
                    yield winreg.QueryValueEx(version_key, "ApplicationPath")[0]


def _iter_type_library_paths(install_dirs: List[str]):
    """Yield every distinct registered type library hosted inside one of ``install_dirs``."""
    key = _open_key(winreg.HKEY_CLASSES_ROOT, "TypeLib")
    if key is None:
        return
    seen = set()
    with key:
        for library_id in _iter_sub_keys(key):
            with winreg.OpenKey(key, library_id) as library_key:
                for version in _iter_sub_keys(library_key):
                    with winreg.OpenKey(library_key, version) as version_key:
                        for locale in _iter_sub_keys(version_key):
                            for path in _iter_locale_library_paths(version_key, locale, install_dirs):
                                marker = os.path.normcase(os.path.normpath(path))
                                if marker not in seen:
                                    seen.add(marker)
                                    yield path


def _iter_locale_library_paths(version_key, locale: str, install_dirs: List[str]):
    """Yield the type library files registered for one library locale."""
    with winreg.OpenKey(version_key, locale) as locale_key:
        for architecture in ("win64", "win32"):
            path = None
            with suppress(OSError):
                with winreg.OpenKey(locale_key, architecture) as architecture_key:
                    path = winreg.QueryValue(architecture_key, None)
            if path and _is_within(path, install_dirs):
                yield path


def _iter_photoshop_local_servers():
    """Yield ``(class_id, executable)`` for every COM class hosted by ``Photoshop.exe``."""
    key = _open_key(winreg.HKEY_CLASSES_ROOT, "CLSID")
    if key is None:
        return
    with key:
        for class_id in _iter_sub_keys(key):
            executable = _executable_from_command(_get_local_server_command(key, class_id))
            if executable and os.path.basename(executable).lower() == _PHOTOSHOP_EXE:
                yield class_id, executable


def _get_local_server_command(parent_key, class_id: str) -> Optional[str]:
    """Return the ``LocalServer32`` command of a CLSID, or None when it has none."""
    with suppress(OSError):
        with winreg.OpenKey(parent_key, f"{class_id}\\LocalServer32") as sub_key:
            return winreg.QueryValue(sub_key, None)
    return None


def _executable_from_command(command: Optional[str]) -> Optional[str]:
    """Extract the executable path from a ``LocalServer32`` command line."""
    if not command:
        return None
    command = command.strip()
    if command.startswith('"'):
        end = command.find('"', 1)
        return command[1:end] if end > 0 else None
    return command.split(" ", 1)[0]


def _is_within(path: str, directories: List[str]) -> bool:
    """Return whether ``path`` lives inside one of ``directories``."""
    normalized = os.path.normcase(os.path.normpath(path))
    return any(normalized.startswith(os.path.normcase(os.path.normpath(d))) for d in directories)


def _add_unique(values: List[str], value: Optional[str]):
    """Append ``value`` to ``values`` unless it is empty or already present."""
    if not value:
        return
    normalized = os.path.normcase(os.path.normpath(value))
    if normalized not in {os.path.normcase(os.path.normpath(existing)) for existing in values}:
        values.append(value)


def _iter_sub_keys(key) -> List[str]:
    """Return the sub key names of an open registry key."""
    with suppress(OSError):
        return [winreg.EnumKey(key, index) for index in range(winreg.QueryInfoKey(key)[0])]
    return []


def _open_key(root_key, sub_key: str):
    """Open a registry key with the architecture appropriate view, or None on failure."""
    mappings = {"AMD64": winreg.KEY_WOW64_64KEY}
    access = winreg.KEY_READ | mappings.get(platform.machine(), winreg.KEY_WOW64_32KEY)
    with suppress(OSError):
        return winreg.OpenKey(key=root_key, sub_key=sub_key, access=access)
    return None
