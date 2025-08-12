from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from photoshop.api._document import Document


class BaseProtocol(Protocol):
    @property
    def typename(self) -> str: ...


class HistoryState(BaseProtocol, Protocol):
    @property
    def name(self) -> str: ...
    @property
    def parent(self) -> "Document": ...
    @property
    def snapshot(self) -> bool: ...


class MeasurementScale(BaseProtocol, Protocol):
    logicalLength: float
    logicalUnits: str
    pixelLength: int


class XMPMetadata(BaseProtocol, Protocol):
    @property
    def parent(self) -> "Document": ...

    rawData: str
