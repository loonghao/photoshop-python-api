# Import built-in modules
import os

# Import local modules
from photoshop import Session


root = "your/images/root"
files = []
for name in os.listdir(root):
    files.append(os.path.join(root, name))
with Session() as api:
    options = api.BatchOptions()
    options.destination = 3
    options.destinationFolder = "c:\\test"
    api.app.batch(files=files, actionName="Quadrant Colors", actionSet="Default Actions", options=options)
