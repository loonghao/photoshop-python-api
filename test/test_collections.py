"""Automated coverage for the collection base classes.

These exercise the shared collection behaviour without a live Photoshop
instance: the COM object is replaced by a small fake that mimics the parts of
the automation interface the collections rely on.
"""

# Import future modules
from __future__ import annotations

# Import built-in modules
from typing import Any
from typing import Tuple
from typing import Union

# Import third-party modules
import pytest

from comtypes import ArgumentError

# Import local modules
from photoshop.api.collections import BaseCollection
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.collections import CollectionWithAdd
from photoshop.api.errors import PhotoshopPythonAPIError


class FakeItem:
    """Stand-in for a Photoshop wrapper object exposed through a collection.

    Accepting an existing instance mirrors the real API classes, which wrap a COM
    object and are also constructed from one; it keeps the wrapper idempotent so
    tests can assert on the wrapped value rather than on nesting depth.

    ``tag`` is an identity marker that is deliberately NOT part of equality. Two
    elements can share a name while remaining tellable apart, which is what lets
    the suite pin down "first match" rather than just "some match".
    """

    def __init__(self, name: FakeItem | str, tag: str | None = None) -> None:
        if isinstance(name, FakeItem):
            tag = tag if tag is not None else name.tag
            name = name.name
        self.name = name
        self.tag = tag

    def __eq__(self, other: object) -> bool:
        return isinstance(other, FakeItem) and other.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"FakeItem({self.name!r}, tag={self.tag!r})"


# An element is either a bare name or a (name, tag) pair, where the tag keeps
# same-named elements distinguishable.
# Tuple, not tuple: this alias is evaluated at import time, and PEP 585
# subscripting of builtins only works from Python 3.9 onwards.
ElementSpec = Union[str, Tuple[str, str]]


def _as_item(spec: ElementSpec) -> FakeItem:
    """Build a FakeItem from a bare name or a (name, tag) pair."""
    if isinstance(spec, tuple):
        return FakeItem(*spec)
    return FakeItem(spec)


class FakeCollectionApp:
    """Minimal stand-in for the COM collection behind a Photoshop collection."""

    def __init__(self, items: list[ElementSpec]) -> None:
        self._items = [_as_item(spec) for spec in items]
        self.remove_all_calls = 0
        self.add_calls = 0
        self.flagged_as_method: set[str] = set()

    def _FlagAsMethod(self, *names: str) -> None:
        self.flagged_as_method.update(names)

    def __iter__(self):
        # Yield the stored instances so callers observe element identity.
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, key: Any) -> FakeItem:
        if isinstance(key, str):
            for item in self._items:
                if item.name == key:
                    return item
            # Photoshop raises a COM ArgumentError for unknown names.
            raise ArgumentError()
        return self._items[key]

    def item(self, index: int) -> FakeItem:
        return self._items[index]

    def add(self) -> FakeItem:
        self.add_calls += 1
        item = FakeItem(f"added_{self.add_calls}")
        self._items.append(item)
        return item

    def removeAll(self) -> None:
        self.remove_all_calls += 1
        self._items.clear()


def _build(cls, items: list[ElementSpec]):
    """Instantiate a collection class and attach a fake COM collection to it.

    ``Photoshop.__init__`` is bypassed on purpose: it needs a live COM automation
    object. Only its postconditions are reproduced, so the collection logic under
    test still runs against the same attributes it would see in production.
    """
    collection = cls.__new__(cls)
    collection._app_id = ""
    collection._has_parent = False
    collection.adobe = None
    collection.app = FakeCollectionApp(items)
    collection._resolution_log = []
    collection.type = FakeItem
    return collection


def make_collection(items: list[ElementSpec]) -> BaseCollection[FakeItem, Any]:
    """Build a BaseCollection backed by a fake COM collection."""
    return _build(BaseCollection, items)


def make_named_collection(items: list[ElementSpec]) -> CollectionOfNamedObjects[FakeItem, Any]:
    return _build(CollectionOfNamedObjects, items)


