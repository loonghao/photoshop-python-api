""""""
import pytest

from photoshop import Session


class TestSolidColor:
    """Test the solidColor."""

    # pylint: disable=attribute-defined-outside-init
    @pytest.fixture(autouse=True)
    def setup(self):
        self.session = Session()
        self.solid_color = self.session.SolidColor()

    def test_cmyk_black(self):
        assert self.solid_color.cmyk.black == 0

    def test_cmyk_cyan(self):
        assert self.solid_color.cmyk.cyan == 0

    def test_cmyk_magenta(self):
        assert self.solid_color.cmyk.magenta == 0

    def test_cmyk_typename(self):
        assert self.solid_color.cmyk.typename == "CMYKColor"

    def test_yellow(self):
        assert self.solid_color.cmyk.yellow == 0

    def test_hsb_brightness(self):
        assert self.solid_color.hsb.brightness == 100

    def test_hsb_hue(self):
        assert self.solid_color.hsb.hue == 0

    def test_hsb_saturation(self):
        assert self.solid_color.hsb.saturation == 0

    def test_hsb_typename(self):
        assert self.solid_color.hsb.typename == "HSBColor"
