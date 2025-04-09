<p align="center">
<img src="https://i.imgur.com/cjp1RH6.png" alt="logo">
</p>

<p align="center">
<a href="https://img.shields.io/pypi/pyversions/photoshop-python-api">
<img src="https://img.shields.io/pypi/pyversions/photoshop-python-api" alt="python version"></a>
<a href="https://badge.fury.io/py/photoshop-python-api">
<img src="https://img.shields.io/pypi/v/photoshop-python-api?color=green" alt="PyPI version"></a>
<img src="https://img.shields.io/pypi/dw/photoshop-python-api" alt="Downloads Status">
<a href="https://pepy.tech/badge/photoshop-python-api">
<img src="https://pepy.tech/badge/photoshop-python-api" alt="Downloads"></a>
<img src="https://img.shields.io/pypi/l/photoshop-python-api" alt="License">
<img src="https://img.shields.io/pypi/format/photoshop-python-api" alt="pypi format">
<a href="https://discord.gg/AnxSa6n">
<img src="https://img.shields.io/discord/724615671400628314" alt="Chat on Discord"></a>
<a href="https://github.com/loonghao/photoshop-python-api/graphs/commit-activity">
<img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>
<a href="https://github.com/loonghao/photoshop-python-api/actions/workflows/bumpversion.yml">
<img src="https://github.com/loonghao/photoshop-python-api/actions/workflows/bumpversion.yml/badge.svg" alt="Bump version"></a>
<a href="https://github.com/loonghao/photoshop-python-api/actions/workflows/pages/pages-build-deployment">
<img src="https://github.com/loonghao/photoshop-python-api/actions/workflows/pages/pages-build-deployment/badge.svg" alt="pages-build-deployment"></a>
<a href="https://github.com/loonghao/photoshop-python-api/actions/workflows/publish_docs.yml">
<img src="https://github.com/loonghao/photoshop-python-api/actions/workflows/publish_docs.yml/badge.svg" alt="Documentation Status"></a>
<a href="https://img.shields.io/badge/photoshop-2024-green">
<img src="https://img.shields.io/badge/photoshop-2024-green" alt="photoshop-2024"></a>
<a href="https://img.shields.io/badge/photoshop-2023-green">
<img src="https://img.shields.io/badge/photoshop-2023-green" alt="photoshop-2023"></a>
<a href="https://img.shields.io/badge/photoshop-2022-green">
<img src="https://img.shields.io/badge/photoshop-2022-green" alt="photoshop-2022"></a>
<a href="https://img.shields.io/badge/photoshop-2021-green">
<img src="https://img.shields.io/badge/photoshop-2021-green" alt="photoshop-2021"></a>
<a href="https://img.shields.io/badge/photoshop-2020-green">
<img src="https://img.shields.io/badge/photoshop-2020-green" alt="photoshop-2020"></a>
<a href="https://img.shields.io/badge/photoshop-CC2019-green">
<img src="https://img.shields.io/badge/photoshop-CC2019-green" alt="photoshop-CC2019"></a>
<a href="https://img.shields.io/badge/photoshop-CC2018-green">
<img src="https://img.shields.io/badge/photoshop-CC2018-green" alt="photoshop-CC2018"></a>
<a href="https://img.shields.io/badge/photoshop-CC2017-green">
<img src="https://img.shields.io/badge/photoshop-CC2017-green" alt="photoshop-CC2017"></a>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-18-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
</p>

<p align="center">Python API for Photoshop.</p>
<p align="center"><i>⚠️ Only for Windows platform !</i></p>

<p align="center"><em>The example above was created with Photoshop Python API. Check it out at <a href="https://loonghao.github.io/photoshop-python-api/examples">https://loonghao.github.io/photoshop-python-api/examples</a>.</em></p>

Has been tested and used Photoshop version:

