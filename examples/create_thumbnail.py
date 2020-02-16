from photoshop.application import Application
from photoshop.save_options import JPEGSaveOptions

MAX_THUMB_SIZE = 1280
app = Application()
doc = app.activeDocument
orig_name = doc.name
width_str = doc.width
height_str = doc.height
thumb_name = f'{orig_name}_tumb'
index = width_str / MAX_THUMB_SIZE

thumb_width = int(width_str / index)

thumb_height = int(height_str / index)

thumb_doc = doc.duplicate(thumb_name)
thumb_doc.resizeImage(thumb_width, thumb_height-100)
o = JPEGSaveOptions()
thumb_doc.saveAs('d:/thumb.jpg', o, as_copy=True)
thumb_doc.close()
