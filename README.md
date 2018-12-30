photoshop_python_api
====================

https://theiviaxx.github.io/photoshop-docs/index.html

Has been tested and used Photoshop version:

    - cc2019
    - cc2018
    - cc2017
    - cs6

install
-------
Clone from github.
```cmd
git clone https://github.com/loonghao/photoshop_python_api.git
```
Install package.
```cmd
python setup.py installl
```
How to save a PSD
-----------------
```python
from photoshop_python_api.documents import Documents
from photoshop_python_api.save_options import PhotoshopSaveOptions
documents = Documents()
# create new documents
doc = documents.add()
# add new artlayers
doc.add_art_layers()
options = PhotoshopSaveOptions()
# save to psd
options.save_as('c:/test.psd')
```
Hello, World
------------
```python
from photoshop_python_api.documents import Documents

from photoshop_python_api.solid_color import SolidColor

doc = Documents()
doc_ref = doc.add()
textColor = SolidColor().option
textColor.RGB.Red = 225
textColor.RGB.Green = 0
textColor.RGB.Blue = 0
newTextLayer = doc_ref.add_art_layers()
psTextLayer = 2  # from enum PsLayerKind
newTextLayer.Kind = psTextLayer
newTextLayer.TextItem.Contents = "Hello, World!"
newTextLayer.TextItem.Position = [160, 167]
newTextLayer.TextItem.Size = 36
newTextLayer.TextItem.Color = textColor
```
Use PySide in Photoshop
-----------------------
```python
import os
import sys

from PySide import QtCore
from PySide import QtGui

from photoshop_python_api.documents import Documents


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
        doc = Documents()
        doc_ref = doc.active_document
        os.system("start {}".format(os.path.dirname(doc_ref.path)))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec_())

```

![alt icon](https://github.com/loonghao/photoshop_python_api/blob/master/images/pyside_open_folder.gif)
