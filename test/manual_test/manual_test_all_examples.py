"""Manual test all examples."""

# Import local modules
from photoshop.api import Application
from pathlib import Path

root = Path(__file__).parent.parent.parent.joinpath("examples")
for script_file in root.glob("*.py"):
    try:
        exec(script_file.read_text())
    except Exception as err:
        print(f"Test failed: {script_file}", str(err), end="\n")

# Clear up and close all documents.
app = Application()

while app.documents.length:
    app.activeDocument.close()
