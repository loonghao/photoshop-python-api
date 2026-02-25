"""The Adobe Photoshop CC application object.

Which is the root of the object model and provides access to all other
objects. This object provides application-wide information,
such as application defaults and available fonts. It provides many important
methods, such as those for opening files and loading documents.

app = Application()

app.documents.add(800, 600, 72, "docRef")

"""

import os
import time

from _ctypes import COMError
from pathlib import Path
from typing import Any

from comtypes.client.dynamic import _Dispatch as FullyDynamicDispatch

from photoshop.api._artlayer import ArtLayer
from photoshop.api._core import Photoshop
from photoshop.api._document import Document
from photoshop.api._documents import Documents
from photoshop.api._layerSets import LayerSets
from photoshop.api._measurement_log import MeasurementLog
from photoshop.api._notifiers import Notifiers
from photoshop.api._preferences import Preferences
from photoshop.api._text_fonts import TextFonts
from photoshop.api.action_descriptor import ActionDescriptor
from photoshop.api.action_reference import ActionReference
from photoshop.api.batch_options import BatchOptions
from photoshop.api.enumerations import DialogModes, JavaScriptExecutionMode, PurgeTarget
from photoshop.api.errors import PhotoshopPythonAPIError
from photoshop.api.solid_color import SolidColor


