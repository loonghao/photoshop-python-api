""""""
import pytest

from photoshop.application import Application
from photoshop.solid_color import SolidColor
from photoshop.event_id import EventID


class TestApplication:
    """Test the solidColor."""

    # pylint: disable=attribute-defined-outside-init
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = Application()
        color = SolidColor()
        color.rgb.red = 255
        color.rgb.green = 111
        self.app.backgroundColor = color
        foreground_color = SolidColor()
        foreground_color.rgb.green = 0
        self.app.foregroundColor = foreground_color
        self.app.currentTool = "moveTool"
        self.app.notifiers.removeAll()

    def test_active_document(self, photoshop_app):
        assert photoshop_app.activeDocument.name == \
               self.app.activeDocument.name

    def test_get_background_color(self):
        assert self.app.backgroundColor.rgb.red == 255
        assert self.app.backgroundColor.rgb.green == 111
        assert self.app.backgroundColor.rgb.blue == 255
        assert self.app.backgroundColor.cmyk.yellow == 0
        assert self.app.backgroundColor.cmyk.magenta == 60
        assert self.app.backgroundColor.cmyk.cyan == 17
        assert self.app.backgroundColor.cmyk.black == 0
        assert self.app.backgroundColor.hsb.hue == 300
        assert self.app.backgroundColor.hsb.saturation == 56
        assert self.app.backgroundColor.hsb.brightness == 100
        assert self.app.backgroundColor.lab.A == 68
        assert self.app.backgroundColor.lab.B == -46
        assert self.app.backgroundColor.lab.L == 69

    def test_set_background_color(self, photoshop_app):
        self.app.backgroundColor.rgb.green = 0
        assert self.app.backgroundColor.rgb.green == \
               photoshop_app.backgroundColor.rgb.green

    def test_build(self):
        assert self.app.build == "21.0 (20191018.r.37 2019/10/18: 614690fb487)"

    def test_get_color_settings(self):
        assert self.app.colorSettings == "North America General Purpose 2"

    def test_set_color_settings(self, photoshop_app):
        color_settings = photoshop_app.colorSettings
        self.app.colorSettings = "Monitor Color"
        assert photoshop_app.colorSettings == "Monitor Color"
        self.app.colorSettings = color_settings

    def test_get_current_tool(self):
        assert self.app.currentTool == "moveTool"

    def test_set_current_tool(self):
        self.app.currentTool = "typeCreateOrEditTool"
        assert self.app.currentTool == "typeCreateOrEditTool"

    def test_displayDialogs(self):
        assert self.app.displayDialogs == "DisplayErrorDialogs"

    def test_documents(self):
        assert len(self.app.documents) == 0

    def test_get_fonts_count(self):
        assert self.app.fonts.length == 440
        assert len(self.app.fonts) == 440

    def test_get_foreground_color(self):
        assert self.app.foregroundColor.rgb.red == 255
        assert self.app.foregroundColor.rgb.green == 0
        assert self.app.foregroundColor.rgb.blue == 255
        assert self.app.foregroundColor.cmyk.yellow == 0
        assert self.app.foregroundColor.cmyk.magenta == 82
        assert self.app.foregroundColor.cmyk.cyan == 27
        assert self.app.foregroundColor.cmyk.black == 0
        assert self.app.foregroundColor.hsb.hue == 300
        assert self.app.foregroundColor.hsb.saturation == 100
        assert self.app.foregroundColor.hsb.brightness == 100
        assert self.app.foregroundColor.lab.A == 93
        assert self.app.foregroundColor.lab.B == -61
        assert self.app.foregroundColor.lab.L == 60

    def test_get_free_memory(self):
        assert self.app.freeMemory

    def test_get_locale(self):
        assert self.app.locale == "en_US"

    def test_macintoshFileTypes(self):
        assert "JPEG" in self.app.macintoshFileTypes

    def test_get_name(self):
        assert self.app.name == "Adobe Photoshop"

    def test_notifiers(self):
        assert self.app.notifiers.length == 0

    def test_add_notifiers(self, tmpdir):
        jsx_file = tmpdir.join("event.jsx")
        jsx_file.write('alert("Test Event")')
        self.app.notifiers.add(EventID.Open, str(jsx_file))
        assert self.app.notifiers.length == 1
        assert self.app.notifiers[0].EventID == EventID.Open

    def test_get_notifiersEnabled(self):
        assert not self.app.notifiersEnabled

    def test_get_application_path(self):
        assert self.app.path.as_posix() == \
               "C:/Program Files/Adobe/Adobe Photoshop 2020"

    def test_playbackDisplayDialogs(self):
        assert self.app.playbackDisplayDialogs == "DialogModes.NO"

    def test_playbackParameters(self):
        # assert self.app.playbackParameters
        print("Need test.")

    def test_preferences(self):
        assert self.app.preferences

    def test_get_preferencesFolder(self):
        assert self.app.preferencesFolder.is_dir()

    def test_get_recentFiles(self):
        assert self.app.recentFiles

    def test_scriptingBuildDate(self):
        assert self.app.scriptingBuildDate == "Apr 10 2020 00:39:52"

    def test_get_scriptingVersion(self):
        assert self.app.scriptingVersion == "21.1"

    def test_get_systemInformation(self):
        assert self.app.systemInformation

    def test_get_typename(self):
        assert self.app.typename == "Application"

    def test_get_version(self):
        assert self.app.version == "21.1.2"

    def test_windowsFileTypes(self):
        assert len(self.app.windowsFileTypes) >= 100

    def test_batch(self):
        self.app.batch()

    def test_beep(self):
        self.app.beep()

    def test_bringToFront(self):
        self.app.bringToFront()

    def test_changeProgressText(self):
        self.app.changeProgressText("test")

    def test_charIDToTypeID(self):
        assert self.app.charIDToTypeID("Type") == "1417244773"

    def test_compareWithNumbers(self):
        assert self.app.compareWithNumbers(20, 1)

    def test_do_action(self):
        self.app.doAction('Vignette (selection)', 'Default Actions')

    def test_featureEnabled(self):
        assert self.app.featureEnabled("photoshop/extended")

    # def test_getCustomOptions(self):
    #     assert self.app.getCustomOptions("Application")

    def test_isQuicktimeAvailable(self):
        assert self.app.isQuicktimeAvailable

    def test_openDialog(self):
        assert self.app.openDialog()

    def test_refresh(self):
        return self.app.refresh()

    def test_refreshFonts(self):
        return self.app.refreshFonts()

    def test_run_menu_item(self):
        assert self.app.runMenuItem(
            self.app.stringIDToTypeID("toggleProofColors"))

    def test_showColorPicker(self):
        assert self.app.showColorPicker()

    def test_stringIDToTypeID(self):
        assert self.app.stringIDToTypeID("toggleProofColors") == 2034

    def test_togglePalettes(self):
        assert self.app.togglePalettes()
        self.app.togglePalettes()

    def test_toolSupportsBrushes(self):
        assert self.app.toolSupportsBrushes("Tool")

    def test_toolSupportsBrushPresets(self):
        assert self.app.toolSupportsBrushPresets("Tool")

    def test_typeIDToCharID(self):
        assert self.app.typeIDToCharID("toggleProofColors")

    def test_typeIDToStringID(self):
        assert self.app.typeIDToStringID("toggleProofColors")

    def test_updateProgress(self):
        assert self.app.updateProgress("Done", "total")
