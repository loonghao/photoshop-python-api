"""
The collection of Notifier objects in the document. Access through the
Application.notifiers collection property.

For example:
var notRef = app.notifiers.add("OnClickGoButton", eventFile)
Notifiers must be enabled using the Application.notifiersEnabled property.

"""

# Import built-in modules
from typing import Any
from typing import Optional

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._notifier import Notifier


class Notifiers(Photoshop):
    def __init__(self, parent: Optional[Any] = None):
        super().__init__(parent=parent)

    @property
    def _notifiers(self) -> list:
        return [n for n in self.app]

    def __len__(self):
        return self.length

    def __iter__(self):
        for app in self.app:
            yield app

    def __getitem__(self, item):
        return self._notifiers[item]

    @property
    def length(self):
        return len(self._notifiers)

    def add(
        self, event, event_file: Optional[Any] = None, event_class: Optional[Any] = None
    ) -> Notifier:
        self.parent.notifiersEnabled = True
        return Notifier(self.app.add(event, event_file, event_class))

    def removeAll(self):
        self.app.removeAll()
        self.parent.notifiersEnabled = False
