"""Tests for the CLSID fallback used when Photoshop publishes no versioned ProgID."""

# Import built-in modules
from unittest import mock

# Import third-party modules
import pytest

# Import local modules
from photoshop.api import _clsid
from photoshop.api import _core
from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError

ACTION_DESCRIPTOR_CLSID = "{B907FC78-A0EB-4DCA-BC8C-4E36718E1DC9}"


@pytest.fixture(autouse=True)
def _reset_clsid_cache():
    """Keep the process wide CLSID cache from leaking between tests."""
    _clsid.reset_cache()
    yield
    _clsid.reset_cache()


@pytest.fixture()
def action_descriptor_cls():
    """A Photoshop wrapper whose only version ID is the one found in the registry."""

    class ActionDescriptor(Photoshop):
        object_name = "ActionDescriptor"

    return ActionDescriptor


def _build(factory, create_object, class_id=None, versions=("",)):
    """Instantiate ``factory`` with ``CreateObject`` and the CLSID resolution patched."""
    with mock.patch.object(_core, "CreateObject", create_object), mock.patch.object(
        _core, "resolve_photoshop_class_id", lambda _: class_id
    ), mock.patch.object(Photoshop, "_get_photoshop_versions", lambda _: list(versions)):
        return factory()


def test_falls_back_to_clsid_when_every_progid_fails(action_descriptor_cls):
    """The object is created from its CLSID once every ProgID lookup has failed."""
    requested = []

    def create_object(name, dynamic=False):
        requested.append(name)
        if name.startswith("Photoshop."):
            raise OSError("Invalid class string")
        return f"created:{name}"

    instance = _build(action_descriptor_cls, create_object, class_id=ACTION_DESCRIPTOR_CLSID)

    assert instance.app == f"created:{ACTION_DESCRIPTOR_CLSID}"
    # Every ProgID is tried before falling back, and the fallback is dynamic.
    assert requested == ["Photoshop.ActionDescriptor", ACTION_DESCRIPTOR_CLSID]


def test_progid_is_preferred_over_clsid(action_descriptor_cls):
    """A working ProgID keeps winning, so existing behaviour is unchanged."""
    requested = []

    def create_object(name, dynamic=False):
        requested.append(name)
        return f"created:{name}"

    instance = _build(action_descriptor_cls, create_object, class_id=ACTION_DESCRIPTOR_CLSID)

    assert instance.app == "created:Photoshop.ActionDescriptor"
    assert requested == ["Photoshop.ActionDescriptor"]


def test_clsid_fallback_runs_for_every_version(action_descriptor_cls):
    """The fallback is only reached after all registry versions have been tried."""
    requested = []

    def create_object(name, dynamic=False):
        requested.append(name)
        if name.startswith("Photoshop."):
            raise OSError("Invalid class string")
        return f"created:{name}"

    _build(action_descriptor_cls, create_object, class_id=ACTION_DESCRIPTOR_CLSID, versions=("190", ""))

    assert requested == [
        "Photoshop.ActionDescriptor.190",
        "Photoshop.ActionDescriptor",
        ACTION_DESCRIPTOR_CLSID,
    ]


def test_error_lists_every_attempt_when_clsid_is_unavailable(action_descriptor_cls):
    """A failure reports each ProgID tried and that no CLSID was registered."""

    def create_object(name, dynamic=False):
        raise OSError("Invalid class string")

    with pytest.raises(PhotoshopPythonAPIError) as error:
        _build(action_descriptor_cls, create_object, class_id=None)

    message = str(error.value)
    assert "Photoshop.ActionDescriptor" in message
    assert "No CLSID is registered for 'ActionDescriptor'" in message
    assert "Please check if you have Photoshop installed correctly." in message


def test_error_reports_clsid_creation_failure(action_descriptor_cls):
    """A CLSID that resolves but cannot be created is reported too."""

    def create_object(name, dynamic=False):
        raise OSError("Server execution failed")

    with pytest.raises(PhotoshopPythonAPIError) as error:
        _build(action_descriptor_cls, create_object, class_id=ACTION_DESCRIPTOR_CLSID)

    assert f"CLSID '{ACTION_DESCRIPTOR_CLSID}' for 'ActionDescriptor' could not be created." in str(error.value)


