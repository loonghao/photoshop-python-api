"""Tests for the real class ID resolution path: type library indexing and registry walking.

The tests in ``test_clsid_fallback.py`` stub out the resolver to cover how the fallback is
wired into ``Photoshop``. These tests do the opposite and run the resolver itself, so a
broken type library index cannot pass unnoticed. Everything below works against an
in-memory registry and a fake type library, so no Photoshop installation is required.
"""

# Import built-in modules
import os

# Import third-party modules
import pytest

# Import local modules
from photoshop.api import _clsid
from photoshop.api import _core
from photoshop.api.errors import PhotoshopPythonAPIError

PS_BIN = os.path.join("C:", os.sep, "Adobe", "Photoshop 2024")
PS_BETA_BIN = os.path.join("C:", os.sep, "Adobe", "Photoshop 2024 Beta")
PHOTOSHOP_EXE = os.path.join(PS_BIN, "Photoshop.exe")
EXE_NO_SPACES = os.path.join("C:", os.sep, "Adobe", "Photoshop2024", "Photoshop.exe")

SCRIPTING_LIB = os.path.join(PS_BIN, "Required", "Plug-ins", "Extensions", "ScriptingSupport.8li")
APPLICATION_LIB = os.path.join(PS_BIN, "TypeLibrary.tlb")
BETA_LIB = os.path.join(PS_BETA_BIN, "Required", "Plug-ins", "Extensions", "ScriptingSupport.8li")

ACTION_DESCRIPTOR_CLSID = "{B907FC78-A0EB-4DCA-BC8C-4E36718E1DC9}"
SOLID_COLOR_CLSID = "{A215FAEF-98B6-4388-BE36-2986DCD955B1}"
APPLICATION_CLSID = "{18455259-BEE7-442C-89FE-DE31ED630B2B}"


@pytest.fixture(autouse=True)
def _reset_clsid_cache():
    """Reset the process wide caches so tests never observe each other's lookups."""
    _clsid.reset_cache()
    yield
    _clsid.reset_cache()


def type_library_tree():
    """Build a registry tree describing one installed Photoshop with type libraries."""
    return {
        "HKEY_LOCAL_MACHINE": {"SOFTWARE": {"Adobe": {"Photoshop": {"190.0": {"ApplicationPath": PS_BIN + os.sep}}}}},
        "HKEY_CLASSES_ROOT": {
            "TypeLib": {
                "{SCRIPTING}": {"1.0": {"0": {"win64": {None: SCRIPTING_LIB}}}},
                "{APPLICATION}": {"1.0": {"0": {"win32": {None: APPLICATION_LIB}}}},
            },
            "CLSID": {
                "{APP-CLSID}": {"LocalServer32": {None: f'"{PHOTOSHOP_EXE}" /Automation'}},
            },
        },
    }


"""
* Fake Windows registry
"""


class FakeKey:
    """A handle into :class:`FakeRegistry`, carrying the path it was opened with."""

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        """Match the real ``PyHKEY`` interface."""
        return self

    def __exit__(self, *exc_info):
        """Match the real ``PyHKEY`` interface."""
        self.Close()
        return False

    def Close(self):
        """Match the real ``PyHKEY`` interface."""


class FakeRegistry:
    """An in-memory stand-in for the :mod:`winreg` functions used by ``_clsid``.

    The tree is a nested dict of sub key names; a ``None`` key holds the default value.
    """

    def __init__(self, tree):
        self.tree = tree
        self.HKEY_CLASSES_ROOT = "HKEY_CLASSES_ROOT"
        self.HKEY_LOCAL_MACHINE = "HKEY_LOCAL_MACHINE"

    def _node(self, key):
        node = self.tree
        for part in key.path:
            if not isinstance(node, dict) or part not in node:
                raise FileNotFoundError(key.path)
            node = node[part]
        return node

    def OpenKey(self, key, sub_key=None, access=0):
        """Open a sub key, raising ``FileNotFoundError`` when the path does not exist."""
        base = key.path if isinstance(key, FakeKey) else (key,)
        candidate = FakeKey(base + tuple(part for part in sub_key.split(os.sep) if part))
        self._node(candidate)
        return candidate

    def EnumKey(self, key, index):
        """Return the name of the index-th sub key."""
        return sorted(name for name in self._node(key) if name is not None)[index]

    def QueryInfoKey(self, key):
        """Return ``(sub_key_count, value_count, modified_at)``."""
        node = self._node(key)
        return (len([name for name in node if name is not None]), 0, 0)

    def _value(self, key, name):
        """Return a named value, raising ``FileNotFoundError`` like the real registry."""
        node = self._node(key)
        if name not in node:
            raise FileNotFoundError((key.path, name))
        return node[name]

    def QueryValue(self, key, sub_key=None):
        """Return the default value of a key."""
        return self._value(key, None)

    def QueryValueEx(self, key, name):
        """Return ``(value, type_id)`` for a named value."""
        return (self._value(key, name), 1)


