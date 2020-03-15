import photoshop as ps
from photoshop import Session

# style 1
app = ps.Application()
app.load("your/psd/or/psb/file_path.psd")

# style 2
with Session("your/psd/or/psb/file_path.psd", action="open") as ps:
    ps.echo(ps.active_document.name)
