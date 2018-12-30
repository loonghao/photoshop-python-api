import sys

from PySide import QtCore
from PySide import QtGui

from photoshop_python_api import Documents


class Dialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.uiButton = QtGui.QPushButton('open', self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        grid = QtGui.QGridLayout()
        grid.addWidget(self.uiButton, 3, 2)
        main_widget = QtGui.QWidget()
        main_widget.setLayout(grid)
        self.setCentralWidget(main_widget)
        self.uiButton.clicked.connect(self.browse_clicked)

    # actions
    def browse_clicked(self):
        doc = Documents()
        # photoshop doesn't appear to have a "save as" dialog accessible via
        # python. so open our own Qt file dialog.
        file_dialog = QtGui.QFileDialog(
            caption="Save As",
            filter="Photoshop Documents (*.psd)"
        )
        file_dialog.setLabelText(QtGui.QFileDialog.Accept, "Save")
        file_dialog.setLabelText(QtGui.QFileDialog.Reject, "Cancel")
        file_dialog.setOption(QtGui.QFileDialog.DontResolveSymlinks)
        file_dialog.setOption(QtGui.QFileDialog.DontUseNativeDialog)
        if not file_dialog.exec_():
            return
        path = file_dialog.selectedFiles()[0]
        doc.open(path)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    a = Dialog()
    a.show()
    sys.exit(app.exec_())
