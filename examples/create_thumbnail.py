"""Example of creating thumbnail images in Photoshop.

This script demonstrates how to:
1. Create thumbnails from the active document
2. Support different output formats (JPEG, PNG)
3. Maintain aspect ratio while resizing
4. Handle different quality settings
5. Support multiple output directories

Module Attributes:
    DEFAULT_QUALITY: Default JPEG quality setting (0-12)
    DEFAULT_MAX_RESOLUTION: Default maximum resolution for thumbnails
    SUPPORTED_FORMATS: List of supported output formats

Module Classes:
    None

Module Functions:
    create_sample_document() -> None
    create_thumbnail() -> str
    create_multiple_thumbnails() -> list[str]
    main() -> None
"""

# Import built-in modules
from __future__ import annotations

import os
import time
from pathlib import Path
from tempfile import mkdtemp
from typing import Optional, Literal

# Import local modules
from photoshop import Session
from photoshop.api import Units
from photoshop.api.enumerations import (
    NewDocumentMode,
    DocumentFill,
    LayerKind,
)

# Constants
DEFAULT_QUALITY = 10
DEFAULT_MAX_RESOLUTION = 512
SUPPORTED_FORMATS = Literal["jpg", "png"]

def create_sample_document(ps, name: str = "Sample Document") -> None:
    """Create a sample document with various content.
    
    Args:
        ps: Photoshop session object
        name: Name of the document to create
    """
    # Create a new document
    doc = ps.app.documents.add(
        width=800,
        height=600,
        resolution=72,
        name=name,
        mode=NewDocumentMode.NewRGB,
        initialFill=DocumentFill.White,
    )
    
    # Create a shape layer
    shape_layer = doc.artLayers.add()
    shape_layer.name = "Blue Rectangle"
    
    # Set shape color
    color = ps.SolidColor()
    color.rgb.red = 0
    color.rgb.green = 0
    color.rgb.blue = 255
    
    # Create shape selection
    doc.selection.select([
        [50, 50],
        [750, 50],
        [750, 550],
        [50, 550],
    ])
    
    # Fill shape
    ps.app.foregroundColor = color
    doc.selection.fill(ps.app.foregroundColor)
    doc.selection.deselect()
    
    # Add text layer
    text_layer = doc.artLayers.add()
    text_layer.kind = LayerKind.TextLayer
    text_layer.name = "Sample Text"
    text_layer.textItem.contents = "Thumbnail Demo"
    text_layer.textItem.position = [300, 300]
    text_layer.textItem.size = 48
    text_layer.textItem.font = "Microsoft YaHei"
    
    print(f"Created sample document: {name}")

