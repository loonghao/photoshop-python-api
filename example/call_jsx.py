from photoshop_python_api.application import Application

app = Application()
# print app.pixel_aspect_ratio
# print app.saved
# print app.resolution
# print app.selection
# print app.width
print app.background_color.cmyk

# from photoshop_python_api.art_layers import ArtLayers
# layer = ArtLayers()
# print layer.get_by_name('Layer 8')