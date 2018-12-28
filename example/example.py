# # -*- coding: utf-8 -*-
# """
# module author: Long Hao <hoolongvfx@gmail.com>
# """
from photoshop_python_api.documents import Documents
from photoshop_python_api.save_options import SaveOptions
d = Documents()
doc = d.app.ActiveDocument
options = SaveOptions().psd
doc.SaveAs('D:\\tes2t.psd', options)

