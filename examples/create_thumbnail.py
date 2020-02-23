import photoshop as ps

MAX_THUMB_SIZE = 1280
app = ps.Application()
doc = app.activeDocument
orig_name = doc.name
width_str = doc.width
height_str = doc.height
thumb_name = f'{orig_name}_tumb'
index = width_str / MAX_THUMB_SIZE

thumb_width = int(width_str / index)

thumb_height = int(height_str / index)

thumb_doc = doc.duplicate(thumb_name)
thumb_doc.resizeImage(thumb_width, thumb_height - 100)
o = ps.JPEGSaveOptions()
thumb_doc.saveAs('d:/thumb.jpg', o, asCopy=True)
thumb_doc.close()
