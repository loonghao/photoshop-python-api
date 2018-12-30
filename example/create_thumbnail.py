import os

from photoshop_python_api import Core
from photoshop_python_api.save_options import GIFSaveOptions

os.environ['PS_VERSION'] = "2017"
app = Core()
print app.name()