def create_thumbnail(
    ps,
    source_doc,
    output_path: Optional[str] = None,
    max_resolution: int = DEFAULT_MAX_RESOLUTION,
    format: SUPPORTED_FORMATS = "jpg",
    quality: int = DEFAULT_QUALITY,
    maintain_aspect: bool = True,
    background_color: Optional[tuple[int, int, int]] = None,
) -> str:
    """Create a thumbnail image for currently active document.

    Args:
        ps: Photoshop session object
        source_doc: Source document object
        output_path: Output path for the thumbnail image
        max_resolution: Maximum resolution for the thumbnail image
        format: Output format ("jpg" or "png")
        quality: JPEG quality (1-12, only for JPG)
        maintain_aspect: If True, maintains aspect ratio
        background_color: RGB tuple for background color

    Returns:
        str: Path to the generated thumbnail image

    Raises:
        ValueError: If format is not supported or quality is out of range
        RuntimeError: If no active document is found
    """
    # Validate inputs
    if format not in ["jpg", "png"]:
        raise ValueError(f"Unsupported format: {format}. Use 'jpg' or 'png'")
    
    if format == "jpg" and not 1 <= quality <= 12:
        raise ValueError("JPEG quality must be between 1 and 12")

    # Generate output path if not provided
    if output_path is None:
        output_dir = Path(mkdtemp())
        output_path = str(output_dir / f"thumb.{format}")
    else:
        # Ensure directory exists
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

    # Create a temporary directory for intermediate files
    temp_dir = Path(mkdtemp())
    temp_path = str(temp_dir / f"temp_{Path(output_path).name}")

    # Get original dimensions
    width = source_doc.width
    height = source_doc.height

    # Calculate new dimensions
    if maintain_aspect:
        ratio = width / height
        if width > height:
            new_width = max_resolution
            new_height = max_resolution / ratio
        else:
            new_height = max_resolution
            new_width = max_resolution * ratio
    else:
        new_width = new_height = max_resolution

    # Create new document
    new_doc = ps.app.documents.add(
        width=new_width,
        height=new_height,
        resolution=72.0,
        mode=NewDocumentMode.NewRGB,
        initialFill=DocumentFill.White,
    )
    time.sleep(0.5)  # Wait for document to initialize

    try:
        # Set background color if specified
        if background_color:
            color = ps.SolidColor()
            color.rgb.red = background_color[0]
            color.rgb.green = background_color[1]
            color.rgb.blue = background_color[2]
            new_doc.backgroundColor = color

        # Use JavaScript to copy and paste
        js = f"""
        try {{
            var sourceDoc = app.documents.getByName("{source_doc.name}");
            var targetDoc = app.documents.getByName("{new_doc.name}");
            app.activeDocument = sourceDoc;
            sourceDoc.activeLayer.copy();
            app.activeDocument = targetDoc;
            targetDoc.paste();
            "success"
        }} catch(e) {{
            e.message
        }}
        """
        result = ps.app.doJavaScript(js)
        if result != "success":
            print(f"Warning: Copy operation failed - {result}")

        time.sleep(0.5)  # Wait for paste to complete

        # Save the thumbnail
        ps.app.activeDocument = new_doc
        if format == "jpg":
            options = ps.JPEGSaveOptions(quality=quality)
        else:  # png
            options = ps.PNGSaveOptions(compression=9)

        # Save with a temporary name first
        new_doc.saveAs(temp_path, options, True)
        time.sleep(0.5)  # Wait for save to complete

        # Close and reopen
        new_doc.close()
        time.sleep(0.5)  # Wait for close to complete

        # Open the temporary file
        new_doc = ps.app.open(temp_path)
        time.sleep(0.5)  # Wait for document to load

        # Save with the final name
        new_doc.saveAs(output_path, options, True)
        time.sleep(0.5)  # Wait for save to complete

        print(f"Created thumbnail: {output_path}")
        print(f"  Size: {new_width:.0f}x{new_height:.0f} pixels")
        print(f"  Format: {format.upper()}")
        if format == "jpg":
            print(f"  Quality: {quality}")

        return output_path

    finally:
        # Always close the new document
        if os.path.exists(temp_path):
            os.remove(temp_path)
        new_doc.close()
        time.sleep(0.5)  # Wait for close to complete
        # Clean up temporary directory
        temp_dir.rmdir()

def create_multiple_thumbnails(
    ps,
    source_path: str,
    sizes: list[int],
    output_dir: Optional[str] = None,
    format: SUPPORTED_FORMATS = "jpg",
    quality: int = DEFAULT_QUALITY,
    prefix: str = "thumb",
) -> list[str]:
    """Create multiple thumbnails of different sizes.

    Args:
        ps: Photoshop session object
        source_path: Path to source document
        sizes: List of maximum resolutions
        output_dir: Output directory (default: temp dir)
        format: Output format ("jpg" or "png")
        quality: JPEG quality (1-12, only for JPG)
        prefix: Filename prefix for thumbnails

    Returns:
        list[str]: List of paths to generated thumbnails
    """
    if output_dir is None:
        output_dir = mkdtemp()
    else:
        os.makedirs(output_dir, exist_ok=True)

    thumbnails = []
    source_doc = None
    
    try:
        # Open source document
        source_doc = ps.app.open(source_path)
        time.sleep(0.5)  # Wait for document to load

        # Ensure source document is active
        ps.app.activeDocument = source_doc
        time.sleep(0.5)  # Wait for document to activate

        for size in sizes:
            try:
                output_path = os.path.join(output_dir, f"{prefix}_{size}.{format}")
                thumb_path = create_thumbnail(
                    ps,
                    source_doc,
                    output_path=output_path,
                    max_resolution=size,
                    format=format,
                    quality=quality,
                )
                thumbnails.append(thumb_path)
                print(f"Created {size}px thumbnail: {thumb_path}")
            except Exception as e:
                print(f"Failed to create {size}px thumbnail: {e}")
                continue
    finally:
        # Close source document
        if source_doc:
            source_doc.close()
            time.sleep(0.5)  # Wait for close to complete

    return thumbnails

