"""Manual test all examples."""
import glob
import os

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

for script in glob.glob(os.path.join(root, "*.py")):
    try:
        exec(open(script, "r").read())
    except:
        print("Test failed: {}".format(script))
