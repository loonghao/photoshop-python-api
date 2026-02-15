from os import PathLike

from photoshop.api._core import Photoshop
from photoshop.api._layer import Layer
from photoshop.api.enumerations import (
    CreateFields,
    DepthMaource,
    DisplacementMapType,
    ElementPlacement,
    EliminateFields,
    Geometry,
    LayerKind,
    LensType,
    NoiseDistribution,
    OffsetUndefinedAreas,
    RasterizeType,
    TextureType,
    UndefinedAreas,
)
from photoshop.api.text_item import TextItem


# pylint: disable=too-many-public-methods, too-many-arguments
class ArtLayer(Layer):
    """An object within a document that contains the visual elements of the image

    (equivalent to a layer in the Adobe Photoshop application).

    """

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "add",
            "adjustBrightnessContrast",
            "adjustColorBalance",
            "adjustCurves",
            "adjustLevels",
            "applyAddNoise",
            "applyAverage",
            "applyBlur",
            "applyBlurMore",
            "applyClouds",
            "applyCustomFilter",
            "applyDeInterlace",
            "applyDespeckle",
            "applyDifferenceClouds",
            "applyDiffuseGlow",
            "applyDisplace",
            "applyDustAndScratches",
            "applyGaussianBlur",
            "applyGlassEffect",
            "applyHighPass",
            "applyLensBlur",
            "applyLensFlare",
            "applyMaximum",
            "applyMedianNoise",
            "applyMinimum",
            "applyMotionBlur",
            "applyNTSC",
            "applyOceanRipple",
            "applyOffset",
            "applyPinch",
            "invert",
            "merge",
            "posterize",
            "rasterize",
            "convertToSmartObject",
        )

    @property
    def fillOpacity(self) -> float:
        """The interior opacity of the layer. Range: 0.0 to 100.0."""
        return self.app.fillOpacity

    @fillOpacity.setter
    def fillOpacity(self, value: float) -> None:
        """The interior opacity of the layer. Range: 0.0 to 100.0."""
        self.app.fillOpacity = value

    @property
    def filterMaskDensity(self) -> float:
        """The density of the filter mask (between 0.0 and 100.0)"""
        return self.app.filterMaskDensity

    @filterMaskDensity.setter
    def filterMaskDensity(self, value: float) -> None:
        self.app.filterMaskDensity = value

    @property
    def filterMaskFeather(self) -> float:
        """The feather of the filter mask (between 0.0 and 250.0)"""
        return self.app.filterMaskFeather

    @filterMaskFeather.setter
    def filterMaskFeather(self, value: float) -> None:
        self.app.filterMaskFeather = value

    @property
    def grouped(self) -> bool:
        """If true, the layer is grouped with the layer below."""
        return self.app.grouped

    @grouped.setter
    def grouped(self, value: bool) -> None:
        self.app.grouped = value

    @property
    def isBackgroundLayer(self) -> bool:
        """bool: If true, the layer is a background layer."""
        return self.app.isBackgroundLayer

    @isBackgroundLayer.setter
    def isBackgroundLayer(self, value: bool) -> None:
        self.app.isBackgroundLayer = value

    @property
    def kind(self) -> LayerKind:
        """Get the layer kind.

        Returns:
            LayerKind: The kind of this layer.
        """
        return LayerKind(self.app.kind)

    @kind.setter
    def kind(self, value: LayerKind) -> None:
        self.app.kind = value

    @property
    def layerMaskDensity(self) -> float:
        """The density of the layer mask (between 0.0 and 100.0)."""
        return self.app.layerMaskDensity

    @layerMaskDensity.setter
    def layerMaskDensity(self, value: float) -> None:
        self.app.layerMaskDensity = value

    @property
    def layerMaskFeather(self) -> float:
        """The feather of the layer mask (between 0.0 and 250.0)."""
        return self.app.layerMaskFeather

    @layerMaskFeather.setter
    def layerMaskFeather(self, value: float) -> None:
        self.app.layerMaskFeather = value

    @property
    def pixelsLocked(self) -> bool:
        """If true, the pixels in the layer’s image cannot be edited."""
        return self.app.pixelsLocked

    @pixelsLocked.setter
    def pixelsLocked(self, value: bool) -> None:
        self.app.pixelsLocked = value

    @property
    def positionLocked(self) -> bool:
        """bool: If true, the pixels in the layer’s image cannot be moved
        within the layer."""
        return self.app.positionLocked

    @positionLocked.setter
    def positionLocked(self, value: bool) -> None:
        self.app.positionLocked = value

    @property
    def textItem(self) -> TextItem:
        """The text that is associated with the layer. Valid only when ‘kind’
        is text layer.

        returns:
            TextItem:
        """
        return TextItem(self.app.textItem)

    @textItem.setter
    def textItem(self, value: TextItem) -> None:
        self.app.textItem = value.app

    @property
    def transparentPixelsLocked(self) -> bool:
        return self.app.transparentPixelsLocked

    @transparentPixelsLocked.setter
    def transparentPixelsLocked(self, value: bool) -> None:
        self.app.transparentPixelsLocked = value

    @property
    def vectorMaskDensity(self) -> float:
        """The density of the vector mask (between 0.0 and 100.0)"""
        return self.app.vectorMaskDensity

    @vectorMaskDensity.setter
    def vectorMaskDensity(self, value: float) -> None:
        self.app.vectorMaskDensity = value

    @property
    def vectorMaskFeather(self) -> float:
        """The feather of the vector mask (between 0.0 and 250.0)"""
        return self.app.vectorMaskFeather

    @vectorMaskFeather.setter
    def vectorMaskFeather(self, value: float) -> None:
        self.app.vectorMaskFeather = value

    def adjustBrightnessContrast(self, brightness: int, contrast: int) -> None:
        """Adjusts the brightness and contrast.

        Args:
            brightness (int): The brightness amount. Range: -100 to 100.
            contrast (int): The contrast amount. Range: -100 to 100.

        """
        self.app.adjustBrightnessContrast(brightness, contrast)

    def adjustColorBalance(
        self,
        shadows: tuple[int, int, int],
        midtones: tuple[int, int, int],
        highlights: tuple[int, int, int],
        preserveLuminosity: bool,
    ) -> None:
        """Adjusts the color balance of the layer’s component channels.

        Args:
            shadows: The adjustments for the shadows. The array must include
                     three values (in the range -100 to 100), which represent
                     cyan or red, magenta or green, and yellow or blue, when
                     the document mode is CMYK or RGB.
            midtones: The adjustments for the midtones. The array must include
                      three values (in the range -100 to 100), which represent
                      cyan or red, magenta or green, and yellow or blue, when
                      the document mode is CMYK or RGB.
            highlights: The adjustments for the highlights. The array must
                        include three values (in the range -100 to 100), which
                        represent cyan or red, magenta or green, and yellow or
                        blue, when the document mode is CMYK or RGB.
            preserveLuminosity: If true, luminosity is preserved.

        """
        self.app.adjustColorBalance(
            shadows,
            midtones,
            highlights,
            preserveLuminosity,
        )

    def adjustCurves(self, curveShape: list[tuple[float, float]]) -> None:
        """Adjusts the tonal range of the selected channel using up to fourteen
        points.



        Args:
            curveShape: The curve points. The number of points must be between
                2 and 14.

        Returns:

        """
        self.app.adjustCurves(curveShape)

    def adjustLevels(
        self,
        inputRangeStart: int,
        inputRangeEnd: int,
        inputRangeGamma: float,
        outputRangeStart: int,
        outputRangeEnd: int,
    ) -> None:
        """Adjusts levels of the selected channels.

        Args:
            inputRangeStart:
            inputRangeEnd:
            inputRangeGamma:
            outputRangeStart:
            outputRangeEnd:

        Returns:

        """
        self.app.adjustLevels(
            inputRangeStart,
            inputRangeEnd,
            inputRangeGamma,
            outputRangeStart,
            outputRangeEnd,
        )

    def applyAddNoise(self, amount: float, distribution: NoiseDistribution, monochromatic: bool) -> None:
        self.app.applyAddNoise(amount, distribution, monochromatic)

    def applyDiffuseGlow(self, graininess: int, amount: int, clear_amount: int) -> None:
        """Applies the diffuse glow filter.

        Args:
            graininess: The amount of graininess. Range: 0 to 10.
            amount: The glow amount. Range: 0 to 20.
            clear_amount: The clear amount. Range: 0 to 20.

        Returns:

        """
        self.app.applyDiffuseGlow(graininess, amount, clear_amount)

    def applyAverage(self) -> None:
        """Applies the average filter."""
        self.app.applyAverage()

    def applyBlur(self) -> None:
        """Applies the blur filter."""
        self.app.applyBlur()

    def applyBlurMore(self) -> None:
        """Applies the blur more filter."""
        self.app.applyBlurMore()

    def applyClouds(self) -> None:
        """Applies the clouds filter."""
        self.app.applyClouds()

    def applyCustomFilter(self, characteristics: list[int], scale: int, offset: int) -> None:
        """Applies the custom filter."""
        self.app.applyCustomFilter(characteristics, scale, offset)

    def applyDeInterlace(self, eliminateFields: EliminateFields, createFields: CreateFields) -> None:
        """Applies the de-interlace filter."""
        self.app.applyDeInterlace(eliminateFields, createFields)

    def applyDespeckle(self) -> None:
        self.app.applyDespeckle()

    def applyDifferenceClouds(self) -> None:
        """Applies the difference clouds filter."""
        self.app.applyDifferenceClouds()

    def applyDisplace(
        self,
        horizontalScale: int,
        verticalScale: int,
        displacementType: DisplacementMapType,
        undefinedAreas: UndefinedAreas,
        displacementMapFile: str | PathLike[str],
    ) -> None:
        """Applies the displace filter."""
        self.app.applyDisplace(
            horizontalScale,
            verticalScale,
            displacementType,
            undefinedAreas,
            str(displacementMapFile),
        )

    def applyDustAndScratches(self, radius: int, threshold: int) -> None:
        """Applies the dust and scratches filter."""
        self.app.applyDustAndScratches(radius, threshold)

    def applyGaussianBlur(self, radius: float) -> None:
        """Applies the gaussian blur filter."""
        self.app.applyGaussianBlur(radius)

    def applyGlassEffect(
        self,
        distortion: int,
        smoothness: int,
        scaling: int,
        invert: bool,
        texture: TextureType,
        textureFile: str | PathLike[str],
    ) -> None:
        self.app.applyGlassEffect(
            distortion,
            smoothness,
            scaling,
            invert,
            texture,
            str(textureFile),
        )

    def applyHighPass(self, radius: float) -> None:
        """Applies the high pass filter."""
        self.app.applyHighPass(radius)

    def applyLensBlur(
        self,
        source: DepthMaource,
        focalDistance: int,
        invertDepthMap: bool,
        shape: Geometry,
        radius: int,
        bladeCurvature: int,
        rotation: int,
        brightness: int,
        threshold: int,
        amount: int,
        distribution: NoiseDistribution,
        monochromatic: bool,
    ) -> None:
        """Apply the lens blur filter."""
        self.app.applyLensBlur(
            source,
            focalDistance,
            invertDepthMap,
            shape,
            radius,
            bladeCurvature,
            rotation,
            brightness,
            threshold,
            amount,
            distribution,
            monochromatic,
        )

    def applyLensFlare(self, brightness: int, flareCenter: tuple[float, float], lensType: LensType) -> None:
        self.app.applyLensFlare(brightness, flareCenter, lensType)

    def applyMaximum(self, radius: float) -> None:
        self.app.applyMaximum(radius)

    def applyMedianNoise(self, radius: float) -> None:
        self.app.applyMedianNoise(radius)

    def applyMinimum(self, radius: float) -> None:
        self.app.applyMinimum(radius)

    def applyMotionBlur(self, angle: int, radius: float) -> None:
        self.app.applyMotionBlur(angle, radius)

    def applyNTSC(self) -> None:
        self.app.applyNTSC()

    def applyOceanRipple(self, size: int, magnitude: int) -> None:
        self.app.applyOceanRipple(size, magnitude)

    def applyOffset(self, horizontal: int, vertical: int, undefinedAreas: OffsetUndefinedAreas) -> None:
        self.app.applyOffset(horizontal, vertical, undefinedAreas)

    def applyPinch(self, amount: int) -> None:
        self.app.applyPinch(amount)

    def rasterize(self, target: RasterizeType) -> None:
        self.app.rasterize(target)

    def posterize(self, levels: int) -> None:
        self.app.posterize(levels)

    def merge(self) -> "ArtLayer":
        return ArtLayer(self.app.merge())

    def invert(self) -> None:
        self.app.invert()

    def duplicate(
        self,
        relativeObject: "Layer | None" = None,
        insertionLocation: ElementPlacement | None = None,
    ) -> "ArtLayer":
        """Duplicates the layer.

        Args:
            relativeObject: Layer or LayerSet.
            insertionLocation: The location to insert the layer.

        Returns:
            ArtLayer: The duplicated layer.

        """
        return ArtLayer(self.app.duplicate(relativeObject.app if relativeObject else None, insertionLocation))

    def convertToSmartObject(self) -> "ArtLayer":
        """Converts the layer to a smart object.

        Returns:
            ArtLayer: The converted smart object layer.

        """
        # Convert layer to smart object using JavaScript
        js = """
        var idnewPlacedLayer = stringIDToTypeID("newPlacedLayer");
        executeAction(idnewPlacedLayer, undefined, DialogModes.NO);
        """
        self.eval_javascript(js)
        return self
