# Import local modules
from __future__ import annotations

from photoshop.api._collection_base import CollectionBase
from photoshop.api._document import Document
from photoshop.api.enumerations import BitsPerChannelType, DocumentFill, NewDocumentMode
from photoshop.api.errors import PhotoshopPythonAPIError


# pylint: disable=too-many-public-methods, too-many-arguments
class Documents(CollectionBase[Document]):
    """The collection of open documents."""

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
            width: The width of the document (in pixels).
            height: The height of the document (in pixels).
            resolution: The resolution of the document (in pixels per inch)
            name: The name of the document.
            mode: The document mode.
            initialFill: The initial fill of the document.
            pixelAspectRatio: The initial pixel aspect ratio of the document.
                Default is `1.0`, the range is `0.1-10.00`.
            bitsPerChannel: The number of bits per channel.
            colorProfileName: The name of color profile for document.

        Returns:
            Document: The newly created document instance.
        """
        return self._wrap_item(
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
            ),
        )

    def getByName(self, document_name: str) -> Document:
        """Get document by given document name.
        
        Args:
            document_name: The name of the document to find
            
        Returns:
            Document: The document with the specified name
            
        Raises:
            PhotoshopPythonAPIError: If no document with the specified name is found
        """
        for doc in self:
            if doc.name == document_name:
                return doc
        raise PhotoshopPythonAPIError(f'Could not find a document named "{document_name}"')

    def _wrap_item(self, item: Any) -> Document:
        """Wrap a COM document object in a Document instance.
        
        Args:
            item: The COM document object to wrap
            
        Returns:
            Document: The wrapped document
        """
        return Document(item)
