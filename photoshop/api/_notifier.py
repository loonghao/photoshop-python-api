"""
The collection of Notifier objects in the document. Access through the
Application.notifiers collection property. For example:
var notRef = app.notifiers.add("OnClickGoButton", eventFile)
Notifiers must be enabled using the Application.notifiersEnabled property

"""
# Import built-in modules
from pathlib import Path

# Import local modules
from photoshop.api._core import Photoshop


class Notifier(Photoshop):
    def __init__(self, parent=None):
        super().__init__()
        self._flag_as_method(
            "remove",
        )

    @property
    def event(self):
        """The event identifier, a four-character code or a unique string."""
        return self.app.event

    @property
    def eventClass(self):
        """The class identifier, a four-character code or a unique string.

        When an event applies to multiple types of objects, use this
        propery to distinguish which object this notifier applies to.
        For example, the Make event ("Mk ") can apply to
        documents ("Dcmn"), channels ("Chnl") and other objects.

        """
        return self.app.eventClass

    @property
    def eventFile(self) -> Path:
        """The path to the file to execute when the event occurs and
        activates the notifier."""
        return Path(self.app.eventFile)

    def remove(self):
        """Deletes this object.

        You can also remove a Notifier object
        from the Script Events Manager
        drop-down list by deleting the file named
        Script Events Manager.xml from the
        Photoshop preferences folder. See Adobe
        Photoshop CC help for more information.

        """
        return self.app.remove()
