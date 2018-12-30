import os
import sys

from PySide import QtCore
from PySide import QtGui

from photoshop_python_api.application import Application


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

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
        app = Application()
        doc_ref = app.active_document
        os.system("start {}".format(os.path.dirname(doc_ref.path)))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec_())