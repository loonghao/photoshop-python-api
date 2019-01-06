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


Hello World
-----------

```python
from photoshop_python_api import Application
from photoshop_python_api.save_options import JPEGSaveOptions
from photoshop_python_api.solid_color import SolidColor

app = Application()
doc = app.document
new_doc = doc.art_layers.add()
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
# # save to jpg
jpg = 'c:/hello_world.jpg'
doc.save_as(jpg, options, as_copy=True)
app.run_javascript('alert("save to jpg: {}")'.format(jpg))
```