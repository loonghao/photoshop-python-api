""""""
import pytest

from photoshop.application import Application
from photoshop.solid_color import SolidColor
from photoshop.enumerations import DialogModes


class TestApplication:
    """Test the solidColor."""

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
        assert self.app.fonts.length == 445
        assert len(self.app.fonts) == 445

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
