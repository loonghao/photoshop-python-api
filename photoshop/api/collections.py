from typing import Generic, Iterator, Protocol, TypeVar

from comtypes import ArgumentError

from photoshop.api._core import Photoshop
from photoshop.api.errors import PhotoshopPythonAPIError


class _PhotoshopObject(Protocol):
    def __init__(self, parent: Photoshop | None = None) -> None: ...


class NamedPhotoshopObject(_PhotoshopObject, Protocol):
    @property
    def name(self) -> str: ...


T = TypeVar("T", bound=_PhotoshopObject)
N = TypeVar("N", bound=NamedPhotoshopObject)
G = TypeVar("G", bound=int | str)


class BaseCollection(Photoshop, Generic[T, G]):
    """A collection of Photoshop objects."""

    def __init__(self, type: type[T], parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self.type = type
        self._flag_as_method("item")

    @property
    def length(self) -> int:
        return len(list(self.app))

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, key: G) -> T:
        try:
            return self.type(self.app[key])
        except ArgumentError as exc:
            raise PhotoshopPythonAPIError(
                f"Couldn't find an item with key '{key}' in {type(self)}"
            ) from exc

    def __iter__(self) -> Iterator[T]:
        for item in self.app:
            yield self.type(item)

    def item(self, index: int) -> T:
        return self.type(self.app.item(index))

    def getByIndex(self, index: int) -> T:
        for idx, item in enumerate(self.app):
            if idx == index:
                return self.type(item)
        raise IndexError(f"Index {index} is out of range in {type(self)}")


class CollectionWithAdd(BaseCollection[T, G]):
    """Collection that has a add method that takes no arguments."""

    def __init__(self, type: type[T], parent: Photoshop | None = None) -> None:
        super().__init__(type, parent)
        self._flag_as_method("add")

    def add(self) -> T:
        return self.type(self.app.add())


class CollectionOfNamedObjects(BaseCollection[N, G]):
    """A collection of named Photoshop objects."""

    def getByName(self, name: str) -> N | None:
        """Get the first element in the collection with the provided name."""
        for item in self.app:
            if item.name == name:
                return self.type(item)
        return None


class CollectionOfRemovables(BaseCollection[T, G]):
    """A collection of removable Photoshop objects."""

    def __init__(self, type: type[T], parent: Photoshop | None = None) -> None:
        super().__init__(type, parent)
        self._flag_as_method("removeAll")

    def removeAll(self) -> None:
        """Deletes all items."""
        self.app.removeAll()
