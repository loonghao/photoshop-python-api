"""Let the current document Fit on screen."""

# Import local modules
from photoshop import Session


with Session() as ps:
    ps.app.runMenuItem(ps.app.charIDToTypeID("FtOn"))
