"""Defines an HSB color, used in the `SolidColor` object."""

# Import local modules
from photoshop.api._core import Photoshop


class HSBColor(Photoshop):
    """An HSB color specification."""

    object_name = "HSBColor"

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)

    @property
    def brightness(self) -> float:
        return self.app.brightness

    @brightness.setter
    def brightness(self, value: float) -> None:
        self.app.brightness = value

    @property
    def saturation(self) -> float:
        return self.app.saturation

    @saturation.setter
    def saturation(self, value: float) -> None:
        self.app.saturation = value

    @property
    def hue(self) -> float:
        """The hue value. Range: 0.0 to 360.0."""
        return self.app.hue

    @hue.setter
    def hue(self, value: float) -> None:
        self.app.hue = value
