"""The Adobe Adobe Photoshop CC application object.

Which is the root of the object model and provides access to all other
objects. This object provides application-wide information,
such as application defaults and available fonts. It provides many important
methods, such as those for opening files and loading documents.

app = Application()

app.documents.add(800, 600, 72, "docRef")

"""

# Import built-in modules
import os
import time
from pathlib import Path

# Import local modules
from photoshop._core import Photoshop
from photoshop._document import Document
from photoshop._documents import Documents
from photoshop._preferences import Preferences
from photoshop.solid_color import SolidColor
from photoshop._text_fonts import TextFonts
from photoshop.enumerations import DialogModes


class Application(Photoshop):

    def __init__(self, version=None):
        super().__init__(ps_version=version)

    @property
    def activeDocument(self):
        """The frontmost documents.

        Setting this property is equivalent to clicking an
        open document in the Adobe Photoshop CC
        application to bring it to the front of the screen.

        """
        return Document(self.app.activeDocument)

    @activeDocument.setter
    def activeDocument(self, document):
        self.app.activeDocument = document

    @property
    def backgroundColor(self):
        """The default background color and color style for documents.

        Returns:
            photoshop.solid_color.SolidColor: The SolidColor instance.

        """
        return SolidColor(self.app.backgroundColor)

    @backgroundColor.setter
    def backgroundColor(self, color):
        """Sets the default background color and color style for documents.

        Args:
            color (photoshop.solid_color.SolidColor): The SolidColor instance.

        """
        self.app.backgroundColor = color

    @property
    def build(self):
        """str: The information about the application."""
        return self.app.build

    @property
    def colorSettings(self):
        """The name of the current color settings.

        as selected with Edit > Color Settings.

        """
        return self.app.colorSettings

    @colorSettings.setter
    def colorSettings(self, settings):
        """The name of the current color settings.

        Args:
            settings (str): The name of the current tool sel.

        """
        self.doJavaScript(f'app.colorSettings="{settings}"')

    @property
    def currentTool(self):
        """str: The name of the current tool sel."""
        return self.app.currentTool

    @currentTool.setter
    def currentTool(self, tool_name):
        """Sets the current tool for select.

        Args:
            tool_name (str): The name of the current tool sel.

        """
        self.app.currentTool = tool_name

    @property
    def displayDialogs(self):
        """The dialog mode for the document, which indicates whether or not
        Photoshop displays dialogs when the script runs."""
        return DialogModes(self.app.displayDialogs)

    @displayDialogs.setter
    def displayDialogs(self, dialog_mode):
        """The dialog mode for the document, which indicates whether or not
        Photoshop displays dialogs when the script runs.

        Args:
            dialog_mode (photoshop.enumerations.DialogModes): The dialog modes.

        """
        self.app.displayDialogs = dialog_mode

    @property
    def documents(self):
        """photoshop._documents.Documents: The Documents instance."""
        return Documents(self.app.documents)

    @property
    def fonts(self):
        return TextFonts(self.app.fonts)

    @property
    def foregroundColor(self):
        """Get default foreground color.

        Used to paint, fill, and stroke selections.

        Returns:
            photoshop.solid_color.SolidColor: The SolidColor instance.

        """
        return SolidColor(parent=self.app.foregroundColor)

    @foregroundColor.setter
    def foregroundColor(self, color):
        """Set the `foregroundColor`.

        Args:
            color (photoshop.solid_color.SolidColor): The SolidColor instance.

        """
        self.app.foregroundColor = color

    @property
    def freeMemory(self):
        """The amount of unused memory available to Photoshop."""
        return self.app.freeMemory

    @property
    def locale(self):
        """The language locale of the application."""
        return self.app.locale

    @property
    def macintoshFileTypes(self):
        """A list of the image file types Photoshop can open."""
        return self.app.macintoshFileTypes

    @property
    def measurementLog(self):
        """The log of measurements taken."""
        return self.app.measurementLog

    @property
    def name(self):
        return self.app.name

    @property
    def notifiers(self):
        """The notifiers currently configured (in the Scripts Events Manager
        menu in the application)."""
        return self.app.notifiers

    @property
    def notifiersEnabled(self):
        """If true, notifiers are enabled."""
        return self.app.notifiersEnabled

    @notifiersEnabled.setter
    def notifiersEnabled(self, value):
        self.app.notifiersEnabled = value

    @property
    def parent(self):
        """The object’s container."""
        return self.app.parent

    @property
    def path(self):
        """str: The full path to the location of the Photoshop application."""
        return Path(self.app.path)

    @property
    def playbackDisplayDialogs(self):
        return self.app.playbackDisplayDialogs

    @property
    def playbackParameters(self):
        return self.app.playbackParameters

    @playbackParameters.setter
    def playbackParameters(self, value):
        self.app.playbackParameters = value

    @property
    def preferences(self):
        return Preferences(self.app.preferences)

    @property
    def preferencesFolder(self):
        return Path(self.app.preferencesFolder)

    @property
    def recentFiles(self):
        return self.app.recentFiles

    @property
    def scriptingBuildDate(self):
        return self.app.scriptingBuildDate

    @property
    def scriptingVersion(self):
        return self.app.scriptingVersion

    @property
    def systemInformation(self):
        return self.app.systemInformation

    @property
    def typename(self):
        return self.app.typename

    @property
    def version(self):
        return self.app.version

    @property
    def windowsFileTypes(self):
        return self.app.windowsFileTypes

    # Methods.
    def batch(self, *args, **kwargs):
        """Runs the batch automation routine.

        Similar to the **File** > **Automate** > **Batch** command.

        """
        self.app.bath(*args, **kwargs)

    def beep(self):
        """Causes a "beep" sound."""
        self.eval_javascript("app.beep()")

    def bringToFront(self):
        return self.eval_javascript('app.bringToFront()')

    def changeProgressText(self, text):
        """Changes the text that appears in the progress window."""
        self.eval_javascript(f"app.changeProgressText('{text}')")

    def charIDToTypeID(self, char_id):
        return self.app.charIDToTypeID(char_id)

    def compareWithNumbers(self, first, second):
        return self.app.compareWithNumbers(first, second)

    def doAction(self, action, action_from):
        """Plays the specified action from the Actions palette."""
        return self.app.doAction(action, action_from)

    def doForcedProgress(self, title, javascript):
        script = "app.doForcedProgress('{}', '{}')".format(
            title,
            javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgress(self, title, javascript):
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

    def doProgressSegmentTask(self, segmentLength, done, total, javascript):
        script = "app.doProgressSegmentTask({}, {}, {}, '{}');".format(
            segmentLength, done, total, javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressSubTask(self, index, limit, javascript):
        script = "app.doProgressSubTask({}, {}, '{}');".format(
            index, limit, javascript,
        )
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def doProgressTask(self, index, javascript):
        """Sections off a portion of the unused progress bar for execution of
        a subtask. Returns false on cancel.

        """
        script = f"app.doProgressTask({index}, '{javascript}');"
        self.eval_javascript(script)
        # Ensure the script execute success.
        time.sleep(1)

    def eraseCustomOptions(self, key):
        self.app.eraseCustomOptions(key)

    def executeAction(self, eventID, descriptor, displayDialogs=2):
        return self.app.executeAction(eventID, descriptor, displayDialogs)

    @property
    def activeLayer(self):
        return self.app.ArtLayer

    @property
    def layerSets(self):
        return self.app.LayerSets

    def open(self, document_file_path, document_type=None,
             as_smart_object=False):
        document = self.app.open(document_file_path,
                                 document_type,
                                 as_smart_object)
        if not as_smart_object:
            return Document(document)
        return document

    def load(self, document_file_path):
        """Loads a support document."""
        self.app.load(document_file_path)
        return self.activeDocument

    def doJavaScript(self, javascript, Arguments=None, ExecutionMode=None):
        return self.app.doJavaScript(javascript, Arguments, ExecutionMode)

    def isQuicktimeAvailable(self):
        return self.eval_javascript('app.isQuicktimeAvailable()')

    def purge(self, target):
        """Purges one or more caches.

        Args:
            target:
                .e.g:
                    0: Clears all caches.
                    1: Clears the clipboard.
                    2: Deletes all history states from the History palette.
                    3: Clears the undo cache.

        Returns:

        """
        self.app.purge(target)

    def putCustomOptions(self, key, custom_object, persistent):
        self.app.putCustomOptions(key, custom_object, persistent)

    def refresh(self):
        """Pauses the script while the application refreshes.

        Ues to slow down execution and show the results to the user as the
        script runs.
        Use carefully; your script runs much more slowly when using this
        method.

        """
        self.app.refresh()

    def refreshFonts(self):
        """Force the font list to get refreshed."""
        return self.eval_javascript('app.refreshFonts();')

    def runMenuItem(self, menu_id):
        """Run a menu item given the menu ID."""
        return self.eval_javascript(f'app.runMenuItem({menu_id})', )

    def showColorPicker(self):
        """Returns false if dialog is cancelled, true otherwise."""
        return self.eval_javascript('app.showColorPicker();')

    def stringIDToTypeID(self, string_id):
        return self.app.stringIDToTypeID(string_id)

    def togglePalettes(self):
        """Toggle palette visibility."""
        self.app.togglePallettes()

    def toolSupportsBrushes(self, tool):
        return self.app.toolSupportsBrushes(tool)

    def toolSupportsBrushPresets(self, tool):
        return self.app.toolSupportsPresets(tool)

    @staticmethod
    def system(command):
        os.system(command)

    def typeIDToStringID(self, type_id):
        return self.app.typeIDToStringID(type_id)

    def typeIDToCharID(self, type_id):
        return self.app.typeIDToCharID(type_id)

    def updateProgress(self, done, total):
        self.eval_javascript(f'app.updateProgress({done}, {total})')
