photoshop_python_api
====================
[![PyPI version](https://badge.fury.io/py/photoshop-python-api.svg)](https://badge.fury.io/py/photoshop-python-api)

The API for using COM (Component Object Model) objects interfaces of Photoshop.

https://photoshop-python-api.readthedocs.io

![logo](https://i.imgur.com/9NpsSvd.png)

Has been tested and used Photoshop version:

    - 2020
    - cc2019
    - cc2018
    - cc2017
    - cs6

Installing
----------
You can install via pip.

```cmd
pip install photoshop_python_api
```
or through clone from Github.
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

import photoshop as ps
app = ps.Application()
doc = app.documents.add()
new_doc = doc.artLayers.add()
text_color = ps.SolidColor()
text_color.rgb.green = 255
new_text_layer = new_doc
new_text_layer.kind = ps.LayerKind.TextLayer
new_text_layer.textItem.contents = 'Hello, World!'
new_text_layer.textItem.position = [160, 167]
new_text_layer.textItem.size = 40
new_text_layer.textItem.color = text_color
options = ps.JPEGSaveOptions(quality=5)
# # save to jpg
jpg = 'd:/hello_world.jpg'
doc.saveAs(jpg, options, asCopy=True)
app.doJavaScript(f'alert("save to jpg: {jpg}")')

```

Create thumbnail
----------------


```python

import photoshop as ps

app = ps.Application()
active_document = app.activeDocument
orig_name = active_document.name
width_str = active_document.width
height_str = active_document.height
index = width_str / 1280
thumb_width = int(width_str / index)
thumb_height = int(height_str / index)
thumb_doc = active_document.duplicate('{}_tumb'.format(orig_name))
thumb_doc.resizeImage(thumb_width, thumb_height)
o = ps.JPEGSaveOptions(quality=10)
thumb_doc.saveAs('c:/thumb.jpg', o, as_copy=True)
thumb_doc.close()

```

Run javascript
--------------

```python

import photoshop as ps

app = ps.Application()
jsx = r"""
var doc = app.activeDocument;
var orig_name = doc.name;
alert(orig_name);
"""
app.doJavaScript(jsx)

```

Open .psd file
--------------

```python

import photoshop as ps

app = ps.Application()
app.load("your/psd/or/psb/file_path.psd")

```

Research and reference
----------------------
- https://theiviaxx.github.io/photoshop-docs/Photoshop/
- http://wwwimages.adobe.com/www.adobe.com/content/dam/acom/en/devnet/photoshop/pdfs/photoshop-cc-javascript-ref-2015.pdf
- https://github.com/lohriialo/photoshop-scripting-python
- https://www.adobe.com/devnet/photoshop/scripting.html
- https://www.youtube.com/playlist?list=PLUEniN8BpU8-Qmjyv3zyWaNvDYwJOJZ4m
- http://yearbook.github.io/esdocs/#/Photoshop/Application
- http://www.shining-lucy.com/wiki/page.php?id=appwiki:photoshop:ps_script
- http://www.tonton-pixel.com/wp-content/uploads/DecisionTable.pdf
- http://jongware.mit.edu/pscs5js_html/psjscs5/pc_Application.html
- https://indd.adobe.com/view/a0207571-ff5b-4bbf-a540-07079bd21d75
