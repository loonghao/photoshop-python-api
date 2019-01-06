from photoshop_python_api.application import Application
from photoshop_python_api.save_options import JPEGSaveOptions

MAX_THUMB_SIZE = 1280
app = Application()
doc = app.activeDocument
orig_name = doc.name
width_str = doc.width
height_str = doc.height
thumb_name = '{}_tumb'.format(orig_name)
index = width_str / MAX_THUMB_SIZE

thumb_width = int(width_str / index)

thumb_height = int(height_str / index)
print thumb_height, width_str

thumb_doc = doc.duplicate(orig_name)
thumb_doc.resize_image(thumb_width, thumb_height)
thumb_doc.save_as('c:/thumb.jpg', JPEGSaveOptions(), as_copy=True)
thumb_doc.close()