@pytest.fixture()
def registry(monkeypatch):
    """Replace ``winreg`` with an in-memory registry and return the mutable tree."""
    tree = {}
    fake = FakeRegistry(tree)
    monkeypatch.setattr(_clsid, "winreg", fake)
    monkeypatch.setattr(_clsid, "_open_key", lambda root, sub_key: safe_open(fake, root, sub_key))
    return tree


def safe_open(registry, root, sub_key):
    """Open ``sub_key`` under ``root``, returning None instead of raising."""
    try:
        return registry.OpenKey(root, sub_key)
    except OSError:
        return None


"""
* Fake type library
"""


class FakeTypeAttr:
    """Stand-in for ``comtypes`` ``TYPEATTR``, exposing only the coclass GUID."""

    def __init__(self, guid):
        self.guid = guid


class FakeTypeInfo:
    """Stand-in for ``comtypes`` ``ITypeInfo``."""

    def __init__(self, name, guid):
        self._name = name
        self._guid = guid

    def GetDocumentation(self, index):
        """Return ``(name, doc_string, help_context, help_file)``."""
        return (self._name, "", 0, "")

    def GetTypeAttr(self):
        """Return the attributes of this type."""
        return FakeTypeAttr(self._guid)


class FakeTypeLib:
    """Stand-in for ``comtypes`` ``ITypeLib``, mixing coclasses with other type kinds."""

    def __init__(self, entries):
        self._entries = entries

    def GetTypeInfoCount(self):
        """Return how many types the library declares."""
        return len(self._entries)

    def GetTypeInfoType(self, index):
        """Return the kind of the index-th type."""
        return self._entries[index][0]

    def GetTypeInfo(self, index):
        """Return the index-th type."""
        return self._entries[index][1]


def coclass(name, guid):
    """Build a coclass entry for :class:`FakeTypeLib`."""
    return (_clsid.typeinfo.TKIND_COCLASS, FakeTypeInfo(name, guid))


def not_a_coclass(name):
    """Build a non-coclass entry, which the indexer must skip."""
    return (_clsid.typeinfo.TKIND_DISPATCH, FakeTypeInfo(name, "{00000000-0000-0000-0000-000000000000}"))


@pytest.fixture()
def load_type_lib(monkeypatch):
    """Patch type library loading and return a mapping of paths to fake libraries."""
    libraries = {}
    errors = {}

    def load(path):
        if path in errors:
            raise errors[path]
        return libraries[path]

    monkeypatch.setattr(_clsid.typeinfo, "LoadTypeLibEx", load)
    return {"libraries": libraries, "errors": errors}


"""
* Pure helpers
"""


@pytest.mark.parametrize(
    ("command", "expected"),
    [
        (f'"{PHOTOSHOP_EXE}" /Automation', PHOTOSHOP_EXE),
        (f"{EXE_NO_SPACES} /Automation", EXE_NO_SPACES),
        (EXE_NO_SPACES, EXE_NO_SPACES),
        ('"C:\\Adobe\\Photoshop.exe', None),  # unterminated quote
        ("", None),
        (None, None),
    ],
)
def test_executable_from_command(command, expected):
    """The executable of a LocalServer32 command line is extracted, quotes included."""
    assert _clsid._executable_from_command(command) == expected


@pytest.mark.parametrize(
    ("path", "directory", "expected"),
    [
        (SCRIPTING_LIB, PS_BIN, True),
        (SCRIPTING_LIB, PS_BIN + os.sep, True),
        (PS_BIN, PS_BIN, True),
        # A sibling sharing a name prefix is not inside the install directory.
        (BETA_LIB, PS_BIN, False),
        (BETA_LIB, PS_BETA_BIN, True),
        (os.path.join("C:", os.sep, "Other", "lib.tlb"), PS_BIN, False),
    ],
)
def test_is_within_is_anchored_on_a_separator(path, directory, expected):
    """Sibling directories that share a name prefix are not treated as contained."""
    assert _clsid._is_within(path, [directory]) is expected


def test_is_within_ignores_case():
    """Windows paths compare case insensitively."""
    assert _clsid._is_within(SCRIPTING_LIB.lower(), [PS_BIN.upper()])


