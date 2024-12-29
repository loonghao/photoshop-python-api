"""Create a Hello World text layer in Photoshop.

This script demonstrates how to:
1. Create a new document
2. Add a text layer
3. Set text properties
4. Save the document
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum
from tempfile import mkdtemp
from typing import Optional, Tuple, Union

import photoshop.api as ps

class TextAlignment(Enum):
    """Text alignment options."""
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

@dataclass
class TextStyle:
    """Text style properties."""
    contents: str
    position: Tuple[float, float]
    size: float
    color: Union[ps.SolidColor, Tuple[int, int, int]] = (0, 0, 0)
    font: str = "Arial"
    alignment: TextAlignment = TextAlignment.LEFT
    bold: bool = False
    italic: bool = False
    opacity: float = 100.0

class TextCreator:
    """Class for creating text layers in Photoshop."""
    
    def __init__(self, app: ps.Application) -> None:
        """Initialize text creator.
        
        Args:
            app: Photoshop application instance
        """
        self.app = app
        self.doc = None
        self.text_layer = None
    
    def create_document(self, width: int = 500, height: int = 300) -> bool:
        """Create a new document.
        
        Args:
            width: Document width in pixels
            height: Document height in pixels
            
        Returns:
            True if successful
        """
        try:
            self.doc = self.app.documents.add(width=width, height=height)
            print(f"\nCreated new document: {width}x{height} pixels")
            return True
        except Exception as e:
            print(f"Error creating document: {e}")
            return False
    
    def create_text_layer(self, style: TextStyle) -> Optional[ps.ArtLayer]:
        """Create a text layer with specified style.
        
        Args:
            style: Text style properties
            
        Returns:
            Text layer if successful, None otherwise
        """
        try:
            if not self.doc:
                print("Error: No document is open")
                return None
            
            # Create text layer
            self.text_layer = self.doc.artLayers.add()
            self.text_layer.kind = ps.LayerKind.TextLayer
            
            # Set text properties
            text_item = self.text_layer.textItem
            text_item.contents = style.contents
            text_item.position = list(style.position)
            text_item.size = style.size
            text_item.font = style.font
            text_item.justification = {
                TextAlignment.LEFT: ps.Justification.Left,
                TextAlignment.CENTER: ps.Justification.Center,
                TextAlignment.RIGHT: ps.Justification.Right,
            }[style.alignment]
            
            # Set color
            if isinstance(style.color, tuple):
                color = ps.SolidColor()
                color.rgb.red = style.color[0]
                color.rgb.green = style.color[1]
                color.rgb.blue = style.color[2]
                text_item.color = color
            else:
                text_item.color = style.color
            
            # Set style
            if style.bold:
                text_item.fauxBold = True
            if style.italic:
                text_item.fauxItalic = True
            
            # Set opacity
            self.text_layer.opacity = style.opacity
            
            print(f"\nCreated text layer: {style.contents}")
            print(f"Font: {style.font}, Size: {style.size}pt")
            print(f"Position: {style.position}")
            print(f"Alignment: {style.alignment.value}")
            
            return self.text_layer
            
        except Exception as e:
            print(f"Error creating text layer: {e}")
            return None
    
    def save_document(self, file_path: str = None, 
                     quality: int = 5) -> Optional[str]:
        """Save document to file.
        
        Args:
            file_path: Path to save file, if None uses temp directory
            quality: Save quality (1-100)
            
        Returns:
            File path if successful, None otherwise
        """
        try:
            if not self.doc:
                print("Error: No document is open")
                return None
            
            # Generate file path
            if not file_path:
                file_path = os.path.join(mkdtemp("photoshop-python-api"), 
                                       "hello_world.jpg")
            
            # Save file
            options = ps.JPEGSaveOptions(quality=quality)
            self.doc.saveAs(file_path, options, asCopy=True)
            
            print(f"\nSaved document to: {file_path}")
            return file_path
            
        except Exception as e:
            print(f"Error saving document: {e}")
            return None

def hello_world() -> None:
    """Create a Hello World example."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        creator = TextCreator(app)
        
        # Create document
        if not creator.create_document(500, 300):
            return
        
        # Create text style
        style = TextStyle(
            contents="Hello, World!",
            position=(160, 167),
            size=40,
            color=(0, 255, 0),  # Green color
            font="Arial",
            alignment=TextAlignment.CENTER,
            bold=True,
            opacity=90,
        )
        
        # Create text layer
        if not creator.create_text_layer(style):
            return
        
        # Save and open file
        file_path = creator.save_document(quality=5)
        if file_path:
            os.startfile(file_path)
        
    except Exception as e:
        print(f"Error in hello_world: {e}")

if __name__ == "__main__":
    hello_world()
