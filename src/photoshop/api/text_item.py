from ._core import Photoshop
from .solid_color import SolidColor
from .text_font import TextFont


class TextItem(Photoshop):
    object_name = "Application"

    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def alternateLigatures(self):
        return self.app.alternateLigatures

    @alternateLigatures.setter
    def alternateLigatures(self, value):
        self.app.alternateLigatures = value

    @property
    def antiAliasMethod(self):
        return self.app.antiAliasMethod

    @antiAliasMethod.setter
    def antiAliasMethod(self, value):
        self.app.antiAliasMethod = value

    @property
    def autoKerning(self):
        """The auto kerning option to use."""
        return self.app.autoKerning

    @autoKerning.setter
    def autoKerning(self, value):
        self.app.autoKerning = value

    @property
    def autoLeadingAmount(self):
        return self.app.autoLeadingAmount

    @autoLeadingAmount.setter
    def autoLeadingAmount(self, value):
        self.app.autoLeadingAmount = value

    @property
    def baselineShift(self):
        return self.app.baselineShift

    @baselineShift.setter
    def baselineShift(self, value):
        self.app.baselineShift = value

    @property
    def contents(self):
        """str: The actual text in the layer."""
        return self.app.contents

    @contents.setter
    def contents(self, text):
        """Set the actual text in the layer.

        Args:
            text: The actual text.

        """
        self.app.contents = text

    @property
    def desiredGlyphScaling(self):
        return self.app.desiredGlyphScaling

    @desiredGlyphScaling.setter
    def desiredGlyphScaling(self, value):
        self.app.desiredGlyphScaling = value

    @property
    def desiredLetterScaling(self):
        return self.app.desiredGlyphScaling

    @desiredLetterScaling.setter
    def desiredLetterScaling(self, value):
        self.app.desiredGlyphScaling = value

    @property
    def desiredWordScaling(self):
        return self.app.desiredWordScaling

    @desiredWordScaling.setter
    def desiredWordScaling(self, value):
        self.app.desiredWordScaling = value

    @property
    def direction(self):
        return self.app.direction

    @direction.setter
    def direction(self, value):
        self.app.direction = value

    @property
    def fauxBold(self):
        return self.app.fauxBold

    @fauxBold.setter
    def fauxBold(self, value):
        self.app.fauxBold = value

    @property
    def fauxItalic(self):
        return self.app.fauxItalic

    @fauxItalic.setter
    def fauxItalic(self, value):
        self.app.fauxItalic = value

    @property
    def firstLineIndent(self):
        return self.app.firstLineIndent

    @firstLineIndent.setter
    def firstLineIndent(self, value):
        self.app.firstLineIndent = value

    @property
    def font(self):
        """.text_font.TextFont: Current font."""
        return TextFont(self.app.font)

    @font.setter
    def font(self, text_font):
        self.app.font = text_font

    @property
    def hangingPunctuation(self):
        return self.app.hangingPunctuation

    @hangingPunctuation.setter
    def hangingPunctuation(self, value):
        self.app.hangingPunctuation = value

    @property
    def height(self):
        """int:The height of the bounding box for paragraph text."""
        return self.app.height

    @height.setter
    def height(self, value):
        self.app.height = value

    @property
    def horizontalScale(self):
        return self.app.horizontalScale

    @horizontalScale.setter
    def horizontalScale(self, value):
        self.app.horizontalScale = value

    @property
    def position(self):
        return self.app.position

    @position.setter
    def position(self, array):
        """The position of the origin for the text.

        The array must contain two values. Setting this property is basically
        equivalent to clicking the text tool at a point in the documents to
        create the point of origin for text.

        """
        self.app.position = array

    @property
    def size(self):
        return self.app.size

    @size.setter
    def size(self, value):
        self.app.size = value

    @property
    def color(self) -> SolidColor:
        return SolidColor(self.app.color)

    @color.setter
    def color(self, color_value):
        """The color of textItem."""
        self.app.color = color_value

    @property
    def capitalization(self):
        """Gets text case."""
        return self.app.capitalization

    @capitalization.setter
    def capitalization(self, value):
        """Sets text case."""
        self.app.capitalization = value

    @property
    def name(self):
        return self.app.name
