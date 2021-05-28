""""""
# Import third-party modules
import pytest

# Import local modules
from photoshop import Session
from photoshop.api.enumerations import TextType


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
        # self.session.close()

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

    def test_fauxBold(self):
        assert not self.text_item.fauxBold

    def test_set_fauxBold(self):
        assert not self.text_item.fauxBold
        self.text_item.fauxBold = True
        assert self.text_item.fauxBold

    def test_fauxItalic(self):
        assert not self.text_item.fauxItalic

    def test_firstLineIndent(self):
        assert self.text_item.firstLineIndent == 0.0

    def test_get_font(self):
        assert self.text_item.font == "ArialMT"

    def test_set_font(self):
        self.text_item.font = "AdobeThai-Regular"
        assert self.text_item.font == "AdobeThai-Regular"

    def test_hangingPunctuation(self):
        assert not self.text_item.hangingPunctuation

    def test_hyphenateAfterFirst(self):
        assert self.text_item.hyphenateAfterFirst == 2

    def test_justification(self):
        assert self.text_item.justification == 1

    def test_set_justification(self):
        self.text_item.justification = 2
        assert self.text_item.justification == 2

    def test_kind(self):
        assert self.text_item.kind == 1

    def test_set_kind(self):
        self.text_item.kind = TextType.ParagraphText
        assert self.text_item.kind == 2
        assert self.text_item.kind == TextType.ParagraphText

    def test_noBreak(self):
        assert not self.text_item.noBreak

    def test_position(self):
        assert self.text_item.position == (5.0, 57.0)

    def test_size(self):
        assert self.text_item.size == 18.0

    def test_change_size(self):
        self.text_item.size = 20
        assert self.text_item.size == 20.0
