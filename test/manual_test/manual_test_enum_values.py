# Import local modules
from photoshop.api.application import Application
from photoshop.api.enumerations import FontSize


app = Application()
prefs = app.preferences
print(prefs.textFontSize)
prefs.textFontSize = FontSize.Medium
print(prefs.textFontSize)
prefs.textFontSize = FontSize.Small
print(prefs.textFontSize)
#app.eval_javascript("alert(app.preferences.textFontSize)")