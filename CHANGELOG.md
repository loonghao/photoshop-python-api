## v0.22.4 (2023-12-04)

### Fix

- **deps**: update dependency wheel to ^0.42.0

## v0.22.3 (2023-11-20)

### Fix

- **text_item**: Remove unused import
- **TextItem.font**: Change font to a read/write string property

## v0.22.2 (2023-11-08)

### Fix

- **workflows**: Add quotes to prevent 3.10 being interpretted as 3.1
- **typing**: Replace list with List as Python <= 3.8 does not support subscriptable types

### Refactor

- **Photoshop**: Remove unnecessary exception type from suppress
- **Application**: Fix incorrect docstring for app.purge, allow Path objects for app.load, wrap colorSettings exceptions
- **Photoshop**: Restructure the sequence of events attempting to initialize a valid Dispatch object

## v0.22.1 (2023-09-22)

### Refactor

- **TextFonts**: Add support for method 'get' and operator 'in'

## v0.22.0 (2023-09-18)

### Feat

- Explicitly flag COM methods

### Fix

- formatting and linting
- comtypes does not play well with hasattr

## v0.21.10 (2023-09-14)

### Fix

- fix auto bump version
- fix can't set attribute `activeHistoryState`

## v0.21.9 (2023-08-31)

### Fix

- **constants**: Update PHOTOSHOP_VERSION_MAPPINGS to add 2024 release mapping (v24/180.0)

## v0.21.8 (2023-08-22)

### Fix

- **deps**: update dependency wheel to v0.41.2

## v0.21.7 (2023-08-17)

### Fix

- **deps**: update dependency wheel to ^0.41.0

## v0.21.6 (2023-08-17)

### Fix

- **test_imports.py**: Include root in install lines
- **import-test.yml**: Try an alternate approach with multiple poetry install retries
- **import-test.yml**: Correct typo in poetry version string
- **import-test.yml**: Revert to <= poetry 1.5.0 to fix "Import Test" workflow
- **import-test.yml**: Attempt to update lock to prevent inconsitent poetry.lock and pyproject.toml
- **import-test**: Attempt to fix poetry bug in "Import Test" workflow
- **deps**: Attempt to fix failing "Import Test" workflow

### Refactor

- **TextFonts**: Implement __getitem__ to allow lookup by postScriptName

## v0.21.5 (2023-07-02)

### Fix

- fix paste contents of the clipboard

## v0.21.4 (2023-06-13)

### Fix

- **LayerSets**: Fix infinite recursion when trying to access LayerSets as a list

### Refactor

- **Photoshop**: Attempt to get running Photoshop application before spawning new one

## v0.21.3 (2023-05-18)

### Fix

- **deps**: update dependency wheel to ^0.40.0

## v0.21.2 (2023-05-17)

### Refactor

- **artLayers,layerSets**: Refactored __getitem__ to work like a dictionary key on LayerSets. Added type hinting and try/except to __getitem__ for both ArtLayers and LayerSets

## v0.21.1 (2023-02-14)

### Refactor

- update constants for support Photoshop 2023

## v0.21.0 (2023-01-06)

### Feat

- **png.py**: Add optional args to PNGSaveOptions

## v0.20.1 (2022-11-28)

### Refactor

- **action_descriptor**: Fix type hints for doubles

## v0.20.0 (2022-11-26)

### Feat

- add a new option for create batch

## v0.19.7 (2022-11-14)

### Fix

- **deps**: update dependency wheel to ^0.38.0

## v0.19.6 (2022-11-06)

### Refactor

- update constants for support Photoshop 2022

## v0.19.5 (2022-07-17)

### Refactor

- **application**: add a default value of action

## v0.19.4 (2022-07-10)

### Fix

- get document by document name from documents.

## v0.19.3 (2022-06-17)

### Fix

- fix import `EPSSaveOptions`

## v0.19.2 (2022-06-14)

### Refactor

- **session.py**: add EPS save options

## v0.19.1 (2022-05-29)

### Fix

- **document**: export document
- **png**: exported PNG image is too large

## v0.19.0 (2022-05-20)

### Fix

- **ArtLayer,-LayerSet**: adjusted linkedLayers property, fixed remove()

### Feat

- **ArtLayer**: added linkedLayers and opacity, fixed unlink

## v0.18.1 (2022-04-17)

### Refactor

- **ActionList**: Added ActionList to __init__ and Session to make ActionList callable from Application or Session object

## v0.18.0 (2022-04-04)

### Fix

- fix export document

### Feat

- add new function to convert as javascript

## v0.17.7 (2022-03-20)

### Fix

- **deps**: update dependency wheel to ^0.37.0

## v0.17.6 (2022-03-19)

### Refactor

- improve type hints

### Fix

- add `ArtLayer` instance return when duplicate layer

## v0.17.5 (2022-03-13)

### Fix

- update ci config and re-tag

## v0.17.4 (2022-03-13)

### Perf

- add more docstrings

## v0.17.3 (2022-03-13)

### Perf

- add more docstrings

## v0.17.2 (2022-03-13)

### Perf

- improve docs

### Fix

- retag and update ci

### Refactor

- improve `getByName` from `artLayers` and `layers`

## v0.17.1 (2022-03-12)

### Refactor

- improve docs

## v0.17.0 (2021-09-21)

### Feat

- Update the logic of searching the installation path of Photoshop through the registration

## v0.16.3 (2021-09-12)

### Fix

- add 2021 to version mappings

## v0.16.2 (2021-08-15)

### Fix

- **api/text_item.py**: missing width.setter for paragraphtext in text_item.py

## v0.16.1 (2021-07-04)

### Fix

- fix install failed in python-3.9

## v0.16.0 (2021-05-29)

### Feat

- **documents**: support get document by index

## v0.15.2 (2021-05-29)

### Refactor

- use absolute path imports
- use absolute path imports

## 0.15.1 (2021-02-03)

## 0.15.0 (2021-01-10)

## 0.14.0 (2020-10-22)

## 0.13.0 (2020-09-23)

## 0.12.1 (2020-09-13)

## 0.12.0 (2020-05-10)

## 0.11.0 (2020-05-07)

## 0.10.0 (2020-04-22)

## 0.9.0 (2020-04-09)

## 0.8.0 (2020-04-08)

## 0.7.2 (2020-04-01)

## 0.3.0 (2020-02-24)

## 0.2.1 (2020-02-17)
