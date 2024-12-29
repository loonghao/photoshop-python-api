"""Manage and retrieve Photoshop documents by name.

This script demonstrates how to:
1. Get document by name
2. List all open documents
3. Get document properties
4. Handle document errors
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, List, Optional

import examples._psd_files as psd  # Import from examples
from photoshop import Session

@dataclass
class DocumentInfo:
    """Information about a Photoshop document."""
    name: str
    path: str
    width: float
    height: float
    resolution: float
    mode: str
    bits_per_channel: int
    channels: int
    layers: int

class DocumentManager:
    """Class for managing Photoshop documents."""
    
    def __init__(self, ps: Session) -> None:
        """Initialize the document manager.
        
        Args:
            ps: Photoshop session instance
        """
        self.ps = ps
    
    def list_documents(self) -> List[str]:
        """List all open documents.
        
        Returns:
            List of document names
        """
        try:
            docs = [doc.name for doc in self.ps.app.documents]
            if docs:
                print("\nOpen documents:")
                for name in docs:
                    print(f"- {name}")
            else:
                print("No documents are open")
            return docs
            
        except Exception as e:
            print(f"Error listing documents: {e}")
            return []
    
    def get_document_by_name(self, name: str) -> Optional[Any]:
        """Get document by name.
        
        Args:
            name: Document name to find
            
        Returns:
            Document object if found, None otherwise
        """
        try:
            doc = self.ps.app.documents.getByName(name)
            print(f"\nFound document: {doc.name}")
            print(f"Full path: {doc.fullName}")
            return doc
            
        except Exception as e:
            print(f"Error getting document '{name}': {e}")
            return None
    
    def get_document_info(self, doc: Any) -> Optional[DocumentInfo]:
        """Get detailed information about a document.
        
        Args:
            doc: Document object
            
        Returns:
            DocumentInfo object if successful, None otherwise
        """
        try:
            # Get document dimensions using JavaScript
            js_code = """
            try {
                var doc = app.activeDocument;
                doc.width.value + "," + doc.height.value
            } catch(e) {
                e.message
            }
            """
            result = self.ps.app.doJavaScript(js_code)
            
            try:
                width, height = map(float, result.split(","))
            except Exception:
                print("Error getting document dimensions")
                return None
            
            # Create document info
            info = DocumentInfo(
                name=doc.name,
                path=str(doc.fullName),
                width=width,
                height=height,
                resolution=float(doc.resolution),
                mode=str(doc.mode),
                bits_per_channel=int(doc.bitsPerChannel),
                channels=len(doc.channels),
                layers=len(doc.artLayers),
            )
            
            print(f"\nDocument information for {info.name}:")
            print(f"- Path: {info.path}")
            print(f"- Size: {info.width:.1f}x{info.height:.1f} pixels")
            print(f"- Resolution: {info.resolution:.1f} PPI")
            print(f"- Mode: {info.mode}")
            print(f"- Bits per channel: {info.bits_per_channel}")
            print(f"- Channels: {info.channels}")
            print(f"- Layers: {info.layers}")
            
            return info
            
        except Exception as e:
            print(f"Error getting document info: {e}")
            return None
    
    def document_exists(self, name: str) -> bool:
        """Check if a document exists.
        
        Args:
            name: Document name to check
            
        Returns:
            True if document exists
        """
        try:
            self.ps.app.documents.getByName(name)
            return True
        except Exception:
            return False

def main() -> None:
    """Demonstrate document management."""
    # Get sample PSD file
    PSD_FILE = psd.get_psd_files()
    template_path = PSD_FILE["slate_template.psd"]
    template_name = os.path.basename(template_path)
    
    # Open document and manage it
    with Session(template_path, action="open", auto_close=True) as ps:
        try:
            print("\nInitializing document manager...")
            manager = DocumentManager(ps)
            
            # List all documents
            manager.list_documents()
            
            # Get document by name
            if manager.document_exists(template_name):
                doc = manager.get_document_by_name(template_name)
                if doc:
                    # Get document info
                    manager.get_document_info(doc)
            else:
                print(f"\nDocument '{template_name}' not found")
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