"""
* Type library indexing
"""


def test_read_coclasses_indexes_coclasses_and_skips_other_types(load_type_lib):
    """Only coclasses are indexed, and their names are normalized."""
    load_type_lib["libraries"][SCRIPTING_LIB] = FakeTypeLib(
        [
            coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID),
            not_a_coclass("IActionDescriptor"),
            coclass("_SolidColor", SOLID_COLOR_CLSID),
        ]
    )

    assert _clsid._read_coclasses(SCRIPTING_LIB) == {
        "ActionDescriptor": ACTION_DESCRIPTOR_CLSID,
        "SolidColor": SOLID_COLOR_CLSID,
    }


def test_read_coclasses_returns_empty_when_library_has_no_coclass(load_type_lib):
    """A library declaring no coclass yields an empty index rather than an error."""
    load_type_lib["libraries"][APPLICATION_LIB] = FakeTypeLib([not_a_coclass("ISomething")])

    assert _clsid._read_coclasses(APPLICATION_LIB) == {}


def test_read_coclasses_returns_empty_when_library_cannot_be_loaded(load_type_lib):
    """An unreadable library is skipped instead of aborting the whole resolution."""
    load_type_lib["errors"][SCRIPTING_LIB] = OSError("library is not a type library")

    assert _clsid._read_coclasses(SCRIPTING_LIB) == {}


def test_read_coclasses_keeps_what_it_indexed_before_a_failure(load_type_lib):
    """A library that fails part way through contributes what was read so far."""

    class BrokenTypeLib(FakeTypeLib):
        """A library that reports two types but cannot describe the second one."""

        def GetTypeInfo(self, index):
            if index:
                raise OSError("corrupt type library")
            return self._entries[index][1]

    load_type_lib["libraries"][SCRIPTING_LIB] = BrokenTypeLib(
        [coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID), not_a_coclass("Broken")]
    )

    assert _clsid._read_coclasses(SCRIPTING_LIB) == {"ActionDescriptor": ACTION_DESCRIPTOR_CLSID}


"""
* Registry walking
"""


def test_iter_type_library_paths_finds_libraries_inside_the_install_dir(registry):
    """Registered type libraries hosted by Photoshop are found, both architectures."""
    registry.update(type_library_tree())

    found = list(_clsid._iter_type_library_paths([PS_BIN]))

    assert sorted(found) == sorted([SCRIPTING_LIB, APPLICATION_LIB])


def test_iter_type_library_paths_excludes_other_installations(registry):
    """A sibling install that shares a name prefix does not contribute its library."""
    registry.update(type_library_tree())
    registry["HKEY_CLASSES_ROOT"]["TypeLib"]["{BETA}"] = {"1.0": {"0": {"win64": {None: BETA_LIB}}}}

    found = list(_clsid._iter_type_library_paths([PS_BIN]))

    assert sorted(found) == sorted([SCRIPTING_LIB, APPLICATION_LIB])
    assert BETA_LIB not in found


def test_iter_type_library_paths_returns_nothing_without_an_install_dir(registry):
    """No install directory short circuits the walk instead of scanning the whole hive."""
    registry.update(type_library_tree())

    assert list(_clsid._iter_type_library_paths([])) == []


def test_iter_type_library_paths_does_not_open_the_hive_without_an_install_dir(registry, monkeypatch):
    """Without an install directory the TypeLib hive is never opened at all."""
    registry.update(type_library_tree())
    opened = []
    real_open = _clsid._open_key

    def spy(root, sub_key):
        opened.append(sub_key)
        return real_open(root, sub_key)

    monkeypatch.setattr(_clsid, "_open_key", spy)

    assert list(_clsid._iter_type_library_paths([])) == []
    assert opened == []


def test_iter_type_library_paths_yields_each_path_once(registry):
    """A library registered for both architectures and several locales is yielded once."""
    registry.update(type_library_tree())
    locale = registry["HKEY_CLASSES_ROOT"]["TypeLib"]["{SCRIPTING}"]["1.0"]["0"]
    locale["win32"] = {None: SCRIPTING_LIB}
    registry["HKEY_CLASSES_ROOT"]["TypeLib"]["{SCRIPTING}"]["1.0"]["409"] = {"win64": {None: SCRIPTING_LIB}}

    assert list(_clsid._iter_type_library_paths([PS_BIN])).count(SCRIPTING_LIB) == 1


