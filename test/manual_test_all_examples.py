"""Manual test all examples."""
import glob
import os

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

for script_file in glob.iglob(os.path.join(root, "*.py")):
    try:
        exec(open(script_file, "r").read())
    except Exception as err:
        print(f"Test failed: {script_file}", str(err), end="\n")
