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

from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions
from photoshop_python_api import SolidColor
from photoshop_python_api import LayerKind

app = Application()
doc = app.documents.add()
new_doc = doc.artLayers.add()
text_color = SolidColor()
text_color.rgb.red = 225
text_color.rgb.green = 255
text_color.rgb.blue = 0
new_text_layer = new_doc
new_text_layer.kind = LayerKind.BRIGHTNESSCONTRAST
new_text_layer.textItem.contents = "Hello, World!"
new_text_layer.textItem.position = [160, 167]
new_text_layer.textItem.size = 200
new_text_layer.textItem.color = text_color
options = JPEGSaveOptions()
options.quality = 10
# # save to jpg
jpg = 'd:/hello_world.jpg'
doc.saveAs(jpg, options, as_copy=True)
app.eval_javascript('alert("save to jpg: {}")'.format(jpg))
```

Create thumbnail
----------------


```python

from photoshop_python_api import Application
from photoshop_python_api import JPEGSaveOptions

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