def test_iter_type_library_paths_tolerates_missing_and_unreadable_keys(registry, monkeypatch):
    """Registry keys that vanish mid-walk are skipped rather than raising."""
    registry.update(type_library_tree())
    real_open = _clsid.winreg.OpenKey

    def flaky_open(key, sub_key=None, access=0):
        if sub_key == "{APPLICATION}":
            raise FileNotFoundError(sub_key)
        return real_open(key, sub_key)

    monkeypatch.setattr(_clsid.winreg, "OpenKey", flaky_open)

    assert list(_clsid._iter_type_library_paths([PS_BIN])) == [SCRIPTING_LIB]


def test_get_photoshop_install_dirs_prefers_the_adobe_application_key(registry):
    """The install directory comes from the Adobe application key when it is present."""
    registry.update(type_library_tree())

    assert _clsid._get_photoshop_install_dirs() == [PS_BIN + os.sep]


def test_get_photoshop_install_dirs_falls_back_to_local_servers(registry):
    """Without the Adobe key the install dir is derived from the registered local server."""
    tree = type_library_tree()
    # An install that never wrote the application path at all.
    tree["HKEY_LOCAL_MACHINE"]["SOFTWARE"]["Adobe"]["Photoshop"]["190.0"] = {}
    registry.update(tree)

    assert _clsid._get_photoshop_install_dirs() == [PS_BIN]


def test_get_photoshop_install_dirs_returns_nothing_when_photoshop_is_absent(registry):
    """An empty registry yields no install directory instead of raising."""

    assert _clsid._get_photoshop_install_dirs() == []


def test_iter_photoshop_local_servers_matches_only_photoshop_exe(registry):
    """Only CLSIDs whose local server is Photoshop.exe are considered."""
    registry.update(type_library_tree())
    clsids = registry["HKEY_CLASSES_ROOT"]["CLSID"]
    clsids["{OTHER}"] = {"LocalServer32": {None: os.path.join(PS_BIN, "NotPhotoshop.exe")}}
    clsids["{NO-SERVER}"] = {}

    assert list(_clsid._iter_photoshop_local_servers()) == [("{APP-CLSID}", PHOTOSHOP_EXE)]


"""
* End to end resolution against the fakes
"""


def test_type_libraries_are_sorted_richest_first(registry, load_type_lib):
    """The most complete type library wins, so a single class library cannot shadow it."""
    registry.update(type_library_tree())
    load_type_lib["libraries"][SCRIPTING_LIB] = FakeTypeLib(
        [
            coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID),
            coclass("SolidColor", SOLID_COLOR_CLSID),
            coclass("Application", APPLICATION_CLSID),
        ]
    )
    load_type_lib["libraries"][APPLICATION_LIB] = FakeTypeLib([coclass("Application", APPLICATION_CLSID)])

    libraries = _clsid._get_type_library_coclasses()

    assert [len(entry) for entry in libraries] == [3, 1]
    assert libraries[0]["ActionDescriptor"] == ACTION_DESCRIPTOR_CLSID


def test_richest_first_tie_break_keeps_both_libraries_usable(registry, load_type_lib):
    """Equally rich libraries are all kept, so resolution still finds every class."""
    other_lib = os.path.join(PS_BIN, "Other.8li")
    registry.update(type_library_tree())
    registry["HKEY_CLASSES_ROOT"]["TypeLib"]["{OTHER}"] = {"1.0": {"0": {"win64": {None: other_lib}}}}
    load_type_lib["libraries"][SCRIPTING_LIB] = FakeTypeLib([coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID)])
    load_type_lib["libraries"][other_lib] = FakeTypeLib([coclass("SolidColor", SOLID_COLOR_CLSID)])
    load_type_lib["libraries"][APPLICATION_LIB] = FakeTypeLib([coclass("Application", APPLICATION_CLSID)])

    libraries = _clsid._get_type_library_coclasses()

    # Three libraries, all equally rich, so no single one is preferred over the others.
    assert [len(entry) for entry in libraries] == [1, 1, 1]
    # They all stay usable regardless of the order the sort settled on.
    assert _clsid.resolve_photoshop_class_id("ActionDescriptor") == ACTION_DESCRIPTOR_CLSID
    assert _clsid.resolve_photoshop_class_id("SolidColor") == SOLID_COLOR_CLSID
    assert _clsid.resolve_photoshop_class_id("Application") == APPLICATION_CLSID


