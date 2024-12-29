"""List and manage Photoshop documents.

This script demonstrates how to:
1. List all open documents
2. Get document information
3. Filter documents by properties
4. Sort documents by various criteria
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

import photoshop.api as ps

class DocumentSortBy(Enum):
    """Document sorting options."""
    NAME = "name"
    SIZE = "size"
    MODIFIED = "modified"
    CREATED = "created"

@dataclass
class DocumentInfo:
    """Document information."""
    name: str
    width: int
    height: int
    resolution: float
    mode: str
    bit_depth: int
    color_profile: str
    file_path: Optional[str] = None
    modified: bool = False
    
    @property
    def size(self) -> int:
        """Get document size in pixels."""
        return self.width * self.height
    
    def __str__(self) -> str:
        """Get string representation."""
        info = [
            f"Name: {self.name}",
            f"Size: {self.width}x{self.height} pixels",
            f"Resolution: {self.resolution} DPI",
            f"Mode: {self.mode}",
            f"Bit Depth: {self.bit_depth}",
            f"Color Profile: {self.color_profile}",
            f"Path: {self.file_path or 'Unsaved'}",
            f"Modified: {'Yes' if self.modified else 'No'}",
        ]
        return "\n".join(info)

class DocumentManager:
    """Class for managing Photoshop documents."""
    
    def __init__(self, app: ps.Application) -> None:
        """Initialize document manager.
        
        Args:
            app: Photoshop application instance
        """
        self.app = app
        self.cache: Dict[str, DocumentInfo] = {}  # Cache document info
    
    def _get_safe_property(self, obj: any, prop: str, default: any = None) -> any:
        """Safely get object property.
        
        Args:
            obj: Object to get property from
            prop: Property name
            default: Default value if property not found
            
        Returns:
            Property value or default
        """
        try:
            return getattr(obj, prop)
        except Exception:
            return default
    
    def get_document_info(self, doc: ps.Document) -> DocumentInfo:
        """Get document information.
        
        Args:
            doc: Photoshop document
            
        Returns:
            Document information
        """
        try:
            # Get document properties safely
            info = DocumentInfo(
                name=self._get_safe_property(doc, "name", "Untitled"),
                width=self._get_safe_property(doc, "width", 0),
                height=self._get_safe_property(doc, "height", 0),
                resolution=self._get_safe_property(doc, "resolution", 72),
                mode=str(self._get_safe_property(doc, "mode", "Unknown")),
                bit_depth=self._get_safe_property(doc, "bitsPerChannel", 8),
                color_profile=self._get_safe_property(doc, "colorProfileName", "None"),
                file_path=self._get_safe_property(doc, "fullName", None),
                modified=self._get_safe_property(doc, "isDirty", False),
            )
            
            # Cache info
            self.cache[info.name] = info
            return info
            
        except Exception as e:
            print(f"Error getting document info for {doc.name}: {e}")
            return DocumentInfo(
                name=self._get_safe_property(doc, "name", "Unknown"),
                width=0,
                height=0,
                resolution=0,
                mode="Unknown",
                bit_depth=0,
                color_profile="Unknown",
            )
    
    def list_documents(self, sort_by: DocumentSortBy = None, 
                      reverse: bool = False) -> List[DocumentInfo]:
        """List all open documents.
        
        Args:
            sort_by: Sort criteria
            reverse: Reverse sort order
            
        Returns:
            List of document information
        """
        try:
            # Get all documents
            docs = []
            for doc in self.app.documents:
                info = self.get_document_info(doc)
                docs.append(info)
            
            # Sort documents
            if sort_by:
                if sort_by == DocumentSortBy.NAME:
                    docs.sort(key=lambda x: x.name, reverse=reverse)
                elif sort_by == DocumentSortBy.SIZE:
                    docs.sort(key=lambda x: x.size, reverse=reverse)
                elif sort_by == DocumentSortBy.MODIFIED:
                    docs.sort(key=lambda x: x.modified, reverse=reverse)
            
            return docs
            
        except Exception as e:
            print(f"Error listing documents: {e}")
            return []
    
    def find_documents(self, 
                      name_pattern: str = None,
                      min_width: int = None,
                      min_height: int = None,
                      mode: str = None,
                      modified_only: bool = False) -> List[DocumentInfo]:
        """Find documents matching criteria.
        
        Args:
            name_pattern: Document name pattern
            min_width: Minimum width in pixels
            min_height: Minimum height in pixels
            mode: Color mode
            modified_only: Only modified documents
            
        Returns:
            List of matching documents
        """
        try:
            docs = self.list_documents()
            filtered = []
            
            for doc in docs:
                # Apply filters
                if name_pattern and name_pattern.lower() not in doc.name.lower():
                    continue
                    
                if min_width and doc.width < min_width:
                    continue
                    
                if min_height and doc.height < min_height:
                    continue
                    
                if mode and doc.mode != mode:
                    continue
                    
                if modified_only and not doc.modified:
                    continue
                
                filtered.append(doc)
            
            return filtered
            
        except Exception as e:
            print(f"Error finding documents: {e}")
            return []
    
    def print_document_list(self, docs: List[DocumentInfo], 
                          detailed: bool = False) -> None:
        """Print document list.
        
        Args:
            docs: List of documents
            detailed: Show detailed information
        """
        if not docs:
            print("\nNo documents found")
            return
        
        print(f"\nFound {len(docs)} document(s):")
        for i, doc in enumerate(docs, 1):
            if detailed:
                print(f"\n{i}. {doc}")
            else:
                print(f"{i}. {doc.name} ({doc.width}x{doc.height})")

def main() -> None:
    """List documents example."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        manager = DocumentManager(app)
        
        # List all documents
        print("\n=== All Documents ===")
        docs = manager.list_documents(sort_by=DocumentSortBy.NAME)
        manager.print_document_list(docs, detailed=True)
        
        # Find modified documents
        print("\n=== Modified Documents ===")
        modified = manager.find_documents(modified_only=True)
        manager.print_document_list(modified)
        
        # Find large documents
        print("\n=== Large Documents (>1000px) ===")
        large = manager.find_documents(min_width=1000, min_height=1000)
        manager.print_document_list(large)
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