class Application(Photoshop):
    """The Adobe Photoshop application object, which contains all other Adobe Photoshop objects.

    This is the root of the object model, and provides access to all other objects.
    To access the properties and methods, you can use the pre-defined global variable app.

    """

    def __init__(self, version: str | None = None, parent: "Photoshop | FullyDynamicDispatch | None" = None) -> None:
        super().__init__(ps_version=version, parent=parent)
        self._flag_as_method(
            "batch",
            "charIDToTypeID",
            "doAction",
            "doJavaScript",
            "eraseCustomOptions",
            "executeAction",
            "executeActionGet",
            "featureEnabled",
            "getCustomOptions",
            "isQuicktimeAvailable",
            "load",
            "open",
            "openDialog",
            "purge",
            "putCustomOptions",
            "refresh",
            "stringIDToTypeID",
            "toolSupportsBrushes",
            "toolSupportsPresets",
            "typeIDToCharID",
            "typeIDToStringID",
        )

    @property
    def activeLayer(self) -> ArtLayer:
        return ArtLayer(self.app.ArtLayer)

    @property
    def layerSets(self) -> LayerSets:
        return LayerSets(self.app.LayerSets)

    @property
    def activeDocument(self) -> Document:
        """The front-most documents.

        Setting this property is equivalent to clicking an
        open document in the Adobe Photoshop CC
        application to bring it to the front of the screen.

        """
        return Document(self.app.activeDocument)

    @activeDocument.setter
    def activeDocument(self, document: Document) -> None:
        self.app.activeDocument = document.app

    @property
    def backgroundColor(self) -> SolidColor:
        """The default background color and color style for documents."""
        return SolidColor(self.app.backgroundColor)

    @backgroundColor.setter
    def backgroundColor(self, color: SolidColor) -> None:
        """Sets the default background color and color style for documents.

        Args:
            color: The SolidColor instance.

        """
        self.app.backgroundColor = color.app

    @property
    def build(self) -> str:
        """str: The information about the application."""
        return self.app.build

    @property
    def colorSettings(self) -> str:
        """str: The name of the currently selected color settings profile
        (selected with Edit > Color Settings).

        """
        return self.app.colorSettings

    @colorSettings.setter
    def colorSettings(self, settings: str) -> None:
        """Sets the currently selected color settings profile.

        Args:
            settings: The name of a color settings profile to select.

        """
        try:
            self.doJavaScript(f'app.colorSettings="{settings}"')
        except COMError as e:
            raise PhotoshopPythonAPIError(f"Invalid color profile provided: '{settings}'") from e

    @property
    def currentTool(self) -> str:
        """str: The name of the current tool selected."""
        return self.app.currentTool

    @currentTool.setter
    def currentTool(self, tool_name: str) -> None:
        """Sets the currently selected tool.

        Args:
            tool_name: The name of a tool to select..

        """
        self.app.currentTool = tool_name

    @property
    def displayDialogs(self) -> DialogModes:
        """The dialog mode for the document, which indicates whether
        Photoshop displays dialogs when the script runs."""
        return DialogModes(self.app.displayDialogs)

    @displayDialogs.setter
    def displayDialogs(self, dialog_mode: DialogModes) -> None:
        """The dialog mode for the document, which indicates whether
        Photoshop displays dialogs when the script runs.
        """
        self.app.displayDialogs = dialog_mode

    @property
    def documents(self) -> Documents:
        """._documents.Documents: The Documents instance."""
        return Documents(self.app.documents)

    @property
    def fonts(self) -> TextFonts:
        return TextFonts(self.app.fonts)

    @property
    def foregroundColor(self) -> SolidColor:
        """Get default foreground color.

        Used to paint, fill, and stroke selections.

        Returns:
            The SolidColor instance.

        """
        return SolidColor(parent=self.app.foregroundColor)

    @foregroundColor.setter
    def foregroundColor(self, color: SolidColor) -> None:
        """Set the `foregroundColor`.

        Args:
            color: The SolidColor instance.

        """
        self.app.foregroundColor = color.app

    @property
    def freeMemory(self) -> float:
        """The amount of unused memory available to ."""
        return self.app.freeMemory

    @property
    def locale(self) -> str:
        """The language locale of the application."""
        return self.app.locale

    @property
    def macintoshFileTypes(self) -> tuple[str]:
        """A list of the image file types Photoshop can open."""
        return self.app.macintoshFileTypes

    @property
    def measurementLog(self) -> MeasurementLog:
        """The log of measurements taken."""
        return MeasurementLog(self.app.measurementLog)

    @property
    def name(self) -> str:
        return self.app.name

    @property
    def notifiers(self) -> Notifiers:
        """The notifiers currently configured (in the Scripts Events Manager
        menu in the application)."""
        return Notifiers(self.app.notifiers)

    @property
    def notifiersEnabled(self) -> bool:
        """bool: If true, notifiers are enabled."""
        return self.app.notifiersEnabled

    @notifiersEnabled.setter
    def notifiersEnabled(self, value: bool) -> None:
        self.app.notifiersEnabled = value

    @property
    def parent(self) -> object:
        """The object’s container."""
        return self.app.parent

    @property
    def path(self) -> Path:
        """str: The full path to the location of the Photoshop application."""
        return Path(self.app.path)

    @property
    def playbackDisplayDialogs(self) -> DialogModes:
        return self.doJavaScript("app.playbackDisplayDialogs")

    @property
    def playbackParameters(self) -> ActionDescriptor:
        """Stores and retrieves parameters used as part of a recorded action."""
        return self.app.playbackParameters

    @playbackParameters.setter
    def playbackParameters(self, value: ActionDescriptor) -> None:
        self.app.playbackParameters = value.app

    @property
    def preferences(self) -> Preferences:
        return Preferences(self.app.preferences)

    @property
    def preferencesFolder(self) -> Path:
        return Path(self.app.preferencesFolder)

    @property
    def recentFiles(self) -> list[Path]:
        return [Path(pth) for pth in self.app.recentFiles]

    @property
    def scriptingBuildDate(self) -> str:
        return self.app.scriptingBuildDate

    @property
    def scriptingVersion(self) -> str:
        return self.app.scriptingVersion

    @property
    def systemInformation(self) -> str:
        return self.app.systemInformation

    @property
    def version(self) -> str:
        return self.app.version

    @property
    def windowsFileTypes(self) -> tuple[str, ...]:
        return self.app.windowsFileTypes

    # Methods.
    def batch(
        self,
        files: list[str],
        actionName: str,
        actionSet: str,
        options: BatchOptions,
    ) -> None:
        """Runs the batch automation routine.

        Similar to the **File** > **Automate** > **Batch** command.

        """
        self.app.batch(files, actionName, actionSet, options.app)

    def beep(self) -> None:
        """Causes a "beep" sound."""
        self.eval_javascript("app.beep()")

    def bringToFront(self) -> None:
        self.eval_javascript("app.bringToFront()")

    def changeProgressText(self, text: str) -> None:
        """Changes the text that appears in the progress window."""
        self.eval_javascript(f"app.changeProgressText('{text}')")

    def charIDToTypeID(self, char_id: str) -> int:
        return self.app.charIDToTypeID(char_id)

    def doAction(self, action: str, action_from: str = "Default Actions") -> None:
        """Plays the specified action from the Actions palette."""
        self.app.doAction(action, action_from)

    def doForcedProgress(self, title: str, javascript: str) -> None:
        script = "app.doForcedProgress('{}', '{}')".format(
            title,
            javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgress(self, title: str, javascript: str) -> None:
        """Performs a task with a progress bar. Other progress APIs must be
        called periodically to update the progress bar and allow cancelling.

        Args:
            title (str): String to show in the progress window.
            javascript (str): JavaScriptString to execute.

        """
        script = "app.doProgress('{}', '{}')".format(
            title,
            javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressSegmentTask(self, segmentLength: int, done: int, total: int, javascript: str) -> None:
        script = "app.doProgressSegmentTask({}, {}, {}, '{}');".format(
            segmentLength,
            done,
            total,
            javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressSubTask(self, index: int, limit: int, javascript: str) -> None:
        script = "app.doProgressSubTask({}, {}, '{}');".format(
            index,
            limit,
            javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressTask(self, taskLength: float, javascript: str) -> None:
        """Sections off a portion of the unused progress bar for execution of
        a subtask. Returns false on cancel.

        """
        script = f"app.doProgressTask({taskLength}, '{javascript}');"
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def eraseCustomOptions(self, key: str) -> None:
        """Removes the specified user objects from the Photoshop registry."""
        self.app.eraseCustomOptions(key)

    def executeAction(
        self,
        event_id: int,
        descriptor: ActionDescriptor | None = None,
        display_dialogs: DialogModes = DialogModes.DisplayNoDialogs,
    ) -> ActionDescriptor:
        return ActionDescriptor(
            self.app.executeAction(event_id, descriptor.app if descriptor else None, display_dialogs)
        )

    def executeActionGet(self, reference: ActionReference) -> ActionDescriptor:
        return ActionDescriptor(self.app.executeActionGet(reference.app))

    def featureEnabled(self, name: str) -> bool:
        """Determines whether the feature

        specified by name is enabled.
        The following features are supported

        as values for name:
        "photoshop/extended"
        "photoshop/standard"
        "photoshop/trial

        """
        return self.app.featureEnabled(name)

    def getCustomOptions(self, key: str) -> ActionDescriptor:
        """Retrieves user objects in the Photoshop registry for the ID with
        value key."""
        return ActionDescriptor(self.app.getCustomOptions(key))

    def open(
        self,
        document_file_path: str | os.PathLike[str],
        document_type: str | None = None,
        as_smart_object: bool = False,
    ) -> Document:
        document = self.app.open(str(document_file_path), document_type, as_smart_object)
        if not as_smart_object:
            return Document(document)
        return document

    def load(self, document_file_path: str | os.PathLike[str]) -> Document:
        """Loads a supported Photoshop document."""
        self.app.load(str(document_file_path))
        return self.activeDocument

    def doJavaScript(
        self,
        javascript: str,
        Arguments: list[Any] | tuple[Any] | None = None,
        ExecutionMode: JavaScriptExecutionMode | None = None,
    ):
        return self.app.doJavaScript(javascript, Arguments, ExecutionMode)

    def isQuicktimeAvailable(self) -> bool:
        return self.app.isQuicktimeAvailable

    def openDialog(self) -> list[Path]:
        return [Path(pth) for pth in self.app.openDialog()]

    def purge(self, target: PurgeTarget) -> None:
        """Purges one or more caches.

        Args:
            target:
                1: Clears the undo cache.
                2: Clears history states from the History palette.
                3: Clears the clipboard data.
                4: Clears all caches

        """
        self.app.purge(target)

    def putCustomOptions(self, key: str, custom_object: ActionDescriptor, persistent: bool) -> None:
        self.app.putCustomOptions(key, custom_object.app, persistent)

    def refresh(self) -> None:
        """Pauses the script while the application refreshes.

        Use to slow down execution and show the results to the user as the
        script runs.
        Use carefully; your script runs much more slowly when using this
        method.
        """
        self.app.refresh()

    def refreshFonts(self) -> None:
        """Force the font list to get refreshed."""
        self.eval_javascript("app.refreshFonts();")

    def runMenuItem(self, menu_id: int) -> None:
        """Run a menu item given the menu ID."""
        self.eval_javascript(
            f"app.runMenuItem({menu_id})",
        )

    def showColorPicker(self) -> str:
        """Returns false if dialog is cancelled, true otherwise."""
        return self.eval_javascript("app.showColorPicker();")

    def stringIDToTypeID(self, string_id: str) -> int:
        return self.app.stringIDToTypeID(string_id)

    def togglePalettes(self) -> None:
        """Toggle palette visibility."""
        self.eval_javascript("app.togglePalettes()")

    def toolSupportsBrushes(self, tool: str) -> bool:
        result = self.eval_javascript(f'app.toolSupportsBrushes("{tool}")')
        return True if result == "true" else False

    def toolSupportsBrushPresets(self, tool: str) -> bool:
        result = self.eval_javascript(f'app.toolSupportsPresets("{tool}")')
        return True if result == "true" else False

    def typeIDToStringID(self, type_id: int) -> str:
        return self.app.typeIDToStringID(type_id)

    def typeIDToCharID(self, type_id: int) -> str:
        return self.app.typeIDToCharID(type_id)

    def updateProgress(self, done: int, total: int) -> None:
        self.eval_javascript(f"app.updateProgress({done}, {total})")