def test_resolve_photoshop_class_id_prefers_the_type_library(action_descriptor_cls):
    """The type library is consulted before any automation object is instantiated."""
    with mock.patch.object(
        _clsid, "_get_type_library_coclasses", lambda: [{"ActionDescriptor": ACTION_DESCRIPTOR_CLSID}]
    ), mock.patch.object(_clsid, "_get_probed_coclasses") as probed:
        assert _clsid.resolve_photoshop_class_id("ActionDescriptor") == ACTION_DESCRIPTOR_CLSID
    probed.assert_not_called()


def test_resolve_photoshop_class_id_probes_when_type_library_misses():
    """A name missing from the type library is looked up on the automation server."""
    with mock.patch.object(_clsid, "_get_type_library_coclasses", lambda: [{"ActionList": "{X}"}]):
        with mock.patch.object(_clsid, "_get_probed_coclasses", lambda: {"ActionDescriptor": ACTION_DESCRIPTOR_CLSID}):
            assert _clsid.resolve_photoshop_class_id("ActionDescriptor") == ACTION_DESCRIPTOR_CLSID


def test_resolve_photoshop_class_id_caches_misses_once_photoshop_is_seen():
    """A miss is only cached when Photoshop was actually found, so starting it later works."""
    with mock.patch.object(_clsid, "_get_type_library_coclasses", return_value=[{"ActionList": "{X}"}]):
        with mock.patch.object(_clsid, "_get_probed_coclasses", return_value={}):
            # Photoshop was seen (the type library index is not empty), so the miss is cached.
            with mock.patch.object(_clsid, "_lookup_class_id", wraps=_clsid._lookup_class_id) as lookup:
                assert _clsid.resolve_photoshop_class_id("Nope") is None
                assert _clsid.resolve_photoshop_class_id("Nope") is None
            assert lookup.call_count == 1


def test_resolve_photoshop_class_id_retries_when_photoshop_was_never_seen():
    """A miss with no Photoshop in sight is retried rather than pinned for the process."""
    with mock.patch.object(_clsid, "_get_type_library_coclasses", return_value=[]):
        with mock.patch.object(_clsid, "_get_probed_coclasses", return_value={}):
            with mock.patch.object(_clsid, "_lookup_class_id", wraps=_clsid._lookup_class_id) as lookup:
                assert _clsid.resolve_photoshop_class_id("Nope") is None
                assert _clsid.resolve_photoshop_class_id("Nope") is None
            assert lookup.call_count == 2


def test_resolution_failure_reason_distinguishes_unknown_class_from_failed_probe():
    """The reported reason says whether the class is missing or Photoshop was unreachable."""
    with mock.patch.object(_clsid, "_get_type_library_coclasses", return_value=[]):
        with mock.patch.object(_clsid, "_get_probed_coclasses", return_value={"ActionList": "{X}"}):
            assert _clsid.resolve_photoshop_class_id("Nope") is None
            assert "declares 'Nope'" in _clsid.resolution_failure_reason("Nope")
    with mock.patch.object(_clsid, "_get_type_library_coclasses", return_value=[]):
        with mock.patch.object(_clsid, "_get_probed_coclasses", return_value={}):
            assert _clsid.resolve_photoshop_class_id("Unreachable") is None
            assert "could be inspected" in _clsid.resolution_failure_reason("Unreachable")


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("ActionDescriptor", "ActionDescriptor"),
        ("_ActionDescriptor", "ActionDescriptor"),
        ("_DCS1_SaveOptions", "DCS1_SaveOptions"),
        ("", ""),
    ],
)
def test_normalize_coclass_name(raw, expected):
    """Coclass names reported over IDispatch carry a leading underscore."""
    assert _clsid._normalize_coclass_name(raw) == expected