def main() -> None:
    """Run the example script.

    This function demonstrates different thumbnail creation scenarios:
    1. Basic thumbnail with default settings
    2. Custom thumbnail with specific format and quality
    3. Multiple thumbnails of different sizes
    """
    # Try different Photoshop versions
    versions = ["2024", "2023", "2022", "2021", "2020"]
    connected = False
    
    for version in versions:
        try:
            with Session(ps_version=version) as ps:
                print(f"Successfully connected to Photoshop {version}")
                connected = True
                
                # Store original ruler units
                app = ps.app
                start_ruler_units = app.preferences.rulerUnits
                app.preferences.rulerUnits = Units.Pixels
                
                try:
                    # Create a sample document
                    create_sample_document(ps)
                    source_doc = ps.active_document
                    
                    # Save sample document
                    temp_dir = mkdtemp()
                    source_path = os.path.join(temp_dir, "sample.psd")
                    options = ps.PhotoshopSaveOptions()
                    source_doc.saveAs(source_path, options)
                    time.sleep(0.5)  # Wait for save to complete
                    source_doc.close()
                    time.sleep(0.5)  # Wait for close to complete
                    
                    # Example 1: Basic thumbnail
                    source_doc = ps.app.open(source_path)
                    time.sleep(0.5)  # Wait for document to load
                    try:
                        thumb_file = create_thumbnail(ps, source_doc)
                        print(f"\nBasic thumbnail saved to: {thumb_file}")
                    finally:
                        source_doc.close()
                        time.sleep(0.5)  # Wait for close to complete

                    # Example 2: Custom thumbnail (PNG with blue background)
                    source_doc = ps.app.open(source_path)
                    time.sleep(0.5)  # Wait for document to load
                    try:
                        custom_thumb = create_thumbnail(
                            ps,
                            source_doc,
                            output_path="custom_thumb.png",
                            max_resolution=256,
                            format="png",
                            background_color=(0, 0, 255),
                        )
                        print(f"\nCustom thumbnail saved to: {custom_thumb}")
                    finally:
                        source_doc.close()
                        time.sleep(0.5)  # Wait for close to complete

                    # Example 3: Multiple thumbnails
                    print("\nCreating multiple thumbnails...")
                    thumbs = create_multiple_thumbnails(
                        ps,
                        source_path,
                        sizes=[128, 256],  # 减少尺寸数量
                        output_dir="thumbnails",
                        format="jpg",
                        quality=12,
                        prefix="photo",
                    )
                    print("\nCreated thumbnails:")
                    for thumb in thumbs:
                        print(f"- {thumb}")
                    
                finally:
                    # Restore ruler units
                    app.preferences.rulerUnits = start_ruler_units
                break  # Exit the loop if successful
        except Exception as e:
            print(f"Failed to connect to Photoshop {version}: {e}")
            continue
    
    if not connected:
        print("\nFailed to connect to any supported Photoshop version.")
        print("Please make sure Photoshop is installed and running correctly.")
        print("Supported versions: " + ", ".join(versions))

if __name__ == "__main__":
    main()
