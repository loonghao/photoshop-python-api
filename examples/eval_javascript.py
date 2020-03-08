import photoshop as ps

app = ps.Application()
jsx = r"""
var doc = app.activeDocument;
var orig_name = doc.name;
alert(orig_name);
"""
app.doJavaScript(jsx)


# Print name of current active document.
print(app.doJavaScript("app.activeDocument.name"))
