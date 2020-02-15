photoshop_python_api
====================

https://photoshop-python-api.readthedocs.io
http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/photoshop/pdfs/photoshop-cc-javascript-ref-2015.pdf

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
python setup.py install
```

Hello World
-----------

```python

from photoshop_python_api.application import Application
from photoshop_python_api.save_options import JPEGSaveOptions
from photoshop_python_api.solid_color import SolidColor

app = Application()
doc = app.document
new_doc = doc.artLayers.add()
textColor = SolidColor()
textColor.RGB.Red = 225
textColor.RGB.Green = 0
textColor.RGB.Blue = 0
newTextLayer = new_doc
newTextLayer.Kind = 2
newTextLayer.TextItem.Contents = "Hello, World!"
newTextLayer.TextItem.Position = [160, 167]
newTextLayer.TextItem.Size = 36
newTextLayer.TextItem.Color = textColor.option
options = JPEGSaveOptions()
jpg = 'c:/hello_world.jpg'
doc.save_as(jpg, options, as_copy=True)
app.eval_javascript('alert("save to jpg: {}")'.format(jpg))
```

Create thumbnail
----------------


```python

from photoshop_python_api.application import Application
from photoshop_python_api.save_options import JPEGSaveOptions

app = Application()
active_document = app.activeDocument
orig_name = active_document.name
width_str = active_document.width
height_str = active_document.height
index = width_str / 1280
thumb_width = int(width_str / index)
thumb_height = int(height_str / index)
thumb_doc = active_document.duplicate('{}_tumb'.format(orig_name))
thumb_doc.resizeImage(thumb_width, thumb_height)
o = JPEGSaveOptions()
o.quality = 10
thumb_doc.saveAs('c:/thumb.jpg', o, as_copy=True)
thumb_doc.close()

```
