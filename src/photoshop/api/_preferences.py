# Import built-in modules
from pathlib import Path

# Import local modules
from photoshop.api._core import Photoshop


class Preferences(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def additionalPluginFolder(self):
        """The path to an additional plug-in folder."""
        return Path(self.app.additionalPluginFolder)

    @property
    def appendExtension(self):
        return self.app.appendExtension

    @property
    def askBeforeSavingLayeredTIFF(self) -> bool:
        return self.app.askBeforeSavingLayeredTIFF

    @property
    def autoUpdateOpenDocuments(self) -> bool:
        """True to automatically update open documents."""
        return self.app.autoUpdateOpenDocuments

    @autoUpdateOpenDocuments.setter
    def autoUpdateOpenDocuments(self, boolean: bool):
        """True to automatically update open documents."""
        self.app.autoUpdateOpenDocuments = boolean

    @property
    def beepWhenDone(self) -> bool:
        """True to beep when a process."""
        return self.app.beepWhenDone

    @beepWhenDone.setter
    def beepWhenDone(self, boolean):
        self.app.beepWhenDone = boolean

    @property
    def colorChannelsInColor(self):
        """True to display component channels in the Channels palette in
        color."""
        return self.app.colorChannelsInColor

    @colorChannelsInColor.setter
    def colorChannelsInColor(self, value):
        self.app.colorChannelsInColor = value

    @property
    def colorPicker(self):
        """The preferred color selection tool."""
        return self.app.colorPicker

    @colorPicker.setter
    def colorPicker(self, value):
        self.app.colorPicker = value

    @property
    def columnGutter(self):
        return self.app.columnGutter

    @columnGutter.setter
    def columnGutter(self, value):
        self.app.columnGutter = value

    @property
    def columnWidth(self):
        return self.app.columnWidth

    @columnWidth.setter
    def columnWidth(self, value):
        self.app.columnWidth = value

    @property
    def createFirstSnapshot(self):
        """Automatically make the first snapshot when a new document is
        created."""
        return self.app.createFirstSnapshot

    @createFirstSnapshot.setter
    def createFirstSnapshot(self, boolean):
        self.app.createFirstSnapshot = boolean

    @property
    def dynamicColorSliders(self):
        return self.app.dynamicColorSliders

    @dynamicColorSliders.setter
    def dynamicColorSliders(self, boolean):
        self.app.dynamicColorSliders = boolean

    @property
    def editLogItems(self) -> bool:
        """The preferred level of detail in the history log."""
        return self.app.editLogItems

    @editLogItems.setter
    def editLogItems(self, boolean: bool):
        """The preferred level of detail in the history log.

        Valid only when useHistoryLog = True

        """
        self.app.editLogItems = boolean

    @property
    def exportClipboard(self):
        """Retain Photoshop contents on the clipboard after exit the app."""
        return self.app.exportClipboard

    @exportClipboard.setter
    def exportClipboard(self, boolean: bool):
        self.app.exportClipboard = boolean

    @property
    def fontPreviewSize(self):
        return self.app.fontPreviewSize

    @fontPreviewSize.setter
    def fontPreviewSize(self, value):
        self.app.fontPreviewSize = value

    @property
    def fullSizePreview(self):
        return self.app.fullSizePreview

    @fullSizePreview.setter
    def fullSizePreview(self, value):
        self.app.fullSizePreview = value

    @property
    def gamutWarningOpacity(self):
        return self.app.gamutWarningOpacity

    @property
    def rulerUnits(self):
        return self.app.rulerUnits

    @rulerUnits.setter
    def rulerUnits(self, value):
        self.app.rulerUnits = value
