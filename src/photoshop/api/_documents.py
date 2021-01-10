from ._core import Photoshop
from ._document import Document
from .enumerations import BitsPerChannelType, DocumentFill, NewDocumentMode


# pylint: disable=too-many-public-methods, too-many-arguments
class Documents(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    def add(
        self,
        width: int = 960,
        height: int = 540,
        resolution: float = 72.0,
        name: str = None,
        mode: int = NewDocumentMode.NewRGB,
        initialFill: int = DocumentFill.White,
        pixelAspectRatio: float = 1.0,
        bitsPerChannel: int = BitsPerChannelType.Document8Bits,
        colorProfileName: str = None,
    ):
        """Creates a new document object and adds it to this collections.

        Args:
            width (int): The width of the document.
            height (int): The height of the document.
            resolution (int): The resolution of the document (in pixels per inch)
            name (str): The name of the document.
            mode (): The document mode.
            initialFill : The initial fill of the document.
            pixelAspectRatio: The initial pixel aspect ratio of the document.
                                Default is `1.0`, the range is `0.1-10.00`.
            bitsPerChannel: The number of bits per channel.
            colorProfileName: The name of color profile for document.

        Returns:
            .Document: Document instance.

        """
        return Document(
            self.app.add(
                width,
                height,
                resolution,
                name,
                mode,
                initialFill,
                pixelAspectRatio,
                bitsPerChannel,
                colorProfileName,
            )
        )

    def __iter__(self):
        for doc in self.app:
            yield Document(doc)

    @property
    def length(self):
        return len(list(self.app))

    def getByName(self, document_name: str):
        return Document(self.app.getByName(document_name))
