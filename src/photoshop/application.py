import os
import time
from photoshop._core import Photoshop
from photoshop.active_document import ActiveDocument
from photoshop.documents import Documents
from photoshop.preferences import Preferences
from photoshop.solid_color import SolidColor


class Application(Photoshop):

    def __init__(self, version=None):
        super().__init__(ps_version=version)

    @property
    def activeDocument(self):
        """The frontmost documents."""
        return ActiveDocument(self.app.activeDocument)

    @property
    def backgroundColor(self):
        return SolidColor(self.app.backgroundColor)

    @backgroundColor.setter
    def backgroundColor(self, color):
        self.app.backgroundColor = color

    @property
    def build(self):
        return self.app.build

    @property
    def colorSettings(self):
        return self.app.colorSettings

    @property
    def currentTool(self):
        return self.app.currentTool

    @currentTool.setter
    def currentTool(self, tool_name):
        self.app.currentTool = tool_name

    @property
    def displayDialogs(self):
        """The dialog mode for the document, which indicates whether or not
        Photoshop displays dialogs when the script runs."""
        return self.app.displayDialogs

    @displayDialogs.setter
    def displayDialogs(self, value):
        self.app.displayDialogs = value

    @property
    def documents(self):
        return Documents(self.app.documents)

    # TODO:
    @property
    def fonts(self):
        return self.app.fonts

    @property
    def foregroundColor(self):
        """The default foreground color (used to paint, fill,
        and stroke selections)."""
        return SolidColor(parent=self.app.foregroundColor)

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

    @property
    def parent(self):
        """The object’s container."""
        return self.app.parent

    @property
    def path(self):
        return self.app.path

    @property
    def playbackDisplayDialogs(self):
        return self.app.playbackDisplayDialogs

    @property
    def playbackParameters(self):
        return self.app.playbackParameters

    @property
    def preferences(self):
        return Preferences(self.app.preferences)

    @property
    def preferencesFolder(self):
        return self.app.preferencesFolder

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

    def batch(self):
        pass

    def beep(self):
        """Alerts the user."""
        pass

    def bringToFront(self):
        return self.eval_javascript('app.bringToFront();')

    def changeProgressText(self, text):
        """Changes the text that appears in the progress window."""
        self.eval_javascript(f"app.changeProgressText('{text}');")

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

    def eraseCustomOptions(self):
        pass

    def executeAction(self, eventID, descriptor, displayDialogs=2):
        return self.app.executeAction(eventID, descriptor, displayDialogs)

    @property
    def activeLayer(self):
        return self.app.ArtLayer

    @property
    def layerSets(self):
        return self.app.LayerSets

    def open(self, document_file_path):
        return ActiveDocument(self.app.open(document_file_path))

    def load(self, document_file_path):
        """Loads a support document."""
        self.app.load(document_file_path)
        return self.activeDocument

    def doJavaScript(self, javascript, Arguments=None, ExecutionMode=None):
        return self.app.doJavaScript(javascript, Arguments, ExecutionMode)

    def isQuicktimeAvailable(self):
        return self.app.IsQuicktimeAvailable()

    def purge(self, index):
        """

        Args:
            index:
                .e.g:
                    0: Clears all caches.
                    1: Clears the clipboard.
                    2: Deletes all history states from the History palette.
                    3: Clears the undo cache.

        Returns:

        """
        self.app.purge(index)

    def refreshFonts(self):
        """Force the font list to get refreshed."""
        return self.eval_javascript('app.refreshFonts();')

    def showColorPicker(self):
        return self.eval_javascript('app.showColorPicker();')

    @staticmethod
    def system(command):
        os.system(command)

    def stringIDToTypeID(self, string):
        return self.app.stringIDToTypeID(string)

    def typeIDToStringID(self, typeID):
        return self.app.typeIDToStringID(typeID)

    def typeIDToCharID(self, typeID):
        return self.app.typeIDToCharID(typeID)

    def updateProgress(self, done, total):
        self.eval_javascript(f'app.updateProgress({done}, {total})')
