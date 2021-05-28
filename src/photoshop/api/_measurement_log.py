# Import local modules
from photoshop.api._core import Photoshop


class MeasurementLog(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def exportMeasurements(self, file_path: str, range_: int = None, data_point=None):
        if data_point is None:
            data_point = []
        self.app.exportMeasurements(file_path, range_, data_point)

    def deleteMeasurements(self, range_: int):
        self.app.deleteMeasurements(range_)
