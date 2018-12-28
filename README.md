photoshop_python_api
====================
```python
from photoshop_python_api.documents import Documents
from photoshop_python_api.save_options import SaveOptions

documents = Documents()
# create new documents
doc = documents.add()
# add new artlayers
doc.add_art_layers()
options = SaveOptions().psd
# save to psd
doc.save_as('D:\\tes3111t.psd', options)

```

reference
=========
http://www.timcoolmode.com/images/small/PSD_Exporter.py

https://github.com/lohriialo/photoshop-scripting-python

https://evanmccall.wordpress.com/2015/03/09/how-to-develop-photoshop-tools-in-python/

https://techarttiki.blogspot.com/2008/08/photoshop-scripting-with-python.html

https://www.ps-scripts.com/