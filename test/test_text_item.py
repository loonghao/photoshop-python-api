""""""
import pytest

from photoshop import Session


class TestTextItem:
    """Test the solidColor."""

    # pylint: disable=attribute-defined-outside-init
    @pytest.fixture(autouse=True)
    def setup(self, psd_file):
        """Setup for current test."""
        self.session = Session(
            file_path=psd_file("textitem"), action="open", auto_close=True
        )
        self.session.run_action()
        doc = self.session.active_document
        layer = doc.activeLayer
        self.text_item = layer.textItem()  # -> TextItem
        yield
        self.session.close()

    def test_alternateLigatures(self):
        assert self.text_item.alternateLigatures == 0

    def test_antiAliasMethod(self):
        assert self.text_item.antiAliasMethod == 3

    def test_autoKerning(self):
        assert self.text_item.autoKerning == 2

    def test_autoLeadingAmount(self):
        assert self.text_item.autoLeadingAmount == 120.00000476837158

    def test_set_autoLeadingAmount(self):
        self.text_item.autoLeadingAmount = 20
        assert self.text_item.autoLeadingAmount == 20.000000298023224

    def test_baseline_shift(self):
        assert self.text_item.baselineShift == 0.0
