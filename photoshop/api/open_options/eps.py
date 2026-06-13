# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import OpenDocumentMode


class EPSOpenOptions(Photoshop):
    """Options for saving a document in EPS format.

    using the `Document.saveAs()`

    """

    object_name = "EPSOpenOptions"

    def __init__(self) -> None:
        super().__init__()

    @property
    def antiAlias(self) -> bool:
        return self.app.antiAlias

    @antiAlias.setter
    def antiAlias(self, value: bool) -> None:
        self.app.antiAlias = value

    @property
    def constrainProportions(self) -> bool:
        return self.app.constrainProportions

    @constrainProportions.setter
    def constrainProportions(self, value: bool) -> None:
        self.app.constrainProportions = value

    @property
    def height(self) -> float:
        return self.app.height

    @height.setter
    def height(self, value: float) -> None:
        self.app.height = value

    @property
    def mode(self) -> OpenDocumentMode:
        return OpenDocumentMode(self.app.mode)

    @mode.setter
    def mode(self, value: OpenDocumentMode) -> None:
        self.app.mode = value

    @property
    def resolution(self) -> float:
        return self.app.resolution

    @resolution.setter
    def resolution(self, value: float) -> None:
        self.app.resolution = value

    @property
    def width(self) -> float:
        return self.app.width

    @width.setter
    def width(self, value: float) -> None:
        self.app.width = value
