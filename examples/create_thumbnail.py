import os
from photoshop import Session

with Session(auto_close=True) as ps:
    orig_name = ps.active_document.name
    width_str = ps.active_document.width
    height_str = ps.active_document.height
    thumb_name = f'{orig_name}_tumb'
    index = width_str / 1248

    thumb_width = int(width_str / index)

    thumb_height = int(height_str / index)

    thumb_doc = ps.active_document.duplicate(thumb_name)
    thumb_doc.resizeImage(thumb_width, thumb_height - 100)
    thumb_file = 'd:/thumb.jpg'
    thumb_doc.saveAs(thumb_file, ps.JPEGSaveOptions(), asCopy=True)
    thumb_doc.close()
    os.startfile(thumb_file)
