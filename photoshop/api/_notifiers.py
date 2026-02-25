"""The collection of Notifier objects in the document.

Access through the Application.notifiers collection property.

Examples:
    Notifiers must be enabled using the Application.notifiersEnabled property.
    ```javascript
    var notRef = app.notifiers.add("OnClickGoButton", eventFile)
    ```

"""

from photoshop.api._core import Photoshop
from photoshop.api._notifier import Notifier
from photoshop.api.collections import CollectionOfRemovables


class Notifiers(CollectionOfRemovables[Notifier, int]):
    """The `notifiers` currently configured (in the Scripts Events Manager menu in the application)."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(type=Notifier, parent=parent)
        self._flag_as_method("add")

    def add(self, event: str, event_file: str, event_class: str | None = None) -> Notifier:
        self.app.application.notifiersEnabled = True
        return Notifier(self.app.add(event, event_file, event_class))

    def removeAll(self) -> None:
        self.app.removeAll()
        self.app.application.notifiersEnabled = False
