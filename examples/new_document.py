# Create a new Photoshop document with diminsions 4 inches by 4 inches.
import photoshop as ps

# Start up Photoshop application
app = ps.Application()

start_ruler_units = app.preferences.rulerUnits

app.preferences.rulerUnits = ps.Units.Pixels

# Create the document
docRef = app.documents.add(1920, 1080, 72.0, "My New Document")

# Make sure to set the ruler units prior to creating the document.
app.preferences.rulerUnits = start_ruler_units
