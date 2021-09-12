<p align="center">
<img src="https://i.imgur.com/cjp1RH6.png" alt="logo">
</p>

<p align="center">
<a href="https://img.shields.io/pypi/pyversions/photoshop-python-api">
<img src="https://img.shields.io/pypi/pyversions/photoshop-python-api" alt="python version"></a>
<a href="https://badge.fury.io/py/photoshop-python-api">
<img src="https://img.shields.io/pypi/v/photoshop-python-api?color=green" alt="PyPI version"></a>
<a href="https://photoshop-python-api.readthedocs.io/en/master/?badge=master">
<img src="https://readthedocs.org/projects/photoshop-python-api/badge/?version=master" alt="Documentation Status"></a>
<img src="https://img.shields.io/pypi/dw/photoshop-python-api" alt="Downloads Status">
<a href="https://pepy.tech/badge/photoshop-python-api">
<img src="https://pepy.tech/badge/photoshop-python-api" alt="Downloads"></a>
<img src="https://img.shields.io/pypi/l/photoshop-python-api" alt="License">
<img src="https://img.shields.io/pypi/format/photoshop-python-api" alt="pypi format">
<a href="https://discord.gg/AnxSa6n">
<img src="https://img.shields.io/discord/724615671400628314" alt="Chat on Discird"></a>
<a href="https://github.com/loonghao/photoshop-python-api/graphs/commit-activity">
<img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-11-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END --> 
</p>

<p align="center">Python API for Photoshop.</p>

<p align="center"><em>The example above was created with Photoshop Python API. Check it out at <a href="https://loonghao.github.io/photoshop-python-api/examples">https://loonghao.github.io/photoshop-python-api/examples</a>.</em></p>

Has been tested and used Photoshop version:

| Photoshop Version | Supported          |
| ----------------- | ------------------ |
| 2021              |       ✅           |
| 2020              |       ✅           |
| cc2019            |       ✅           |
| cc2018            |       ✅           |
| cc2017            |       ✅           |


Installing
----------
You can install via pip.

```cmd
pip install photoshop_python_api
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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/loonghao"><img src="https://avatars1.githubusercontent.com/u/13111745?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hal</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=loonghao" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/voodraizer"><img src="https://avatars0.githubusercontent.com/u/1332729?v=4?s=100" width="100px;" alt=""/><br /><sub><b>voodraizer</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Avoodraizer" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/brunosly"><img src="https://avatars2.githubusercontent.com/u/4326547?v=4?s=100" width="100px;" alt=""/><br /><sub><b>brunosly</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Abrunosly" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/tubi-carrillo"><img src="https://avatars3.githubusercontent.com/u/33004093?v=4?s=100" width="100px;" alt=""/><br /><sub><b>tubi</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Atubi-carrillo" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/wjxiehaixin"><img src="https://avatars0.githubusercontent.com/u/48039822?v=4?s=100" width="100px;" alt=""/><br /><sub><b>wjxiehaixin</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Awjxiehaixin" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://it.econline.net"><img src="https://avatars0.githubusercontent.com/u/993544?v=4?s=100" width="100px;" alt=""/><br /><sub><b>罗马钟</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Aenzozhong" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/ClementHector"><img src="https://avatars.githubusercontent.com/u/7068597?v=4?s=100" width="100px;" alt=""/><br /><sub><b>clement</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3AClementHector" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/krevlinmen"><img src="https://avatars.githubusercontent.com/u/56278440?v=4?s=100" width="100px;" alt=""/><br /><sub><b>krevlinmen</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Akrevlinmen" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SThomasN"><img src="https://avatars.githubusercontent.com/u/63218023?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thomas</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3ASThomasN" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/CaptainCsaba"><img src="https://avatars.githubusercontent.com/u/59013751?v=4?s=100" width="100px;" alt=""/><br /><sub><b>CaptainCsaba</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3ACaptainCsaba" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://ilharper.vbox.moe"><img src="https://avatars.githubusercontent.com/u/20179549?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Il Harper</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=Afanyiyu" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
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
