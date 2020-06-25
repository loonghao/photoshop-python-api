photoshop_python_api
====================
![python version](https://img.shields.io/pypi/pyversions/photoshop-python-api)
[![PyPI version](https://img.shields.io/pypi/v/photoshop-python-api?color=green)](https://badge.fury.io/py/photoshop-python-api)
[![Documentation Status](https://readthedocs.org/projects/photoshop-python-api/badge/?version=master)](https://photoshop-python-api.readthedocs.io/en/master/?badge=master)
![Downloads Status](https://img.shields.io/pypi/dw/photoshop-python-api)
[![Downloads](https://pepy.tech/badge/photoshop-python-api)](https://pepy.tech/project/photoshop-python-api)
![license](https://img.shields.io/pypi/l/photoshop-python-api)
![pypi format](https://img.shields.io/pypi/format/photoshop-python-api)
[![chat on Discird](https://img.shields.io/discord/724615671400628314)](https://discord.gg/AnxSa6n)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END --> 

Python API for Photoshop.

https://photoshop-python-api.readthedocs.io

![logo](https://i.imgur.com/cjp1RH6.png)

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
```git exclude
git clone https://github.com/loonghao/photoshop_python_api.git
```
Install package.
```cmd
python setup.py install
```

Since it uses COM (Component Object Model) connect Photoshop, it can be used 
in any DCC software with a python interpreter.


Hello World
-----------

```python

import photoshop.api as ps
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
![demo](https://i.imgur.com/25TrzbV.gif)


Photoshop Session
-----------------
Use it as context.

```python

from photoshop import Session


with Session(action="new_document") as ps:
    doc = ps.active_document
    text_color = ps.SolidColor()
    text_color.rgb.green = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = ps.LayerKind.TextLayer
    new_text_layer.textItem.contents = 'Hello, World!'
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = ps.JPEGSaveOptions(quality=5)
    jpg = 'd:/hello_world.jpg'
    doc.saveAs(jpg, options, asCopy=True)
    ps.app.doJavaScript(f'alert("save to jpg: {jpg}")')


```

More examples
-------------
- https://photoshop-python-api.readthedocs.io/en/master/examples.html


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/loonghao"><img src="https://avatars1.githubusercontent.com/u/13111745?v=4" width="100px;" alt=""/><br /><sub><b>Hal</b></sub></a></td>
    <td align="center"><a href="https://github.com/voodraizer"><img src="https://avatars0.githubusercontent.com/u/1332729?v=4" width="100px;" alt=""/><br /><sub><b>voodraizer</b></sub></a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!


how to get Photoshop program ID
-------------------------------
```PS>
Get-ChildItem "HKLM:\SOFTWARE\Classes" | 
  ?{ ($_.PSChildName -match "^[a-z]+\.[a-z]+(\.\d+)?$") -and ($_.GetSubKeyNames() -contains "CLSID") } | 
  ?{ $_.PSChildName -match "Photoshop.Application" } | ft PSChildName
```
![get_program_id](https://i.imgur.com/UwPN7qq.png)

[How to get a list of COM objects from the registry](https://rakhesh.com/powershell/how-to-get-a-list-of-com-objects-from-the-registry/)

Useful links
------------
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
- http://shining-lucy.com/wiki/page.php?id=appwiki:photoshop:ps_script
- http://web.archive.org/web/20140121053819/http://www.pcpix.com/Photoshop/char.html
- http://www.tonton-pixel.com/scripts/utility-scripts/get-equivalent-id-code/index.html
- https://github.com/Adobe-CEP/Samples/tree/master/PhotoshopEvents
- https://evanmccall.wordpress.com/2015/03/09/how-to-develop-photoshop-tools-in-python
