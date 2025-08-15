# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._document import Document
from photoshop.api.collections import CollectionOfNamedObjects
from photoshop.api.enumerations import BitsPerChannelType
from photoshop.api.enumerations import DocumentFill
from photoshop.api.enumerations import NewDocumentMode


# pylint: disable=too-many-public-methods, too-many-arguments
class Documents(CollectionOfNamedObjects[Document, int | str]):
    """The collection of open documents."""

    def __init__(self, parent: Photoshop | None = None) -> None:
        super().__init__(Document, parent)
        self._flag_as_method("add")

    def add(
        self,
        width: int = 960,
        height: int = 540,
        resolution: float = 72.0,
        name: str | None = None,
        mode: NewDocumentMode = NewDocumentMode.NewRGB,
        initialFill: DocumentFill = DocumentFill.White,
        pixelAspectRatio: float = 1.0,
        bitsPerChannel: BitsPerChannelType = BitsPerChannelType.Document8Bits,
        colorProfileName: str | None = None,
    ) -> Document:
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
