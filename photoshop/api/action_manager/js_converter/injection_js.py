#You may turn on syntax highlighting for js here.
injection = '''

class UnitDouble {
	constructor(unit,ndouble) {
		this.type = 'UnitDouble'
		this.unit = unit
		this.double = ndouble
	}
}

class Enumerated {
	constructor(enumtype,enumval) {
		this.type = 'Enumerated'
		this.enumtype = enumtype
		this.enumval = enumval
	}
}

class TypeID {
	constructor(string) {
		this.type = 'TypeID'
		this.string = string
	}
}

function charIDToTypeID(chr) {
	return 'CharID_'+chr
}
function stringIDToTypeID(str) {
	return 'StrnID_'+str
}

class ActionDescriptor {
	constructor() {this.type = 'ActionDescriptor'}
	putInteger(key,val) {this[key] = val}
	putDouble(key,val) {this[key] = val}
	putUnitDouble(key,unit,ndouble) {this[key] = new UnitDouble(unit,ndouble)}
	putString(key,val) {this[key] = val}
	putBoolean(key,val) {this[key] = val}
	putEnumerated(key,enumtype,enumval) {this[key] = new Enumerated(enumtype,enumval)}
	putObject(key,psclass,val) {val['_classID'] = psclass; this[key] = val}
	putReference(key,val) {this[key] = val}
	putList(key,val) {this[key] = val}
	putClass(key,val) {this[key] = new TypeID(val)}
}

class ActionList {
	constructor() {this.type = 'ActionList'; this.len = 0}
	putInteger(val) {this.len += 1; this[this.len-1] = val}
	putDouble(val) {this.len += 1; this[this.len-1] = val}
	putUnitDouble(unit,ndouble) {this.len += 1; this[this.len-1] = new UnitDouble(unit,ndouble)}
	putString(val) {this.len += 1; this[this.len-1] = val}
	putBoolean(val) {this.len += 1; this[this.len-1] = val}
	putEnumerated(enumtype,enumval) {this.len += 1; this[this.len-1] = new Enumerated(enumtype,enumval)}
	putObject(psclass,val) {this.len += 1; val['_classID'] = psclass; this[this.len-1] = val}
	putReference(val) {this.len += 1; this[this.len-1] = val}
	putList(val) {this.len += 1; this[this.len-1] = val}
	putClass(val) {this.len += 1; this[this.len-1] = new TypeID(val)}
}

class ActionReference {
	constructor() {this.type = 'ActionReference'; this.len = 0}
	putClass(dcls) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Class',
			'Value':null,
		}
	}
	putEnumerated(dcls,enumtype,enumval) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Enumerated',
			'Value':new Enumerated(enumtype,enumval),
		}
	}
	putIdentifier(dcls,val) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Identifier',
			'Value':val,
		}
	}
	putIndex(dcls,val) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Index',
			'Value':val,
		}
	}
	putName(dcls,val) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Name',
			'Value':val,
		}
	}
	putOffset(dcls,val) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Offset',
			'Value':val,
		}
	}
	putProperty(dcls,val) {
		this.len += 1
		this[this.len-1] = {
			'DesiredClass':dcls,
			'FormType':'Property',
			'Value':val,
		}
	}
}

var DialogModes = new Object
DialogModes.ALL = 'All'
DialogModes.ERROR = 'Error'
DialogModes.NO = 'No'

function executeAction(operate,desc,exeoption) {
	execlogdict = {}
	execlogdict['Operation'] = operate
	execlogdict['ActionDescriptor'] = desc
	execlogdict['Option'] = exeoption
	execlogjson = JSON.stringify(execlogdict, null, 4)
	console.log(execlogjson)
    console.log('END OF JSON')
}
'''