| Photoshop Version | Supported          |
|-------------------| ------------------ |
| 2025              |       ✅           |
| 2024              |       ✅           |
| 2023              |       ✅           |
| 2022              |       ✅           |
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
text_color.rgb.red = 0
text_color.rgb.green = 255
text_color.rgb.blue = 0
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
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/loonghao"><img src="https://avatars1.githubusercontent.com/u/13111745?v=4?s=100" width="100px;" alt="Hal"/><br /><sub><b>Hal</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=loonghao" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/voodraizer"><img src="https://avatars0.githubusercontent.com/u/1332729?v=4?s=100" width="100px;" alt="voodraizer"/><br /><sub><b>voodraizer</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Avoodraizer" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/brunosly"><img src="https://avatars2.githubusercontent.com/u/4326547?v=4?s=100" width="100px;" alt="brunosly"/><br /><sub><b>brunosly</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Abrunosly" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tubi-carrillo"><img src="https://avatars3.githubusercontent.com/u/33004093?v=4?s=100" width="100px;" alt="tubi"/><br /><sub><b>tubi</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Atubi-carrillo" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/wjxiehaixin"><img src="https://avatars0.githubusercontent.com/u/48039822?v=4?s=100" width="100px;" alt="wjxiehaixin"/><br /><sub><b>wjxiehaixin</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Awjxiehaixin" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://it.econline.net"><img src="https://avatars0.githubusercontent.com/u/993544?v=4?s=100" width="100px;" alt="罗马钟"/><br /><sub><b>罗马钟</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Aenzozhong" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ClementHector"><img src="https://avatars.githubusercontent.com/u/7068597?v=4?s=100" width="100px;" alt="clement"/><br /><sub><b>clement</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3AClementHector" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/krevlinmen"><img src="https://avatars.githubusercontent.com/u/56278440?v=4?s=100" width="100px;" alt="krevlinmen"/><br /><sub><b>krevlinmen</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Akrevlinmen" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SThomasN"><img src="https://avatars.githubusercontent.com/u/63218023?v=4?s=100" width="100px;" alt="Thomas"/><br /><sub><b>Thomas</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3ASThomasN" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/CaptainCsaba"><img src="https://avatars.githubusercontent.com/u/59013751?v=4?s=100" width="100px;" alt="CaptainCsaba"/><br /><sub><b>CaptainCsaba</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3ACaptainCsaba" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ilharper.vbox.moe"><img src="https://avatars.githubusercontent.com/u/20179549?v=4?s=100" width="100px;" alt="Il Harper"/><br /><sub><b>Il Harper</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=Afanyiyu" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blunderedbishop"><img src="https://avatars.githubusercontent.com/u/56189376?v=4?s=100" width="100px;" alt="blunderedbishop"/><br /><sub><b>blunderedbishop</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Ablunderedbishop" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MrTeferi"><img src="https://avatars.githubusercontent.com/u/92750180?v=4?s=100" width="100px;" alt="MrTeferi"/><br /><sub><b>MrTeferi</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=MrTeferi" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/damienchambe"><img src="https://avatars.githubusercontent.com/u/42462209?v=4?s=100" width="100px;" alt="Damien Chambe"/><br /><sub><b>Damien Chambe</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=damienchambe" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/be42day"><img src="https://avatars.githubusercontent.com/u/20614168?v=4?s=100" width="100px;" alt="Ehsan Akbari Tabar"/><br /><sub><b>Ehsan Akbari Tabar</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3Abe42day" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/in/michael-ikemann"><img src="https://avatars.githubusercontent.com/u/33489959?v=4?s=100" width="100px;" alt="Michael Ikemann"/><br /><sub><b>Michael Ikemann</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/issues?q=author%3AAlyxion" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dsmtE"><img src="https://avatars.githubusercontent.com/u/37016704?v=4?s=100" width="100px;" alt="Enguerrand DE SMET"/><br /><sub><b>Enguerrand DE SMET</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=dsmtE" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.thbattle.net"><img src="https://avatars.githubusercontent.com/u/857880?v=4?s=100" width="100px;" alt="Proton"/><br /><sub><b>Proton</b></sub></a><br /><a href="https://github.com/loonghao/photoshop-python-api/commits?author=feisuzhu" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://allcontributors.org) specification.
Contributions of any kind are welcome!

# Repobeats analytics
![Repobeats analytics](https://repobeats.axiom.co/api/embed/0f4ab02065b94983fc95677c6587a61ce5fa8397.svg "Repobeats analytics image")


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


## 🛠️ Development Guide

Welcome to the development guide for the Photoshop Python API project! This section outlines our development practices and standards to ensure code quality and consistency.

### 📋 Quick Start for Contributors

```bash
# Clone the repository
git clone https://github.com/loonghao/photoshop-python-api.git
cd photoshop-python-api

# Install dependencies with Poetry
poetry install

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

### 🎨 Code Style & Quality

We maintain high code quality standards through automated tools and consistent style guidelines:

- **Style Guide**: We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) with project-specific adjustments:
  - Line length: 120 characters max
  - Docstrings: Google style format
  - Quotes: Double quotes preferred

- **Quality Tools**:
  - [Black](https://black.readthedocs.io/) - Code formatting
  - [isort](https://pycqa.github.io/isort/) - Import organization
  - [flake8](https://flake8.pycqa.org/) - Style enforcement
  - [pre-commit](https://pre-commit.com/) - Automated checks before commits

### 🔄 Git Workflow

We use a structured workflow to maintain a clean and organized repository:

- **Commit Messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/) format

  ```text
  <type>(<scope>): <description>

  [optional body]

  [optional footer(s)]
  ```

  Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

- **Branching Strategy**:
  - Main branch: `main` - Always stable and deployable
  - Feature branches: `feature/<feature-name>`
  - Bug fixes: `fix/<bug-description>`
  - Documentation: `docs/<doc-description>`

### 🧪 Testing

We value thorough testing to ensure reliability:

- **Framework**: We use `pytest` for all tests
- **Coverage**: Aim for high test coverage on new features
- **Run Tests**: `pytest` or `poetry run pytest`

### 📦 Development Environment

- **Python Versions**: We support Python 3.8+ (see `pyproject.toml` for specifics)
- **Dependency Management**: [Poetry](https://python-poetry.org/) for consistent environments
- **Virtual Environment**: Poetry automatically creates and manages virtual environments

### 🤝 Contributing Process

1. **Fork & Clone**: Fork the repository and clone your fork
2. **Branch**: Create a feature branch with a descriptive name
3. **Develop**: Make your changes following our code style guidelines
4. **Test**: Ensure all tests pass and add new tests for new features
5. **Commit**: Use conventional commit format for clear history
6. **Push & PR**: Push your branch and create a Pull Request
7. **Review**: Address any feedback from code reviews
8. **Merge**: Once approved, your PR will be merged

Thank you for contributing to the Photoshop Python API project! 🎉
