"""This script demonstrates how you can use the action manager to execute the
Emboss filter.

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py

"""

# Import third-party modules
import examples._psd_files as psd  # Import from examples.

# Import local modules
from photoshop import Session


PSD_FILE = psd.get_psd_files()
file_path = PSD_FILE["layer_comps.psd"]

with Session(file_path, action="open") as ps:

    def SmartSharpen(inAmount, inRadius, inNoise):
        ss_dict = {
            '_classID':None,
            'presetKindType':am.Enumerated(type='presetKindType', value='presetKindCustom'),
            'amount':am.UnitDouble(unit='radius', double=inAmount),
            'radius':am.UnitDouble(unit='pixelsUnit', double=inRadius),
            'noiseReduction':am.UnitDouble(unit='percentUnit', double=inNoise),
            'blur':am.Enumerated(type='blurType', value='gaussianBlur')
        }
        ss_desc = ps.ActionDescriptor.load(ss_dict)
        app.ExecuteAction(am.str2id('smartSharpen'), ss_desc)

    SmartSharpen(300, 2.0, 20)