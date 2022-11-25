# https://theiviaxx.github.io/photoshop-docs/Photoshop/BatchOptions.html
# Import local modules
from photoshop.api._core import Photoshop


class BatchOptions(Photoshop):
    object_name = "BatchOptions"

    def __init__(self):
        super().__init__()

    @property
    def destination(self):
        """The type of destination for the processed files."""
        return self.app.destination

    @destination.setter
    def destination(self, value):
        self.app.destination = value

    @property
    def destinationFolder(self):
        """The folder location for the processed files. Valid only when ‘destination’ = folder."""
        return self.app.destinationFolder

    @destinationFolder.setter
    def destinationFolder(self, path):
        self.app.destinationFolder = path

    @property
    def errorFile(self):
        """The file in which to log errors encountered.
        To display errors on the screen and stop batch processing when errors occur, leave blank."""
        return self.app.errorFile

    @errorFile.setter
    def errorFile(self, file_path):
        self.app.errorFile = file_path

    @property
    def fileNaming(self) -> list:
        """A list of file naming options. Maximum: 6."""
        return self.app.fileNaming

    @fileNaming.setter
    def fileNaming(self, file_naming: list):
        self.app.fileNaming = file_naming

    @property
    def macintoshCompatible(self) -> bool:
        """If true, the final file names are Macintosh compatible."""
        return self.app.macintoshCompatible

    @macintoshCompatible.setter
    def macintoshCompatible(self, value: bool):
        self.app.macintoshCompatible = value

    @property
    def overrideOpen(self) -> bool:
        """If true, overrides action open commands."""
        return self.app.overrideOpen

    @overrideOpen.setter
    def overrideOpen(self, value: bool):
        self.app.overrideOpen = value

    @property
    def overrideSave(self) -> bool:
        """If true, overrides save as action steps with the specified destination."""
        return self.app.overrideSave

    @overrideSave.setter
    def overrideSave(self, value: bool):
        self.app.overrideSave = value

    @property
    def startingSerial(self) -> int:
        """The starting serial number to use in naming files."""
        return self.app.startingSerial

    @startingSerial.setter
    def startingSerial(self, value: int):
        self.app.startingSerial = value

    @property
    def suppressOpen(self) -> bool:
        """If true, suppresses file open options dialogs."""
        return self.app.suppressOpen

    @suppressOpen.setter
    def suppressOpen(self, value: bool):
        self.app.suppressOpen = value

    @property
    def suppressProfile(self) -> bool:
        """If true, suppresses color profile warnings."""
        return self.app.suppressProfile

    @suppressProfile.setter
    def suppressProfile(self, value: bool):
        self.app.suppressProfile = value

    @property
    def unixCompatible(self) -> bool:
        """If true, the final file names are Unix compatible."""
        return self.app.unixCompatible

    @unixCompatible.setter
    def unixCompatible(self, value: bool):
        self.app.unixCompatible = value

    @property
    def windowsCompatible(self) -> bool:
        """If true, the final file names are Windows compatible."""
        return self.app.windowsCompatible

    @windowsCompatible.setter
    def windowsCompatible(self, value: bool):
        self.app.windowsCompatible = value
