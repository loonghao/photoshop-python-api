"""Document creation management in Photoshop.

This script demonstrates how to:
1. Create documents with different sizes and settings
2. Use document presets
3. Handle different measurement units
4. Set document properties

Constants Reference:
- mode: 1=Bitmap, 2=Grayscale, 3=RGB, 4=CMYK, 7=Lab, 8=Multichannel
- initial_fill: 1=White, 2=Background Color, 3=Transparent
- bits_per_channel: 1=One, 8=Eight, 16=Sixteen, 32=ThirtyTwo
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple, Union

import photoshop.api as ps

class DocumentPreset(Enum):
    """Common document presets."""
    HD_1080P = (1920, 1080, 72.0, "HD 1080p")  # 1920x1080 HD
    HD_720P = (1280, 720, 72.0, "HD 720p")  # 1280x720 HD
    SQUARE_4K = (4000, 4000, 300.0, "4K Square")  # 4K Square
    A4_PRINT = (2480, 3508, 300.0, "A4 Print")  # A4 at 300 DPI
    INSTAGRAM = (1080, 1080, 72.0, "Instagram")  # Instagram Square
    FACEBOOK = (1200, 630, 72.0, "Facebook")  # Facebook Cover
    TWITTER = (1500, 500, 72.0, "Twitter")  # Twitter Header

@dataclass
class DocumentSettings:
    """Document settings."""
    width: float
    height: float
    resolution: float = 72.0
    name: str = "New Document"
    mode: int = 3  # RGB mode
    initial_fill: int = 1  # White
    pixel_aspect_ratio: float = 1.0
    bits_per_channel: int = 8  # 8-bit

class DocumentCreator:
    """Class for creating Photoshop documents."""
    
    def __init__(self, app: ps.Application) -> None:
        """Initialize document creator.
        
        Args:
            app: Photoshop application instance
        """
        self.app = app
        self.original_units = None
    
    def _set_units(self, units: ps.Units) -> None:
        """Set ruler units.
        
        Args:
            units: Units to set
        """
        self.original_units = self.app.preferences.rulerUnits
        self.app.preferences.rulerUnits = units
    
    def _restore_units(self) -> None:
        """Restore original ruler units."""
        if self.original_units is not None:
            self.app.preferences.rulerUnits = self.original_units
            self.original_units = None
    
    def _convert_to_pixels(self, value: float, from_units: ps.Units) -> float:
        """Convert value to pixels.
        
        Args:
            value: Value to convert
            from_units: Units to convert from
            
        Returns:
            float: Value in pixels
        """
        if from_units == ps.Units.Pixels:
            return value
        
        # Standard DPI for unit conversion
        dpi = 72.0
        
        # Convert to pixels
        if from_units == ps.Units.Inches:
            return value * dpi
        if from_units == ps.Units.Centimeters:
            return value * dpi / 2.54
        if from_units == ps.Units.Millimeters:
            return value * dpi / 25.4
        if from_units == ps.Units.Points:
            return value * dpi / 72.0
        if from_units == ps.Units.Picas:
            return value * dpi / 6.0
        return value
    
    def create_from_preset(self, preset: DocumentPreset) -> Optional[ps.Document]:
        """Create document from preset.
        
        Args:
            preset: Document preset
            
        Returns:
            Document if successful, None otherwise
        """
        try:
            width, height, resolution, name = preset.value
            settings = DocumentSettings(
                width=width,
                height=height,
                resolution=resolution,
                name=name,
            )
            return self.create_document(settings)
            
        except Exception as e:
            print(f"Error creating document from preset: {e}")
            return None
    
    def create_document(self, 
                       settings: Union[DocumentSettings, Tuple[float, float]],
                       units: ps.Units = ps.Units.Pixels) -> Optional[ps.Document]:
        """Create new document.
        
        Args:
            settings: Document settings or (width, height) tuple
            units: Units for width and height
            
        Returns:
            Document if successful, None otherwise
        """
        try:
            # Convert tuple to settings
            if isinstance(settings, tuple):
                settings = DocumentSettings(
                    width=settings[0],
                    height=settings[1],
                )
            
            # Set units for creation
            self._set_units(units)
            
            # Convert dimensions to pixels if needed
            width = self._convert_to_pixels(settings.width, units)
            height = self._convert_to_pixels(settings.height, units)
            
            # Create document
            doc = self.app.documents.add(
                width=width,
                height=height,
                resolution=settings.resolution,
                name=settings.name,
                mode=settings.mode,
                initialFill=settings.initial_fill,
                pixelAspectRatio=settings.pixel_aspect_ratio,
                bitsPerChannel=settings.bits_per_channel,
            )
            
            return doc
            
        except Exception as e:
            print(f"Error creating document: {e}")
            return None
            
        finally:
            # Restore original units
            self._restore_units()

def main() -> None:
    """Document creation example."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        creator = DocumentCreator(app)
        
        print("\n=== Creating Documents ===")
        
        # Create document from preset
        print("\nCreating HD 1080p document:")
        doc1 = creator.create_from_preset(DocumentPreset.HD_1080P)
        if doc1:
            print(f"Created document: {doc1.name} ({doc1.width}x{doc1.height})")
        
        # Create custom document in inches
        print("\nCreating 4x4 inch document:")
        settings = DocumentSettings(
            width=4,
            height=4,
            resolution=300,
            name="Print Document",
        )
        doc2 = creator.create_document(settings, units=ps.Units.Inches)
        if doc2:
            print(f"Created document: {doc2.name} ({doc2.width}x{doc2.height})")
        
        # Create simple document from dimensions
        print("\nCreating square document:")
        doc3 = creator.create_document((1000, 1000))
        if doc3:
            print(f"Created document: {doc3.name} ({doc3.width}x{doc3.height})")
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
