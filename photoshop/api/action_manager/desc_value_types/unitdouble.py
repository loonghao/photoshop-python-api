# Import built-in modules
from collections import namedtuple

from ..utils import id2str
from ..utils import str2id


UnitDouble_proto = namedtuple("UnitDouble_proto", ["unit", "double"])


class UnitDouble(UnitDouble_proto):
    """You can initialize a UnitDouble object with 2 arguments: unit, double."""

    @classmethod
    def _packer(cls, obj, index):
        unit = id2str(obj.getUnitDoubleType(index))
        double = obj.getUnitDoubleValue(index)
        return cls(unit, double)

    def _unpacker(self):
        unitid = str2id(self.unit)
        double = self.double
        return (unitid, double)
