# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""
from application import Application
from active_document import ActiveDocument

class Documents(Application):
    def __init__(self):
        super(Documents, self).__init__()

    def add(self, *args, **kwargs):
        return self.app.Documents.Add(*args, **kwargs)

    def add_art_layer(self):
        doc_ref = self.add()
        return doc_ref.ArtLayers.Add()

    def active_document(self):
        return ActiveDocument()

if __name__ == '__main__':
    d = Documents()
    docRef = d.add_art_layer()
    docRef.Name = 'fff'
