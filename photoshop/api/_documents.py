# Import local modules
from photoshop.api._core import Photoshop
from photoshop.api._document import Document
from photoshop.api.enumerations import BitsPerChannelType
from photoshop.api.enumerations import DocumentFill
from photoshop.api.enumerations import NewDocumentMode
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods, too-many-arguments
class Documents(Photoshop):
    """The collection of open documents."""

    def __init__(self, parent):
        super().__init__(parent=parent)
        self._flag_as_method("add")

    def __len__(self) -> int:
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

    def __iter__(self) -> Document:
        for doc in self.app:
            self.adobe.activeDocument = doc
            yield Document(doc)

    def __getitem__(self, item) -> Document:
        try:
            return Document(self.app[item])
        except IndexError:
            raise PhotoshopPythonAPIError("Currently Photoshop did not find Documents.")

    @property
    def length(self) -> int:
        return len(list(self.app))

    def getByName(self, document_name: str) -> Document:
        """Get document by given document name."""
        for doc in self.app:
            if doc.name == document_name:
                return Document(doc)
        raise PhotoshopPythonAPIError(f'Could not find a document named "{document_name}"')
