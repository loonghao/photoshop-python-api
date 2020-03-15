"""Check whether the foreground is equal to the background color.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/CompareColors.py

"""
from photoshop import Session

with Session() as ps:
    if ps.app.foregroundColor.isEqual(ps.app.backgroundColor):
        ps.echo("They're Equal.")
    else:
        ps.echo("NOT Equal.")