def make_removable_collection(items: list[ElementSpec]) -> CollectionOfRemovables[FakeItem, Any]:
    return _build(CollectionOfRemovables, items)


def make_addable_collection(items: list[ElementSpec]) -> CollectionWithAdd[FakeItem, Any]:
    return _build(CollectionWithAdd, items)


class TestBaseCollection:
    """BaseCollection behaviour shared by every Photoshop collection."""

    def test_length_and_len_agree(self) -> None:
        collection = make_collection(["a", "b", "c"])
        assert collection.length == 3
        assert len(collection) == 3

    def test_iteration_wraps_every_item(self) -> None:
        collection = make_collection(["a", "b"])
        items = list(collection)
        assert [item.name for item in items] == ["a", "b"]
        assert all(isinstance(item, FakeItem) for item in items)

    def test_getitem_by_index(self) -> None:
        collection = make_collection(["a", "b"])
        assert collection[0].name == "a"
        assert collection[1].name == "b"

    def test_getitem_by_name(self) -> None:
        collection = make_collection(["a", "b"])
        assert collection["b"].name == "b"

    def test_item_returns_wrapped_object(self) -> None:
        collection = make_collection(["a", "b"])
        assert collection.item(1).name == "b"

    def test_get_by_index_returns_matching_position(self) -> None:
        collection = make_collection(["a", "b", "c"])
        assert collection.getByIndex(2).name == "c"

    def test_get_by_index_out_of_range_raises_index_error(self) -> None:
        collection = make_collection(["a"])
        with pytest.raises(IndexError):
            collection.getByIndex(5)

    def test_unknown_key_raises_photoshop_error(self) -> None:
        collection = make_collection(["a"])
        with pytest.raises(PhotoshopPythonAPIError):
            collection["missing"]

    def test_empty_collection(self) -> None:
        collection = make_collection([])
        assert len(collection) == 0
        assert list(collection) == []


class TestCollectionOfNamedObjects:
    """getByName semantics, including the documented None return."""

    def test_get_by_name_returns_match(self) -> None:
        collection = make_named_collection(["alpha", "beta"])
        found = collection.getByName("beta")
        assert found is not None
        assert found.name == "beta"

    def test_get_by_name_returns_none_when_absent(self) -> None:
        """getByName returns None instead of raising when nothing matches."""
        collection = make_named_collection(["alpha"])
        assert collection.getByName("missing") is None

    def test_get_by_name_on_empty_collection_returns_none(self) -> None:
        collection = make_named_collection([])
        assert collection.getByName("anything") is None

    def test_get_by_name_returns_first_match(self) -> None:
        """getByName returns the FIRST match, as its docstring promises.

        Both elements share the name, so only the tag tells them apart; without
        it a last-match regression would look identical to a first-match.
        """
        collection = make_named_collection([("dup", "first"), ("dup", "second")])
        found = collection.getByName("dup")
        assert found is not None
        assert found.tag == "first"

    def test_get_by_name_does_not_match_prefix(self) -> None:
        """getByName matches the whole name, so a prefix is not a hit."""
        collection = make_named_collection(["alpha"])
        assert collection.getByName("alph") is None

    def test_get_by_name_is_case_sensitive(self) -> None:
        """getByName compares names case-sensitively."""
        collection = make_named_collection(["alpha"])
        assert collection.getByName("ALPHA") is None


class TestCollectionOfRemovables:
    def test_remove_all_delegates_to_com(self) -> None:
        collection = make_removable_collection(["a", "b"])
        collection.removeAll()
        assert collection.app.remove_all_calls == 1
        assert len(collection) == 0


class TestCollectionWithAdd:
    def test_add_returns_wrapped_object(self) -> None:
        collection = make_addable_collection([])
        added = collection.add()
        assert isinstance(added, FakeItem)
        assert collection.app.add_calls == 1
        assert len(collection) == 1
