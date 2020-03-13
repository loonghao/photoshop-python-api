import os
import glob

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

for script in glob.glob(os.path.join(root, "*.py")):
    print("Start test: {}".format(script))
    exec(open(script, "r").read(), {"pwd": root})
