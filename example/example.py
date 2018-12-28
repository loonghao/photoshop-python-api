# # -*- coding: utf-8 -*-
# """
# module author: Long Hao <hoolongvfx@gmail.com>
# """
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
