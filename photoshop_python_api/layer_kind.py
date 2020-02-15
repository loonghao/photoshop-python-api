# This is an enum that will work in python-2 and python-3. No need for methods
# in here. This is an enum which means we don't need an __init__ method.
class LayerKind(object):
    BLACKANDWHITE = 1
    BRIGHTNESSCONTRAST = 2
    CHANNELMIXER = 3
    COLORBALANCE = 5
    CURVES = 6
    EXPOSURE = 7
    GRADIENTFILL = 8
