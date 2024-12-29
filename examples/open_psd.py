"""PSD file opening and management in Photoshop.

This script demonstrates how to:
1. Open PSD/PSB files with different methods
2. Validate files before opening
3. Handle file opening errors
4. Work with opened documents
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Optional, Union

import photoshop.api as ps
from photoshop import Session

class OpenMethod(Enum):
    """PSD file opening methods."""
    DIRECT = auto()  # Direct opening using Application
    SESSION = auto()  # Opening using Session context manager

@dataclass
class OpenOptions:
    """PSD file opening options."""
    path: Union[str, Path]  # File path
    method: OpenMethod = OpenMethod.DIRECT  # Opening method
    as_copy: bool = False  # Open as copy
    show_dialogs: bool = False  # Show dialogs during open

class PSDOpener:
    """Class for opening and managing PSD files."""
    
    def __init__(self, app: Optional[ps.Application] = None) -> None:
        """Initialize PSD opener.
        
        Args:
            app: Optional Photoshop application instance
        """
        self.app = app or ps.Application()
    
    def _validate_file(self, path: Union[str, Path]) -> bool:
        """Validate PSD file.
        
        Args:
            path: File path
            
        Returns:
            bool: True if file is valid
            
        Raises:
            FileNotFoundError: If file does not exist
            ValueError: If file has invalid extension
        """
        path = Path(path)
        
        # Check if file exists
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        
        # Check extension
        if path.suffix.lower() not in [".psd", ".psb"]:
            raise ValueError(f"Invalid file extension: {path.suffix}")
        
        return True
    
    def open_file(self, options: OpenOptions) -> Optional[ps.Document]:
        """Open PSD file.
        
        Args:
            options: Opening options
            
        Returns:
            Document if successful, None otherwise
        """
        try:
            # Validate file
            self._validate_file(options.path)
            path = str(Path(options.path).absolute())
            
            # Open file using selected method
            if options.method == OpenMethod.DIRECT:
                return self._open_direct(path, options)
            return self._open_with_session(path, options)
            
        except Exception as e:
            print(f"Error opening file: {e}")
            return None
    
    def _open_direct(self, path: str, options: OpenOptions) -> Optional[ps.Document]:
        """Open file directly using Application.
        
        Args:
            path: Absolute file path
            options: Opening options
            
        Returns:
            Document if successful, None otherwise
        """
        try:
            # Set dialog preferences
            original_dialogs = self.app.displayDialogs
            self.app.displayDialogs = ps.DialogModes.NO if not options.show_dialogs else ps.DialogModes.ALL
            
            # Open document
            doc = self.app.open(path, options.as_copy)
            
            return doc
            
        except Exception as e:
            print(f"Error in direct open: {e}")
            return None
            
        finally:
            # Restore dialog preferences
            self.app.displayDialogs = original_dialogs
    
    def _open_with_session(self, path: str, options: OpenOptions) -> Optional[ps.Document]:
        """Open file using Session context manager.
        
        Args:
            path: Absolute file path
            options: Opening options
            
        Returns:
            Document if successful, None otherwise
        """
        try:
            # Open session
            with Session(path, action="open") as pss:
                # Get active document
                doc = pss.active_document
                print(f"Opened document: {doc.name}")
                return doc
            
        except Exception as e:
            print(f"Error in session open: {e}")
            return None

def main() -> None:
    """PSD file opening example."""
    try:
        # Initialize opener
        opener = PSDOpener()
        
        print("\n=== Opening PSD Files ===")
        
        # Example PSD file path (replace with actual path)
        file_path = os.path.join(os.path.dirname(__file__), "files", "layer_comps.psd")
        
        # Open file directly
        print("\nOpening file directly:")
        options1 = OpenOptions(
            path=file_path,
            method=OpenMethod.DIRECT,
            show_dialogs=False,
        )
        doc1 = opener.open_file(options1)
        if doc1:
            print(f"Opened document: {doc1.name}")
        
        # Open file with session
        print("\nOpening file with session:")
        options2 = OpenOptions(
            path=file_path,
            method=OpenMethod.SESSION,
        )
        doc2 = opener.open_file(options2)
        if doc2:
            print(f"Opened document: {doc2.name}")
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
