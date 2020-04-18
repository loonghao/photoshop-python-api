"""Save your current active document as a .psd file."""
from photoshop import Session

with Session() as ps:
    psd_file = "your/psd/save/file/path.psd"
    doc = ps.active_document
    options = ps.PhotoshopSaveOptions()
    layers = doc.artLayers
    doc.saveAs(psd_file, options, True)
    ps.alert("Task done!")
    ps.echo(doc.activeLayer)
