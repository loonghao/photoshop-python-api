from photoshop_python_api.application import Application
app = Application()
jsx = r"""
var doc = app.activeDocument;
var orig_name = doc.name;
alert(orig_name);
"""
app.eval_javascript(jsx)
