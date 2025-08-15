# Import built-in modules
from typing import Sequence

# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api.enumerations import MeasurementRange


class MeasurementLog(Photoshop):
    """The log of measurements taken."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(parent=parent)
        self._flag_as_method(
            "exportMeasurements",
            "deleteMeasurements",
        )

    def exportMeasurements(
        self,
        file_path: str,
        range_: MeasurementRange | None = None,
        data_point: Sequence[str] | None = None,
    ):
        if data_point is None:
            data_point = []
        self.app.exportMeasurements(file_path, range_, data_point)

    def deleteMeasurements(self, range_: MeasurementRange) -> None:
        self.app.deleteMeasurements(range_)
