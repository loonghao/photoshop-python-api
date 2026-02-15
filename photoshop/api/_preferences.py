# Import built-in modules
from os import PathLike
from pathlib import Path

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import (
    ColorPicker,
    EditLogItemsType,
    FontPreviewType,
    FontSize,
    GridLineStyle,
    GridSize,
    GuideLineStyle,
    OtherPaintingCursors,
    PaintingCursors,
    PointType,
    QueryStateType,
    ResampleMethod,
    SaveBehavior,
    TypeUnits,
    Units,
)


class Preferences(Photoshop):
    """The application preference settings."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def additionalPluginFolder(self) -> Path:
        """The path to an additional plug-in folder."""
        return Path(self.app.additionalPluginFolder)

    @additionalPluginFolder.setter
    def additionalPluginFolder(self, value: str | PathLike[str]) -> None:
        """The path to an additional plug-in folder."""
        self.app.additionalPluginFolder = str(value)

    @property
    def appendExtension(self) -> SaveBehavior:
        return SaveBehavior(self.app.appendExtension)

    @appendExtension.setter
    def appendExtension(self, value: SaveBehavior) -> None:
        self.app.appendExtension = value

    @property
    def askBeforeSavingLayeredTIFF(self) -> bool:
        return self.app.askBeforeSavingLayeredTIFF

    @askBeforeSavingLayeredTIFF.setter
    def askBeforeSavingLayeredTIFF(self, value: bool) -> None:
        self.app.askBeforeSavingLayeredTIFF = value

    @property
    def autoUpdateOpenDocuments(self) -> bool:
        """True to automatically update open documents."""
        return self.app.autoUpdateOpenDocuments

    @autoUpdateOpenDocuments.setter
    def autoUpdateOpenDocuments(self, boolean: bool) -> None:
        """True to automatically update open documents."""
        self.app.autoUpdateOpenDocuments = boolean

    @property
    def beepWhenDone(self) -> bool:
        """True to beep when a process."""
        return self.app.beepWhenDone

    @beepWhenDone.setter
    def beepWhenDone(self, boolean: bool) -> None:
        self.app.beepWhenDone = boolean

    @property
    def colorChannelsInColor(self) -> bool:
        """True to display component channels in the Channels palette in
        color."""
        return self.app.colorChannelsInColor

    @colorChannelsInColor.setter
    def colorChannelsInColor(self, value: bool) -> None:
        self.app.colorChannelsInColor = value

    @property
    def colorPicker(self) -> ColorPicker:
        """The preferred color selection tool."""
        return ColorPicker(self.app.colorPicker)

    @colorPicker.setter
    def colorPicker(self, value: ColorPicker) -> None:
        self.app.colorPicker = value

    @property
    def columnGutter(self) -> float:
        return self.app.columnGutter

    @columnGutter.setter
    def columnGutter(self, value: float) -> None:
        self.app.columnGutter = value

    @property
    def columnWidth(self) -> float:
        return self.app.columnWidth

    @columnWidth.setter
    def columnWidth(self, value: float) -> None:
        self.app.columnWidth = value

    @property
    def createFirstSnapshot(self) -> bool:
        """Automatically make the first snapshot when a new document is
        created."""
        return self.app.createFirstSnapshot

    @createFirstSnapshot.setter
    def createFirstSnapshot(self, boolean: bool) -> None:
        self.app.createFirstSnapshot = boolean

    @property
    def dynamicColorSliders(self) -> bool:
        return self.app.dynamicColorSliders

    @dynamicColorSliders.setter
    def dynamicColorSliders(self, boolean: bool) -> None:
        self.app.dynamicColorSliders = boolean

    @property
    def editLogItems(self) -> EditLogItemsType:
        """The preferred level of detail in the history log."""
        return EditLogItemsType(self.app.editLogItems)

    @editLogItems.setter
    def editLogItems(self, value: EditLogItemsType) -> None:
        """The preferred level of detail in the history log.

        Valid only when useHistoryLog = True

        """
        self.app.editLogItems = value

    @property
    def exportClipboard(self) -> bool:
        """Retain Photoshop contents on the clipboard after exit the app."""
        return self.app.exportClipboard

    @exportClipboard.setter
    def exportClipboard(self, boolean: bool) -> None:
        self.app.exportClipboard = boolean

    @property
    def fontPreviewSize(self) -> FontPreviewType:
        return FontPreviewType(self.app.fontPreviewSize)

    @fontPreviewSize.setter
    def fontPreviewSize(self, value: FontPreviewType) -> None:
        self.app.fontPreviewSize = value

    @property
    def fullSizePreview(self) -> bool:
        return self.app.fullSizePreview

    @fullSizePreview.setter
    def fullSizePreview(self, value: bool) -> None:
        self.app.fullSizePreview = value

    @property
    def gamutWarningOpacity(self) -> float:
        return self.app.gamutWarningOpacity

    @gamutWarningOpacity.setter
    def gamutWarningOpacity(self, value: float) -> None:
        self.app.gamutWarningOpacity = value

    @property
    def gridSize(self) -> GridSize:
        return GridSize(self.app.gridSize)

    @gridSize.setter
    def gridSize(self, value: GridSize) -> None:
        self.app.gridSize = value

    @property
    def gridStyle(self) -> GridLineStyle:
        return GridLineStyle(self.app.gridStyle)

    @gridStyle.setter
    def gridStyle(self, value: GridLineStyle) -> None:
        self.app.gridStyle = value

    @property
    def gridSubDivisions(self) -> int:
        return self.app.gridSubDivisions

    @gridSubDivisions.setter
    def gridSubDivisions(self, value: int) -> None:
        self.app.gridSubDivisions = value

    @property
    def guideStyle(self) -> GuideLineStyle:
        return GuideLineStyle(self.app.guideStyle)

    @guideStyle.setter
    def guideStyle(self, value: GuideLineStyle) -> None:
        self.app.guideStyle = value

    @property
    def iconPreview(self) -> bool:
        return self.app.iconPreview

    @iconPreview.setter
    def iconPreview(self, value: bool) -> None:
        self.app.iconPreview = value

    @property
    def imageCacheLevels(self) -> int:
        return self.app.imageCacheLevels

    @imageCacheLevels.setter
    def imageCacheLevels(self, value: int) -> None:
        self.app.imageCacheLevels = value

    @property
    def imagePreviews(self) -> SaveBehavior:
        return SaveBehavior(self.app.imagePreviews)

    @imagePreviews.setter
    def imagePreviews(self, value: SaveBehavior) -> None:
        self.app.imagePreviews = value

    @property
    def interpolation(self) -> ResampleMethod:
        return ResampleMethod(self.app.interpolation)

    @interpolation.setter
    def interpolation(self, value: ResampleMethod) -> None:
        self.app.interpolation = value

    @property
    def keyboardZoomResizesWindows(self) -> bool:
        return self.app.keyboardZoomResizesWindows

    @keyboardZoomResizesWindows.setter
    def keyboardZoomResizesWindows(self, value: bool) -> None:
        self.app.keyboardZoomResizesWindows = value

    @property
    def maximizeCompatibility(self) -> QueryStateType:
        return QueryStateType(self.app.maximizeCompatibility)

    @maximizeCompatibility.setter
    def maximizeCompatibility(self, value: QueryStateType) -> None:
        self.app.maximizeCompatibility = value

    @property
    def maxRAMuse(self) -> int:
        return self.app.maxRAMuse

    @maxRAMuse.setter
    def maxRAMuse(self, value: int) -> None:
        self.app.maxRAMuse = value

    @property
    def nonLinearHistory(self) -> bool:
        return self.app.nonLinearHistory

    @nonLinearHistory.setter
    def nonLinearHistory(self, value: bool) -> None:
        self.app.nonLinearHistory = value

    @property
    def numberofHistoryStates(self) -> int:
        return self.app.numberofHistoryStates

    @numberofHistoryStates.setter
    def numberofHistoryStates(self, value: int) -> None:
        self.app.numberofHistoryStates = value

    @property
    def otherCursors(self) -> OtherPaintingCursors:
        return OtherPaintingCursors(self.app.otherCursors)

    @otherCursors.setter
    def otherCursors(self, value: OtherPaintingCursors) -> None:
        self.app.otherCursors = value

    @property
    def paintingCursors(self) -> PaintingCursors:
        return PaintingCursors(self.app.paintingCursors)

    @paintingCursors.setter
    def paintingCursors(self, value: PaintingCursors) -> None:
        self.app.paintingCursors = value

    @property
    def pixelDoubling(self) -> bool:
        return self.app.pixelDoubling

    @pixelDoubling.setter
    def pixelDoubling(self, value: bool) -> None:
        self.app.pixelDoubling = value

    @property
    def pointSize(self) -> PointType:
        return PointType(self.app.pointSize)

    @pointSize.setter
    def pointSize(self, value: PointType) -> None:
        self.app.pointSize = value

    @property
    def recentFileListLength(self) -> int:
        return self.app.recentFileListLength

    @recentFileListLength.setter
    def recentFileListLength(self, value: int) -> None:
        self.app.recentFileListLength = value

    @property
    def rulerUnits(self) -> Units:
        return Units(self.app.rulerUnits)

    @rulerUnits.setter
    def rulerUnits(self, value: Units) -> None:
        self.app.rulerUnits = value

    @property
    def saveLogItems(self) -> Path:
        return Path(self.app.saveLogItems)

    @saveLogItems.setter
    def saveLogItems(self, value: str | PathLike[str]) -> None:
        self.app.saveLogItems = str(value)

    @property
    def savePaletteLocations(self) -> bool:
        return self.app.savePaletteLocations

    @savePaletteLocations.setter
    def savePaletteLocations(self, value: bool) -> None:
        self.app.savePaletteLocations = value

    @property
    def showAsianTextOptions(self) -> bool:
        return self.app.showAsianTextOptions

    @showAsianTextOptions.setter
    def showAsianTextOptions(self, value: bool) -> None:
        self.app.showAsianTextOptions = value

    @property
    def showEnglishFontNames(self) -> bool:
        return self.app.showEnglishFontNames

    @showEnglishFontNames.setter
    def showEnglishFontNames(self, value: bool) -> None:
        self.app.showEnglishFontNames = value

    @property
    def showSliceNumber(self) -> bool:
        return self.app.showSliceNumber

    @showSliceNumber.setter
    def showSliceNumber(self, value: bool) -> None:
        self.app.showSliceNumber = value

    @property
    def showToolTips(self) -> bool:
        return self.app.showToolTips

    @showToolTips.setter
    def showToolTips(self, value: bool) -> None:
        self.app.showToolTips = value

    @property
    def smartQuotes(self) -> bool:
        return self.app.smartQuotes

    @smartQuotes.setter
    def smartQuotes(self, value: bool) -> None:
        self.app.smartQuotes = value

    # textFontSize doesn't seem to be accessible via the COM API
    @property
    def textFontSize(self) -> FontSize:
        return FontSize(self.eval_javascript("app.preferences.textFontSize"))

    @textFontSize.setter
    def textFontSize(self, value: FontSize) -> None:
        self.eval_javascript(f"app.preferences.textFontSize = {value}")

    @property
    def typeUnits(self) -> TypeUnits:
        return TypeUnits(self.app.typeUnits)

    @typeUnits.setter
    def typeUnits(self, value: TypeUnits) -> None:
        self.app.typeUnits = value

    @property
    def useAdditionalPluginFolder(self) -> bool:
        return self.app.useAdditionalPluginFolder

    @useAdditionalPluginFolder.setter
    def useAdditionalPluginFolder(self, value: bool) -> None:
        self.app.useAdditionalPluginFolder = value

    @property
    def useHistoryLog(self) -> bool:
        return self.app.useHistoryLog

    @useHistoryLog.setter
    def useHistoryLog(self, value: bool) -> None:
        self.app.useHistoryLog = value

    @property
    def useLowerCaseExtension(self) -> bool:
        return self.app.useLowerCaseExtension

    @useLowerCaseExtension.setter
    def useLowerCaseExtension(self, value: bool) -> None:
        self.app.useLowerCaseExtension = value

    @property
    def useShiftKeyForToolSwitch(self) -> bool:
        return self.app.useShiftKeyForToolSwitch

    @useShiftKeyForToolSwitch.setter
    def useShiftKeyForToolSwitch(self, value: bool) -> None:
        self.app.useShiftKeyForToolSwitch = value

    @property
    def useVideoAlpha(self) -> bool:
        return self.app.useVideoAlpha

    @useVideoAlpha.setter
    def useVideoAlpha(self, value: bool) -> None:
        self.app.useVideoAlpha = value

    @property
    def windowsThumbnail(self) -> bool:
        return self.app.windowsThumbnail

    @windowsThumbnail.setter
    def windowsThumbnail(self, value: bool) -> None:
        self.app.windowsThumbnail = value
