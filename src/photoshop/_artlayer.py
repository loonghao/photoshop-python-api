from photoshop._core import Photoshop
from photoshop.text_item import TextItem
from photoshop.enumerations import LayerKind


class ArtLayer(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    @property
    def name(self):
        return self.app.name

    @name.setter
    def name(self, text):
        self.app.name = text

    @property
    def fillOpacity(self):
        return self.app.fillOpacity

    @property
    def filterMaskDensity(self):
        return self.app.filterMaskDensity

    @property
    def filterMaskFeather(self):
        return self.app.filterMaskFeather

    @property
    def grouped(self):
        """bool: If true, the layer is grouped with the layer below."""
        return self.app.grouped

    @property
    def isBackgroundLayer(self):
        """bool: If true, the layer is a background layer."""
        return self.app.isBackgroundLayer

    @isBackgroundLayer.setter
    def isBackgroundLayer(self, value):
        self.app.isBackgroundLayer = value

    @property
    def kind(self):
        """Sets the layer kind (such as ‘text layer’) for an empty layer.

        Valid only when the layer is empty and when `isBackgroundLayer` is
        false. You can use the ‘kind ‘ property to make a background layer a
         normal layer; however, to make a layer a background layer, you must
         set `isBackgroundLayer` to true.

         """
        return LayerKind(self.app.kind)

    @kind.setter
    def kind(self, layer_type):
        """set the layer kind."""
        self.app.kind = layer_type

    @property
    def layerMaskDensity(self):
        """The density of the layer mask (between 0.0 and 100.0)."""
        return self.app.layerMaskDensity

    @layerMaskDensity.setter
    def layerMaskDensity(self, value):
        self.app.layerMaskDensity = value

    @property
    def layerMaskFeather(self):
        """The feather of the layer mask (between 0.0 and 250.0)."""
        return self.app.layerMaskFeather

    @layerMaskFeather.setter
    def layerMaskFeather(self, value):
        self.app.layerMaskFeather = value

    @property
    def parent(self):
        """The object’s container."""
        return self.app.parent

    @parent.setter
    def parent(self, value):
        """Set the object’s container."""
        self.app.parent = value

    @property
    def pixelsLocked(self):
        """If true, the pixels in the layer’s image cannot be edited."""
        return self.app.pixelsLocked

    @pixelsLocked.setter
    def pixelsLocked(self, value):
        self.app.pixelsLocked = value

    @property
    def positionLocked(self):
        """bool: If true, the pixels in the layer’s image cannot be moved
        within the layer."""
        return self.app.positionLocked

    @positionLocked.setter
    def positionLocked(self, value):
        self.app.positionLocked = value

    @property
    def textItem(self):
        """The text that is associated with the layer. Valid only when ‘kind’
        is text layer."""
        return TextItem(self.app.textItem)

    @textItem.setter
    def textItem(self, value):
        self.app.textItem = value

    @property
    def transparentPixelsLocked(self):
        return self.app.transparentPixelsLocked

    @transparentPixelsLocked.setter
    def transparentPixelsLocked(self, value):
        self.app.transparentPixelsLocked = value

    @property
    def vectorMaskDensity(self):
        return self.app.vectorMaskDensity

    @vectorMaskDensity.setter
    def vectorMaskDensity(self, value):
        self.app.vectorMaskDensity = value

    @property
    def length(self):
        return len(list(self.app))

    def link(self, artlayer):
        return self.adobe.activeDocument.activeLayer.link(artlayer)

    def add(self):
        return self.app.add()

    def adjustBrightnessContrast(self, brightness, contrast):
        """Adjusts the brightness and contrast.

        Args:
            brightness (int): The brightness amount. Range: -100 to 100.
            contrast (int): The contrast amount. Range: -100 to 100.

        """
        return self.app.adjustBrightnessContrast(brightness, contrast)

    def adjustColorBalance(
            self, shadows, midtones, highlights,
            preserveLuminosity,
    ):
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
        return self.app.adjustColorBalance(
            shadows, midtones, highlights,
            preserveLuminosity,
        )

    def adjustCurves(self, curveShape):
        """Adjusts the tonal range of the selected channel using up to fourteen
        points.



        Args:
            curveShape: The curve points. The number of points must be between
                2 and 14.

        Returns:

        """
        return self.app.adjustCurves(curveShape)

    def adjustLevels(
            self, inputRangeStart, inputRangeEnd, inputRangeGamma,
            outputRangeStart, outputRangeEnd,
    ):
        """Adjusts levels of the selected channels.

        Args:
            inputRangeStart:
            inputRangeEnd:
            inputRangeGamma:
            outputRangeStart:
            outputRangeEnd:

        Returns:

        """
        return self.app.adjustLevels(
            inputRangeStart, inputRangeEnd,
            inputRangeGamma,
            outputRangeStart, outputRangeEnd,
        )

    def applyAddNoise(self, amount, distribution, monochromatic):
        return self.app.applyAddNoise(amount, distribution, monochromatic)

    def applyDiffuseGlow(self, graininess, amount, clear_amount):
        """Applies the diffuse glow filter.

        Args:
            graininess: The amount of graininess. Range: 0 to 10.
            amount: The glow amount. Range: 0 to 20.
            clear_amount: The clear amount. Range: 0 to 20.

        Returns:

        """
        return self.app.applyDiffuseGlow(graininess, amount, clear_amount)

    def applyAverage(self):
        """Applies the average filter."""
        return self.app.applyAverage()

    def applyBlur(self):
        """Applies the blur filter."""
        return self.app.applyBlur()

    def applyBlurMore(self):
        """Applies the blur more filter."""
        return self.app.applyBlurMore()

    def applyClouds(self):
        """Applies the clouds filter."""
        return self.app.applyClouds()

    def applyCustomFilter(self, characteristics, scale, offset):
        """Applies the custom filter."""
        return self.app.applyCustomFilter(characteristics, scale, offset)

    def applyDeInterlace(self, eliminateFields, createFields):
        """Applies the de-interlace filter."""
        return self.app.applyDeInterlace(eliminateFields, createFields)

    def applyDespeckle(self):
        return self.app.applyDespeckle()

    def applyDifferenceClouds(self):
        """Applies the difference clouds filter."""
        return self.app.applyDifferenceClouds()

    def applyDisplace(
            self, horizontalScale, verticalScale, displacementType,
            undefinedAreas, displacementMapFile,
    ):
        """Applies the displace filter."""
        return self.app.applyDisplace(
            horizontalScale, verticalScale,
            displacementType,
            undefinedAreas, displacementMapFile,
        )

    def applyDustAndScratches(self, radius, threshold):
        """Applies the dust and scratches filter."""
        return self.app.applyDustAndScratches(radius, threshold)

    def applyGaussianBlur(self, radius):
        """Applies the gaussian blur filter."""
        return self.app.applyGaussianBlur(radius)

    def applyGlassEffect(
            self, distortion, smoothness, scaling, invert,
            texture,
            textureFile,
    ):
        return self.app.applyGlassEffect(
            distortion, smoothness, scaling,
            invert, texture,
            textureFile,
        )

    def applyHighPass(self, radius):
        """Applies the high pass filter."""
        return self.app.applyHighPass(radius)

    def applyLensBlur(
            self, source, focalDistance, invertDepthMap, shape,
            radius,
            bladeCurvature, rotation, brightness, threshold, amount,
            distribution, monochromatic,
    ):
        """Apply the lens blur filter."""
        return self.app.applyLensBlur(
            source, focalDistance, invertDepthMap,
            shape, radius,
            bladeCurvature, rotation, brightness,
            threshold, amount,
            distribution, monochromatic,
        )
