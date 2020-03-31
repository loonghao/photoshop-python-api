from photoshop._core import Photoshop
from photoshop.document import Document
from photoshop.enumerations import NewDocumentMode
from photoshop.enumerations import DocumentFill
from photoshop.enumerations import BitsPerChannelType


class Documents(Photoshop):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def __len__(self):
        return self.length

    def add(self, width=960, height=540, resolution=72.0, name=None,
            mode=NewDocumentMode.NewRGB, initialFill=DocumentFill.White,
            pixelAspectRatio=None,
            bitsPerChannel=BitsPerChannelType.Document16Bits,
            colorProfileName=None
            ):
        """

        Args:
            width (int): The width of the document.
            height (int): The height of the document.
            resolution (int): The resolution of the document (in pixels per inch)
            name (str): The name of the document.
            mode (): The document mode.
            initialFill : The initial fill of the document.
            pixelAspectRatio: The initial pixel aspect ratio of the document.
            bitsPerChannel: The number of bits per channel.
            colorProfileName: The name of color profile for document.

        Returns:
            photoshop.Document: Document instance.

        """
        return Document(self.app.add(width, height, resolution,
                                     name, mode,
                                     initialFill, pixelAspectRatio,
                                     bitsPerChannel,
                                     colorProfileName))

    def __iter__(self):
        for layer in self.app:
            yield layer

    @property
    def length(self):
        return len(list(self.app))

    def getByName(self, document_name: str):
        return self.app.getByName(document_name)
