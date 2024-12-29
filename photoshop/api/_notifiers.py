"""The collection of Notifier objects in the document.

Access through the Application.notifiers collection property.

Examples:
    Notifiers must be enabled using the Application.notifiersEnabled property.
    ```javascript
    var notRef = app.notifiers.add("OnClickGoButton", eventFile)
    ```
"""

# Import built-in modules
from __future__ import annotations

from typing import Any, Optional

# Import local modules
from photoshop.api._collection_base import CollectionBase
from photoshop.api._notifier import Notifier


class Notifiers(CollectionBase[Notifier]):
    """The collection of notifiers currently configured in Photoshop.
    
    This class represents all the notifiers configured in the Scripts Events Manager
    menu in Photoshop. It provides methods to:
    - Add new notifiers
    - Remove all notifiers
    - Access notifiers by index
    - Iterate over notifiers
    
    Note:
        Notifiers must be enabled using the Application.notifiersEnabled property.
    """

    def add(
        self,
        event: str,
        event_file: Optional[Any] = None,
        event_class: Optional[Any] = None,
    ) -> Notifier:
        """Add a new notifier.
        
        Args:
            event: The event to listen for
            event_file: The script file to execute when the event occurs
            event_class: The event class
            
        Returns:
            Notifier: The newly created notifier
        """
        self.parent.notifiersEnabled = True
        return self._wrap_item(self.app.add(event, event_file, event_class))

    def removeAll(self) -> None:
        """Remove all notifiers and disable notifications."""
        self.app.removeAll()
        self.parent.notifiersEnabled = False

    def _wrap_item(self, item: Any) -> Notifier:
        """Wrap a COM notifier object in a Notifier instance.
        
        Args:
            item: The COM notifier object to wrap
            
        Returns:
            Notifier: The wrapped notifier
        """
        return Notifier(item)
