"""Defines execjs, a function to run js in Node.js"""

# Import built-in modules
import os
import re
import subprocess


# Node.js check
nodestate = os.popen("node --version")
if not re.match(r"^v\d*\.\d*\.\d*", nodestate.read()):
    raise RuntimeError("Please check if Node.js is installed to PATH!")


def execjs(jst):
    tmpjs = jst.replace('"""', '"')
    run = subprocess.run("node", input=tmpjs, capture_output=True, text=True)
    result = run.stdout
    err = run.stderr
    if err:
        raise RuntimeError(err)
    return result
