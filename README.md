photoshop_python_api
====================
Supported Photoshop version:

    - cs6
    - cc2018
    - cc2017

install
-------
Clone from github.
```cmd
git clone https://github.com/loonghao/photoshop_python_api.git
```
Install requirements.
```cmd
pip install -r requirements.txt
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
options = PhotoshopSaveOptions
# save to psd
doc.save_as('D:\\tes3111t.psd', options.option)
```
Hello Word
----------
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
reference
=========
http://www.timcoolmode.com/images/small/PSD_Exporter.py

https://github.com/lohriialo/photoshop-scripting-python

https://evanmccall.wordpress.com/2015/03/09/how-to-develop-photoshop-tools-in-python/

https://techarttiki.blogspot.com/2008/08/photoshop-scripting-with-python.html

https://www.ps-scripts.com/