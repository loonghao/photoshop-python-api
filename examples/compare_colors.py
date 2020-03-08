"""Check whether the foreground is equal to the background color.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/CompareColors.py

"""
import photoshop as ps

app = ps.Application()

if app.foregroundColor.isEqual(app.backgroundColor):
    print("They're Equal")
else:
    print("NOT Equal")
