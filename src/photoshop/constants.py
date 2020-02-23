presetKind = 'presetKindType'
smartSharpen = 'smartSharpen'
presetKindType = 'presetKindType'
presetKindCustom = 'presetKindCustom'
noiseReduction = 'noiseReduction'
blur = 'blur'
blurType = 'blurType'
AMNT = 'Amnt'
contentLayer = 'contentLayer'

# Name of photoshop ``AdobeScriptAutomation Scripts``.
ADOBE_SCRIPT_AUTOMATION_SCRIPTS = 'AdobeScriptAutomation Scripts'

# The photoshop version to COM progid mappings.
PHOTOSHOP_VERSION_MAPPINGS = {
    '2020': 140,
    '2019': 130,
    '2018': 120,
    '2017': 110,
}

# Values for Photoshop enumeration 'PsLayerKind'.
NORMAL_LAYER = 1
TEXT_LAYER = 2
SOLID_FILL_LAYER = 3

# Constants of Photoshop action.
# The all action constants from ``ScriptingListenerJS`` plugin.
# More ``StringIDs`` you can check out:
# http://www.tonton-pixel.com/wp-content/uploads/DecisionTable.pdf
NULL = 'null'
GSNB = 'GsnB'
ORDN = 'Ordn'
DOCI = 'DocI'
CLS = 'Cls '  # This string ID requires a space.
LYR = 'Lyr '  # This string ID requires a space.
OFST = 'Ofst'
PRC = '#Prc'
RDS = 'Rds '  # This string ID requires a space.
PX1 = '#Pxl'
PLC = 'Plc '  # This string ID requires a space.
IDNT = 'Idnt'
HRZN = 'Hrzn'
IN = 'In  '  # This string ID requires two spaces.
TRGT = 'Trgt'
SAVE = 'save'
SAVE_STAGE = 'saveStage'
SAVE_STAGE_TYPE = 'saveStageType'
SAVE_SUCCEEDED = 'saveSucceeded'
RASTERIZE_LAYER = 'rasterizeLayer'
YSN = 'YsN '  # This string ID requires a space.
N = 'N   '  # This string ID requires three spaces.
VRTC = 'Vrtc'
SVNG = 'Svng'
FTCS = 'FTcs'
QCST = 'QCSt'
QCSA = 'Qcsa'
FORCE_NOTIFY = 'forceNotify'
JSMS = 'jsMs'
JSCT = 'jsCt'
PLACED_LAYER_EDIT_CONTENTS = 'placedLayerEditContents'

# The photoshop save options.
JPEG_SAVE_OPTIONS = 'JPEGSaveOptions'
PNG_SAVE_OPTIONS = 'PNGSaveOptions'
PHOTOSHOP_SAVE_OPTIONS = 'PhotoshopSaveOptions'

# Controls whether Photoshop displays dialogs during scripts.
# Show all dialogs.
DIALOG_MODES_ALL = 0
# Show only dialogs related to errors.
DIALOG_MODES_ERROR = 1
# Show no dialogs.
DIALOG_MODES_NO = 2

# The measurement unit for ruler increments.
UNITS_CM = 6  # Centimeters.
UNITS_INCHES = 5  # Inches.
UNITS_MM = 4  # Millimeters.
UNITS_PERCENT = 3  # Percent.
UNITS_PICAS = 2  # Picas.
UNITS_PIXELS = 1  # Pixels.
UNITS_POINTS = 0  # Points.
