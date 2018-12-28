photoshop_python_api
====================
```python
from photoshop_python_api.documents import Documents
from photoshop_python_api.save_options import SaveOptions
d = Documents()
doc = d.app.ActiveDocument
options = SaveOptions().psd
doc.SaveAs('D:\\tes2t.psd', options)
```

reference
=========
http://www.timcoolmode.com/images/small/PSD_Exporter.py

https://github.com/lohriialo/photoshop-scripting-python

https://evanmccall.wordpress.com/2015/03/09/how-to-develop-photoshop-tools-in-python/

https://techarttiki.blogspot.com/2008/08/photoshop-scripting-with-python.html

https://www.ps-scripts.com/