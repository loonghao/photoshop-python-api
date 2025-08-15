# Import built-in modules
from typing import Sequence
from typing import TYPE_CHECKING

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.collections import CollectionOfRemovables
from photoshop.api.path_item import PathItem
from photoshop.api.sub_path_info import SubPathInfo


if TYPE_CHECKING:
    # Import local modules
    from photoshop.api._document import Document


class PathItems(
    CollectionOfRemovables[PathItem, int | str],
    CollectionOfNamedObjects[PathItem, int | str],
):
    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(PathItem, parent)
        self._flag_as_method("add")

    def add(self, name: str, entire_path: Sequence[SubPathInfo]) -> PathItem:
        return PathItem(self.app.add(name, entire_path))

    @property
    def parent(self) -> "Document":
        # Import local modules
        from photoshop.api._document import Document

        return Document(self.app.parent)
