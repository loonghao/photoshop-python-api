# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import AntiAlias
from photoshop.api.enumerations import AutoKernType
from photoshop.api.enumerations import Direction
from photoshop.api.enumerations import Justification
from photoshop.api.enumerations import Language
from photoshop.api.enumerations import StrikeThruType
from photoshop.api.enumerations import TextComposer
from photoshop.api.enumerations import TextType
from photoshop.api.solid_color import SolidColor


class TextItem(Photoshop):
    """The text that is associated with the layer. Valid only when ‘kind’ is text layer."""

    object_name = "Application"

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method(
            "convertToShape",
            "createPath",
        )

    @property
    def alternateLigatures(self):
        return self.app.alternateLigatures

    @alternateLigatures.setter
    def alternateLigatures(self, value):
        self.app.alternateLigatures = value

    @property
    def antiAliasMethod(self) -> AntiAlias:
        """The method of antialiasing to use."""
        return AntiAlias(self.app.antiAliasMethod)

    @antiAliasMethod.setter
    def antiAliasMethod(self, value):
        self.app.antiAliasMethod = value

    @property
    def autoKerning(self) -> AutoKernType:
        """The auto kerning option to use."""
        return AutoKernType(self.app.autoKerning)

    @autoKerning.setter
    def autoKerning(self, value):
        self.app.autoKerning = value

    @property
    def autoLeadingAmount(self):
        return self.app.autoLeadingAmount

    @autoLeadingAmount.setter
    def autoLeadingAmount(self, value):
        """The percentage to use for auto (default) leading (in points).

        Valid only when useAutoLeading = True.

        """
        self.app.useAutoLeading = True
        self.app.autoLeadingAmount = value

    @property
    def baselineShift(self):
        """The unit value to use in the baseline offset of text."""
        return self.app.baselineShift

    @baselineShift.setter
    def baselineShift(self, value):
        self.app.baselineShift = value

    @property
    def capitalization(self):
        """Gets text case."""
        return self.app.capitalization

    @capitalization.setter
    def capitalization(self, value):
        """Sets text case."""
        self.app.capitalization = value

    @property
    def color(self) -> SolidColor:
        """The text color."""
        return SolidColor(self.app.color)

    @color.setter
    def color(self, color_value):
        """The color of textItem."""
        self.app.color = color_value

    @property
    def contents(self) -> str:
        """The actual text in the layer."""
        return self.app.contents

    @contents.setter
    def contents(self, text: str):
        """Set the actual text in the layer.

        Args:
            text: The actual text.

        """
        self.app.contents = text

    @property
    def desiredGlyphScaling(self):
        """The desired amount by which to scale the horizontal size of the
        text letters. A percentage value; at 100, the width of characters is
        not scaled."""
        return self.app.desiredGlyphScaling

    @desiredGlyphScaling.setter
    def desiredGlyphScaling(self, value):
        self.app.desiredGlyphScaling = value

    @property
    def desiredLetterScaling(self):
        """The amount of space between letters .
        (at 0, no space is added between letters).
        Equivalent to Letter Spacing in the Justification
        dialog (Select Justification on the Paragraphs palette menu).
        Valid only when justification = Justification.CENTERJUSTIFIED,
                                                      FULLYJUSTIFIED,
                                                      LEFTJUSTIFIED, or
                                        Justification.RIGHTJUSTIFIED.
        When used, the minimumLetterScaling and
        maximumLetterScaling values are also required.

        """
        return self.app.desiredLetterScaling

    @desiredLetterScaling.setter
    def desiredLetterScaling(self, value):
        self.app.desiredGlyphScaling = value

    @property
    def desiredWordScaling(self):
        """
        The amount (percentage) of space
        between words (at 100, no additional space is added
        between words).
        Equivalent to Word Spacing in the Justification
        dialog (Select Justification on the Paragraphs
        palette menu).
        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the minimumWordScaling and
        maximumWordScaling values are also required

        """
        return self.app.desiredWordScaling

    @desiredWordScaling.setter
    def desiredWordScaling(self, value):
        self.app.desiredWordScaling = value

    @property
    def direction(self):
        """The text orientation."""
        return Direction(self.app.direction)

    @direction.setter
    def direction(self, value):
        self.app.direction = value

    @property
    def fauxBold(self):
        """True to use faux bold (default: false).

        Setting this to true is equivalent to selecting text and
        clicking Faux Bold in the Character palette.

        """
        return self.app.fauxBold

    @fauxBold.setter
    def fauxBold(self, value):
        self.app.fauxBold = value

    @property
    def fauxItalic(self):
        """True to use faux italic (default: false).

        Setting this to true is equivalent to selecting text and
        clicking Faux Italic in the Character palette.

        """
        return self.app.fauxItalic

    @fauxItalic.setter
    def fauxItalic(self, value):
        self.app.fauxItalic = value

    @property
    def firstLineIndent(self):
        """The amount (unit value) to indent the first line of paragraphs."""
        return self.app.firstLineIndent

    @firstLineIndent.setter
    def firstLineIndent(self, value):
        self.app.firstLineIndent = value

    @property
    def font(self) -> str:
        """str: postScriptName of the TextItem's font."""
        return self.app.font

    @font.setter
    def font(self, text_font: str):
        """Set the font of this TextItem.

        Args:
            text_font (str): Must provide the postScriptName of a valid font.
        """
        self.app.font = text_font

    @property
    def hangingPunctuation(self) -> bool:
        """bool: Whether to use Roman hanging punctuation."""
        return self.app.hangingPunctuation

    @hangingPunctuation.setter
    def hangingPunctuation(self, value: bool):
        self.app.hangingPunctuation = value

    @property
    def height(self):
        """int: The height of the bounding box for paragraph text."""
        return self.app.height

    @height.setter
    def height(self, value):
        self.app.height = value

    @property
    def horizontalScale(self) -> int:
        """Character scaling (horizontal) in proportion to verticalScale (a percentage value)."""
        return self.app.horizontalScale

    @horizontalScale.setter
    def horizontalScale(self, value: int):
        """Set the horizontalScale of this TextItem.

        Args:
            value: An integer between 0 and 1000.
        """
        self.app.horizontalScale = value

    @property
    def hyphenateAfterFirst(self):
        """The number of letters after which hyphenation in word wrap is allowed."""
        return self.app.hyphenateAfterFirst

    @hyphenateAfterFirst.setter
    def hyphenateAfterFirst(self, value):
        self.app.hyphenateAfterFirst = value

    @property
    def hyphenateBeforeLast(self):
        """The number of letters before which hyphenation in word wrap is allowed."""
        return self.app.hyphenateBeforeLast

    @hyphenateBeforeLast.setter
    def hyphenateBeforeLast(self, value):
        self.app.hyphenateBeforeLast = value

    @property
    def hyphenateCapitalWords(self):
        """True to allow hyphenation in word wrap of capitalized words"""
        return self.app.hyphenateCapitalWords

    @hyphenateCapitalWords.setter
    def hyphenateCapitalWords(self, value):
        self.app.hyphenateCapitalWords = value

    @property
    def hyphenateWordsLongerThan(self):
        """The minimum number of letters a word must have in order for
        hyphenation in word wrap to be allowed."""
        return self.app.hyphenateWordsLongerThan

    @hyphenateWordsLongerThan.setter
    def hyphenateWordsLongerThan(self, value):
        self.app.hyphenateWordsLongerThan = value

    @property
    def hyphenation(self):
        """True to use hyphenation in word wrap."""
        return self.app.hyphenation

    @hyphenation.setter
    def hyphenation(self, value):
        self.app.hyphenation = value

    @property
    def hyphenationZone(self):
        """The distance at the end of a line that will cause a word to break in
        unjustified type."""
        return self.app.hyphenationZone

    @hyphenationZone.setter
    def hyphenationZone(self, value):
        self.app.hyphenationZone = value

    @property
    def hyphenLimit(self):
        return self.app.hyphenLimit

    @hyphenLimit.setter
    def hyphenLimit(self, value):
        self.app.hyphenLimit = value

    @property
    def justification(self):
        """The paragraph justification."""
        return Justification(self.app.justification)

    @justification.setter
    def justification(self, value):
        self.app.justification = value

    @property
    def kind(self):
        return TextType(self.app.kind)

    @kind.setter
    def kind(self, kind_type):
        self.app.kind = kind_type

    @property
    def language(self):
        return Language(self.app.language)

    @language.setter
    def language(self, text):
        self.app.language = text

    @property
    def leading(self):
        return self.app.leading

    @leading.setter
    def leading(self, value):
        self.app.leading = value

    @property
    def leftIndent(self):
        """The amoun of space to indent text from the left."""
        return self.app.leftIndent

    @leftIndent.setter
    def leftIndent(self, value):
        self.app.leftIndent = value

    @property
    def ligatures(self):
        """True to use ligatures."""
        return self.app.ligatures

    @ligatures.setter
    def ligatures(self, value):
        self.app.ligatures = value

    @property
    def maximumGlyphScaling(self):
        """The maximum amount to scale the horizontal size of the text letters
        (a percentage value; at 100, the width of characters is not scaled).

        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the minimumGlyphScaling and
        desiredGlyphScaling values are also required.

        """
        return self.app.maximumGlyphScaling

    @maximumGlyphScaling.setter
    def maximumGlyphScaling(self, value):
        self.app.maximumGlyphScaling = value

    @property
    def maximumLetterScaling(self):
        """The maximum amount of space to allow between letters

        (at 0, no space is added between letters).
        Equivalent to Letter Spacing in the Justification
        dialog (Select Justification on the Paragraphs
        palette menu).
        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the minimumLetterScaling and
        desiredLetterScaling values are also required.

        """
        return self.app.maximumLetterScaling

    @maximumLetterScaling.setter
    def maximumLetterScaling(self, value):
        self.app.maximumLetterScaling = value

    @property
    def maximumWordScaling(self):
        return self.app.maximumWordScaling

    @maximumWordScaling.setter
    def maximumWordScaling(self, value):
        self.app.maximumWordScaling = value

    @property
    def minimumGlyphScaling(self):
        """The minimum amount to scale the horizontal size of the text letters
        (a percentage value; at 100, the width of characters is not scaled).

        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the maximumGlyphScaling and
        desiredGlyphScaling values are also required.

        """
        return self.app.minimumGlyphScaling

    @minimumGlyphScaling.setter
    def minimumGlyphScaling(self, value):
        self.app.minimumGlyphScaling = value

    @property
    def minimumLetterScaling(self):
        """The minimum amount of space to allow between letters

        (a percentage value; at 0, no space is removed between letters).

        Equivalent to Letter Spacing in the Justification
        dialog (Select Justification on the Paragraphs
        palette menu).
        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the maximumLetterScaling and
        desiredLetterScaling values are also required.

        """
        return self.app.minimumLetterScaling

    @minimumLetterScaling.setter
    def minimumLetterScaling(self, value):
        self.app.minimumLetterScaling = value

    @property
    def minimumWordScaling(self):
        """The minimum amount of space to allow between words

        (a percentage value; at 100, no additional space is removed between words).

        Equivalent to Word Spacing in the Justification
        dialog (Select Justification on the Paragraphs
        palette menu).
        Valid only when justification =
        Justification.CENTERJUSTIFIED,
        FULLYJUSTIFIED, LEFTJUSTIFIED, or
        Justification.RIGHTJUSTIFIED.
        When used, the maximumWordScaling and
        desiredWordScaling values are also required.

        """
        return self.app.minimumWordScaling

    @minimumWordScaling.setter
    def minimumWordScaling(self, value):
        self.app.minimumWordScaling = value

    @property
    def noBreak(self):
        """True to disallow line breaks in this text.

        Tip: When true for many consecutive characters, can
        prevent word wrap and thus may prevent some
        text from appearing on the screen.

        """
        return self.app.noBreak

    @noBreak.setter
    def noBreak(self, value):
        self.app.noBreak = value

    @property
    def oldStyle(self):
        return self.app.oldStyle

    @oldStyle.setter
    def oldStyle(self, value):
        self.app.oldStyle = value

    @property
    def parent(self):
        return self.app.parent

    @parent.setter
    def parent(self, value):
        self.app.parent = value

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
    def rightIndent(self):
        return self.app.rightIndent

    @rightIndent.setter
    def rightIndent(self, value):
        self.app.rightIndent = value

    @property
    def size(self):
        """The font size in UnitValue.

        NOTE: Type was points for CS3 and older.

        """
        return self.app.size

    @size.setter
    def size(self, value):
        self.app.size = value

    @property
    def spaceAfter(self):
        """The amount of space to use after each paragraph."""
        return self.app.spaceAfter

    @spaceAfter.setter
    def spaceAfter(self, value):
        self.app.spaceAfter = value

    @property
    def spaceBefore(self):
        return self.app.spaceBefore

    @spaceBefore.setter
    def spaceBefore(self, value):
        self.app.spaceBefore = value

    @property
    def strikeThru(self):
        """The text strike-through option to use."""
        return StrikeThruType(self.app.strikeThru)

    @strikeThru.setter
    def strikeThru(self, value):
        self.app.strikeThru = value

    @property
    def textComposer(self):
        return TextComposer(self.app.textComposer)

    @textComposer.setter
    def textComposer(self, value):
        self.app.textComposer = value

    @property
    def tracking(self):
        return self.app.tracking

    @tracking.setter
    def tracking(self, value):
        self.app.tracking = value

    @property
    def underline(self):
        """The text underlining options."""
        return self.app.underline

    @underline.setter
    def underline(self, value):
        self.app.underline = value

    @property
    def useAutoLeading(self):
        return self.app.useAutoLeading

    @useAutoLeading.setter
    def useAutoLeading(self, value):
        self.app.useAutoLeading = value

    @property
    def verticalScale(self):
        return self.app.verticalScale

    @verticalScale.setter
    def verticalScale(self, value):
        self.app.verticalScale = value

    @property
    def warpBend(self):
        """The warp bend percentage."""
        return self.app.warpBend

    @warpBend.setter
    def warpBend(self, value):
        self.app.warpBend = value

    @property
    def warpDirection(self) -> Direction:
        """The warp direction."""
        return Direction(self.app.warpDirection)

    @warpDirection.setter
    def warpDirection(self, value):
        self.app.warpDirection = value

    @property
    def warpHorizontalDistortion(self):
        return self.app.warpHorizontalDistortion

    @warpHorizontalDistortion.setter
    def warpHorizontalDistortion(self, value):
        self.app.warpHorizontalDistortion = value

    @property
    def warpStyle(self):
        """The style of warp to use."""
        return self.app.warpStyle

    @warpStyle.setter
    def warpStyle(self, value):
        self.app.warpStyle = value

    @property
    def warpVerticalDistortion(self):
        return self.app.warpVerticalDistortion

    @warpVerticalDistortion.setter
    def warpVerticalDistortion(self, value):
        self.app.warpVerticalDistortion = value

    @property
    def width(self):
        """The width of the bounding box for

        paragraph text.
        Valid only when kind = TextType.PARAGRAPHTEXT.

        """
        return self.app.width

    @width.setter
    def width(self, value: float):
        """The width of the bounding box for

        paragraph text.
        Valid only when kind = TextType.PARAGRAPHTEXT.

        """
        self.app.width = value

    def convertToShape(self):
        """Converts the text item and its containing layer to a fill layer with the
        text changed to a clipping path."""
        return self.app.convertToShape()

    def createPath(self):
        """Creates a clipping path from the outlines of the actual text items

        (such as letters or words).

        """
        return self.app.createPath()
