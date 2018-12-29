photoshop_python_api
====================

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

reference
=========
http://www.timcoolmode.com/images/small/PSD_Exporter.py

https://github.com/lohriialo/photoshop-scripting-python

https://evanmccall.wordpress.com/2015/03/09/how-to-develop-photoshop-tools-in-python/

https://techarttiki.blogspot.com/2008/08/photoshop-scripting-with-python.html

https://www.ps-scripts.com/