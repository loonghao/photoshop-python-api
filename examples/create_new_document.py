"""Example of creating new documents in Photoshop.

This script demonstrates how to:
1. Create documents with different sizes and settings
2. Use various color modes and resolutions
3. Set initial fill and background colors
4. Handle different measurement units
5. Create documents from presets

Module Attributes:
    None

Module Classes:
    None

Module Functions:
    create_basic_document() -> None
    create_custom_document() -> None
    create_preset_document() -> None
    main() -> None
"""

from __future__ import annotations
from typing import Optional

# Import local modules
from photoshop import Session
from photoshop.api import Units
from photoshop.api.enumerations import (
    NewDocumentMode,
    DocumentFill,
)

def create_basic_document(
    ps,
    name: str,
    width: int,
    height: int,
    resolution: float = 72.0,
    mode: NewDocumentMode = NewDocumentMode.NewRGB,
) -> None:
    """Create a basic document with minimal settings.
    
    Args:
        ps: Photoshop session object
        name: Name of the document
        width: Width in pixels
        height: Height in pixels
        resolution: Resolution in pixels/inch (default: 72.0)
        mode: Color mode (default: RGB)
    """
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=resolution,
        name=name,
        mode=mode,
        initialFill=DocumentFill.White,
    )
    print(f"Created basic document: {name}")
    print(f"  Size: {width}x{height} pixels")
    print(f"  Resolution: {resolution} ppi")
    print(f"  Mode: {mode.name}")

def create_custom_document(
    ps,
    name: str,
    width: int,
    height: int,
    resolution: float = 300.0,
    mode: NewDocumentMode = NewDocumentMode.NewRGB,
    bits_per_channel: int = 8,
    fill: DocumentFill = DocumentFill.Transparent,
    color_profile: Optional[str] = None,
) -> None:
    """Create a document with custom settings.
    
    Args:
        ps: Photoshop session object
        name: Name of the document
        width: Width in pixels
        height: Height in pixels
        resolution: Resolution in pixels/inch (default: 300.0)
        mode: Color mode (default: RGB)
        bits_per_channel: Bit depth (default: 8)
        fill: Initial fill type (default: Transparent)
        color_profile: Color profile name (default: None)
    """
    doc = ps.app.documents.add(
        width=width,
        height=height,
        resolution=resolution,
        name=name,
        mode=mode,
        initialFill=fill,
        bitsPerChannel=bits_per_channel,
        colorProfileName=color_profile,
    )
    print(f"\nCreated custom document: {name}")
    print(f"  Size: {width}x{height} pixels")
    print(f"  Resolution: {resolution} ppi")
    print(f"  Mode: {mode.name}")
    print(f"  Bit Depth: {bits_per_channel} bits/channel")
    print(f"  Fill: {fill.name}")
    if color_profile:
        print(f"  Color Profile: {color_profile}")

def create_preset_document(ps, preset_name: str) -> None:
    """Create a document from a preset using JavaScript.
    
    Args:
        ps: Photoshop session object
        preset_name: Name of the preset to use
    """
    js = f"""
    try {{
        var idMk = charIDToTypeID("Mk  ");
        var desc = new ActionDescriptor();
        var idNw = charIDToTypeID("Nw  ");
        desc.putString(idNw, "{preset_name}");
        executeAction(idMk, desc, DialogModes.NO);
        "success"
    }} catch(e) {{
        e.message
    }}
    """
    result = ps.app.doJavaScript(js)
    if result == "success":
        print(f"\nCreated document from preset: {preset_name}")
    else:
        print(f"\nFailed to create document from preset: {result}")

def main() -> None:
    """Run the example script.
    
    This function demonstrates different document creation scenarios:
    1. Basic document (HD video size)
    2. Custom document (print-ready)
    3. Preset document (common sizes)
    
    Returns:
        None
    """
    with Session() as ps:
        # Store original ruler units
        app = ps.app
        start_ruler_units = app.preferences.rulerUnits
        app.preferences.rulerUnits = Units.Pixels
        
        try:
            # Example 1: Create a basic HD document
            create_basic_document(
                ps,
                name="HD Video",
                width=1920,
                height=1080,
            )
            
            # Example 2: Create a custom print document
            create_custom_document(
                ps,
                name="Print Ready",
                width=3508,  # A4 size at 300ppi
                height=4961,
                resolution=300.0,
                mode=NewDocumentMode.NewCMYK,
                bits_per_channel=16,
                fill=DocumentFill.White,
                color_profile="U.S. Web Coated (SWOP) v2",
            )
            
            # Example 3: Create from preset
            create_preset_document(ps, "Web")
            
            print("\nProcess completed! Created the following documents:")
            print("1. HD Video (basic HD 1080p document)")
            print("2. Print Ready (custom CMYK print document)")
            print("3. Web (from preset)")
            
        finally:
            # Restore ruler units
            app.preferences.rulerUnits = start_ruler_units

if __name__ == "__main__":
    main()