def test_resolve_photoshop_class_id_uses_the_type_library(registry, load_type_lib):
    """A class declared by the type library resolves without instantiating anything."""
    registry.update(type_library_tree())
    load_type_lib["libraries"][SCRIPTING_LIB] = FakeTypeLib([coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID)])
    load_type_lib["libraries"][APPLICATION_LIB] = FakeTypeLib([coclass("Application", APPLICATION_CLSID)])

    def fail(*args, **kwargs):
        raise AssertionError("the type library route must not instantiate automation objects")

    original = _clsid.CoCreateInstance
    _clsid.CoCreateInstance = fail
    try:
        assert _clsid.resolve_photoshop_class_id("ActionDescriptor") == ACTION_DESCRIPTOR_CLSID
        assert _clsid.resolve_photoshop_class_id("Application") == APPLICATION_CLSID
    finally:
        _clsid.CoCreateInstance = original


def test_resolve_photoshop_class_id_walks_the_whole_real_path(registry, load_type_lib):
    """Resolution drives the real registry walk, type library index and sorting."""
    registry.update(type_library_tree())
    load_type_lib["libraries"][SCRIPTING_LIB] = FakeTypeLib(
        [
            coclass("ActionDescriptor", ACTION_DESCRIPTOR_CLSID),
            coclass("SolidColor", SOLID_COLOR_CLSID),
        ]
    )
    load_type_lib["libraries"][APPLICATION_LIB] = FakeTypeLib([coclass("Application", APPLICATION_CLSID)])

    assert _clsid.resolve_photoshop_class_id("SolidColor") == SOLID_COLOR_CLSID
    assert _clsid.resolve_photoshop_class_id("Application") == APPLICATION_CLSID
    assert _clsid.resolve_photoshop_class_id("NotAPhotoshopClass") is None


def test_resolve_photoshop_class_id_survives_an_empty_registry(registry, load_type_lib):
    """With nothing registered the resolver returns None instead of raising."""
    assert _clsid.resolve_photoshop_class_id("ActionDescriptor") is None
    assert _clsid.resolve_photoshop_class_id("ActionDescriptor") is None


def test_probe_coclass_name_reports_the_name_from_the_automation_object(monkeypatch):
    """The IDispatch route reads the coclass name back off the live object."""
    created = []

    class FakeDispatch:
        """Stand-in for an automation object exposing ``GetTypeInfo``."""

        def GetTypeInfo(self, index, locale):
            return FakeTypeInfo("_ActionDescriptor", ACTION_DESCRIPTOR_CLSID)

    def fake_create(guid, interface=None, clsctx=None):
        created.append(str(guid))
        return FakeDispatch()

    monkeypatch.setattr(_clsid, "CoCreateInstance", fake_create)

    assert _clsid._probe_coclass_name(ACTION_DESCRIPTOR_CLSID) == "ActionDescriptor"
    assert created == [ACTION_DESCRIPTOR_CLSID]


def test_probe_coclass_name_returns_none_when_creation_fails(monkeypatch):
    """A CLSID that cannot be created contributes nothing instead of raising."""

    def fake_create(guid, interface=None, clsctx=None):
        raise OSError("server execution failed")

    monkeypatch.setattr(_clsid, "CoCreateInstance", fake_create)

    assert _clsid._probe_coclass_name(ACTION_DESCRIPTOR_CLSID) is None


def test_probe_coclass_name_returns_none_without_type_info(monkeypatch):
    """An automation object that exposes no type information is skipped."""

    class NoTypeInfo:
        """Stand-in for Photoshop's broken IDispatch implementations."""

        def GetTypeInfo(self, index, locale):
            raise OSError("no type info")

    monkeypatch.setattr(_clsid, "CoCreateInstance", lambda guid, interface=None, clsctx=None: NoTypeInfo())

    assert _clsid._probe_coclass_name(ACTION_DESCRIPTOR_CLSID) is None


"""
* Error reporting through the public failure path
"""


def test_resolution_error_reports_why_the_class_id_lookup_failed():
    """A resolver that raises is reported as a lookup failure, not a raw traceback."""

    class ActionDescriptor(_core.Photoshop):
        object_name = "ActionDescriptor"

    def explode(name):
        raise OSError("registry hive is corrupt")

    def never_created(name, dynamic=False):
        raise OSError("Invalid class string")

    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(_core, "CreateObject", never_created)
        patch.setattr(_core, "resolve_photoshop_class_id", explode)
        patch.setattr(_core.Photoshop, "_get_photoshop_versions", lambda self: [""])
        with pytest.raises(PhotoshopPythonAPIError) as error:
            ActionDescriptor()

    assert "Class ID lookup for 'ActionDescriptor' failed" in str(error.value)
