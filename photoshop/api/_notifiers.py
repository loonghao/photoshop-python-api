"""The collection of Notifier objects in the document.

Access through the Application.notifiers collection property.

Examples:
    Notifiers must be enabled using the Application.notifiersEnabled property.
    ```javascript
    var notRef = app.notifiers.add("OnClickGoButton", eventFile)
    ```

"""

# Import built-in modules
from typing import TYPE_CHECKING

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._notifier import Notifier
from photoshop.api.collections import CollectionOfRemovables


class Notifiers(CollectionOfRemovables[Notifier, int]):
    """The `notifiers` currently configured (in the Scripts Events Manager menu in the application)."""

    if TYPE_CHECKING:
        from photoshop.api.application import Application

        parent: Application

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(type=Notifier, parent=parent)
        self._flag_as_method("add")

    def add(
        self, event: str, event_file: str, event_class: str | None = None
    ) -> Notifier:
        self.parent.notifiersEnabled = True
        return Notifier(self.app.add(event, event_file, event_class))

    def removeAll(self) -> None:
        self.app.removeAll()
        self.parent.notifiersEnabled = False
