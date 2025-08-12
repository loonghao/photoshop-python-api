# https://theiviaxx.github.io/photoshop-docs/Photoshop/BatchOptions.html
# Import local modules
from os import PathLike
from pathlib import Path
from typing import Sequence

from photoshop.api._core import Photoshop
from photoshop.api.enumerations import BatchDestinationType, FileNamingType


class BatchOptions(Photoshop):
    object_name = "BatchOptions"

    @property
    def destination(self) -> BatchDestinationType:
        """The type of destination for the processed files."""
        return BatchDestinationType(self.app.destination)

    @destination.setter
    def destination(self, value: BatchDestinationType) -> None:
        self.app.destination = value

    @property
    def destinationFolder(self) -> Path | None:
        """The folder location for the processed files. Valid only when ‘destination’ == BatchDestinationType.FOLDER."""
        destination = self.app.destinationFolder
        if destination:
            return Path(self.app.destinationFolder)
        return None

    @destinationFolder.setter
    def destinationFolder(self, path: str | PathLike[str]) -> None:
        self.app.destinationFolder = str(path)

    @property
    def errorFile(self) -> Path | None:
        """The file in which to log errors encountered.
        To display errors on the screen and stop batch processing when errors occur, leave blank."""
        err_file = self.app.errorFile
        if err_file:
            return Path(self.app.errorFile)
        return None

    @errorFile.setter
    def errorFile(self, file_path: str | PathLike[str] | None) -> None:
        self.app.errorFile = str(file_path) if file_path else None

    @property
    def fileNaming(self) -> list[FileNamingType]:
        """A list of file naming options. Maximum: 6."""
        return [FileNamingType(file_naming) for file_naming in self.app.fileNaming]

    @fileNaming.setter
    def fileNaming(self, file_naming: Sequence[FileNamingType]) -> None:
        self.app.fileNaming = file_naming

    @property
    def macintoshCompatible(self) -> bool:
        """If true, the final file names are Macintosh compatible."""
        return self.app.macintoshCompatible

    @macintoshCompatible.setter
    def macintoshCompatible(self, value: bool) -> None:
        self.app.macintoshCompatible = value

    @property
    def overrideOpen(self) -> bool:
        """If true, overrides action open commands."""
        return self.app.overrideOpen

    @overrideOpen.setter
    def overrideOpen(self, value: bool) -> None:
        self.app.overrideOpen = value

    @property
    def overrideSave(self) -> bool:
        """If true, overrides save as action steps with the specified destination."""
        return self.app.overrideSave

    @overrideSave.setter
    def overrideSave(self, value: bool) -> None:
        self.app.overrideSave = value

    @property
    def startingSerial(self) -> int:
        """The starting serial number to use in naming files."""
        return self.app.startingSerial

    @startingSerial.setter
    def startingSerial(self, value: int) -> None:
        self.app.startingSerial = value

    @property
    def suppressOpen(self) -> bool:
        """If true, suppresses file open options dialogs."""
        return self.app.suppressOpen

    @suppressOpen.setter
    def suppressOpen(self, value: bool) -> None:
        self.app.suppressOpen = value

    @property
    def suppressProfile(self) -> bool:
        """If true, suppresses color profile warnings."""
        return self.app.suppressProfile

    @suppressProfile.setter
    def suppressProfile(self, value: bool) -> None:
        self.app.suppressProfile = value

    @property
    def unixCompatible(self) -> bool:
        """If true, the final file names are Unix compatible."""
        return self.app.unixCompatible

    @unixCompatible.setter
    def unixCompatible(self, value: bool) -> None:
        self.app.unixCompatible = value

    @property
    def windowsCompatible(self) -> bool:
        """If true, the final file names are Windows compatible."""
        return self.app.windowsCompatible

    @windowsCompatible.setter
    def windowsCompatible(self, value: bool) -> None:
        self.app.windowsCompatible = value
