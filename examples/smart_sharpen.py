"""Example script demonstrating how to apply Smart Sharpen filter in Photoshop.

This script shows how to:
1. Open an image and prepare it for sharpening
2. Apply Smart Sharpen filter with custom settings
3. Handle different blur types
4. Save the sharpened result
5. Support batch processing

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SmartSharpen.py
"""

# Import built-in modules
from __future__ import annotations

import logging
import os
from tempfile import mkdtemp
from typing import Any, Dict, Optional, Tuple

# Import third-party modules
import examples._psd_files as psd

# Import local modules
from photoshop import Session
import photoshop.api as ps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def apply_smart_sharpen(
    app: Any,
    amount: float = 150.0,
    radius: float = 1.0,
    noise_reduction: float = 10.0,
    blur_type: str = "gaussian",
) -> bool:
    """Apply Smart Sharpen filter with specified settings.

    Args:
        app: Photoshop application object.
        amount: Sharpening amount (0-500).
        radius: Sharpening radius in pixels (0.1-1000).
        noise_reduction: Noise reduction percentage (0-100).
        blur_type: Type of blur ('gaussian', 'lens', or 'motion').

    Returns:
        True if successful, False otherwise.
    """
    try:
        # Validate parameters
        amount = max(0.0, min(500.0, amount))
        radius = max(0.1, min(1000.0, radius))
        noise_reduction = max(0.0, min(100.0, noise_reduction))
        
        # Create descriptor
        desc = ps.ActionDescriptor()
        
        # Set preset kind
        preset_kind = app.stringIDToTypeID(ps.EventID.PresetKind)
        preset_kind_type = app.stringIDToTypeID(ps.EventID.PresetKindType)
        preset_kind_custom = app.stringIDToTypeID(ps.EventID.PresetKindCustom)
        desc.putEnumerated(preset_kind, preset_kind_type, preset_kind_custom)
        
        # Set amount
        amount_id = app.charIDToTypeID("Amnt")
        percent_id = app.charIDToTypeID("#Prc")
        desc.putUnitDouble(amount_id, percent_id, amount)
        
        # Set radius
        radius_id = app.charIDToTypeID("Rds ")
        pixel_id = app.charIDToTypeID("#Pxl")
        desc.putUnitDouble(radius_id, pixel_id, radius)
        
        # Set noise reduction
        noise_id = app.stringIDToTypeID("noiseReduction")
        desc.putUnitDouble(noise_id, percent_id, noise_reduction)
        
        # Set blur type
        blur_id = app.charIDToTypeID("blur")
        blur_type_id = app.stringIDToTypeID("blurType")
        blur_type_map = {
            "gaussian": app.charIDToTypeID("GsnB"),
            "lens": app.charIDToTypeID("LnsB"),
            "motion": app.charIDToTypeID("MtnB"),
        }
        blur_type_value = blur_type_map.get(blur_type.lower(), blur_type_map["gaussian"])
        desc.putEnumerated(blur_id, blur_type_id, blur_type_value)
        
        # Execute filter
        smart_sharpen_id = app.stringIDToTypeID(ps.EventID.SmartSharpen)
        app.ExecuteAction(smart_sharpen_id, desc)
        
        logger.info(
            "Applied Smart Sharpen (Amount: %.1f%%, Radius: %.1fpx, "
            "Noise Reduction: %.1f%%, Blur: %s)",
            amount, radius, noise_reduction, blur_type,
        )
        return True

    except Exception as e:
        logger.error("Failed to apply Smart Sharpen: %s", str(e))
        return False


def process_image(
    doc: Any,
    app: Any,
    settings: Dict[str, float],
) -> bool:
    """Process a single image with Smart Sharpen filter.

    Args:
        doc: Document to process.
        app: Photoshop application object.
        settings: Dictionary of filter settings.

    Returns:
        True if successful, False otherwise.
    """
    try:
        # Ensure we have a valid document
        if not doc:
            logger.error("No document provided")
            return False

        # Log document info
        logger.info("Processing document: %s", doc.name)
        logger.info("Document size: %dx%d", doc.width, doc.height)
        logger.info("Number of layers: %d", doc.artLayers.length)

        # Try to find a suitable layer to sharpen
        if doc.artLayers.length > 0:
            # Try to find a normal layer
            found_layer = False
            for i in range(doc.artLayers.length):
                try:
                    layer = doc.artLayers[i]
                    layer_name = layer.name if hasattr(layer, "name") else f"Layer {i}"
                    layer_kind = layer.kind if hasattr(layer, "kind") else "Unknown"
                    
                    logger.info(
                        "Checking layer %d: %s (Kind: %s)",
                        i, layer_name, layer_kind,
                    )
                    
                    # Try to make this layer active
                    doc.activeLayer = layer
                    found_layer = True
                    logger.info("Using layer for sharpening: %s", layer_name)
                    break
                except Exception as e:
                    logger.warning("Failed to check layer %d: %s", i, str(e))
                    continue
            
            if not found_layer:
                logger.error("Could not find a suitable layer for sharpening")
                return False
        else:
            logger.error("Document has no layers")
            return False
        
        # Apply filter
        return apply_smart_sharpen(app, **settings)

    except Exception as e:
        logger.error("Failed to process image: %s", str(e))
        return False


def save_result(
    doc: Any,
    output_dir: Optional[str] = None,
    format_options: Optional[Dict] = None,
) -> Tuple[bool, str]:
    """Save the processed document.

    Args:
        doc: Document to save.
        output_dir: Directory to save the file in.
        format_options: Dictionary of save options.

    Returns:
        Tuple of (success, output_path).
    """
    try:
        # Setup save location
        if not output_dir:
            output_dir = mkdtemp()
        
        # Setup format options
        if not format_options:
            format_options = {
                "format": "psd",
                "options": ps.PhotoshopSaveOptions(),
            }
        
        # Generate output path
        base_name = os.path.splitext(os.path.basename(doc.name))[0]
        output_path = os.path.join(
            output_dir,
            f"{base_name}_sharpened.{format_options['format']}",
        )
        
        # Save document
        doc.saveAs(output_path, format_options["options"])
        logger.info("Saved result to: %s", output_path)
        
        return True, output_path

    except Exception as e:
        logger.error("Failed to save result: %s", str(e))
        return False, ""


def main() -> None:
    """Main function demonstrating Smart Sharpen filter usage."""
    try:
        with Session() as ps_app:
            # Get sample PSD file
            psd_files = psd.get_psd_files()
            file_path = psd_files["trim.psd"]  # Using a simpler file
            
            # Open document
            doc = ps_app.app.open(file_path)
            logger.info("Opened document: %s", doc.name)
            
            # Define filter settings
            settings = {
                "amount": 150.0,
                "radius": 1.0,
                "noise_reduction": 10.0,
                "blur_type": "gaussian",
            }
            
            # Process image
            if process_image(doc, ps_app.app, settings):
                # Save result
                success, output_path = save_result(doc)
                if success:
                    ps_app.alert(
                        "Smart Sharpen applied successfully!\n"
                        f"Result saved to: {output_path}",
                    )
                else:
                    ps_app.alert("Failed to save the result!")
            else:
                ps_app.alert("Failed to apply Smart Sharpen!")

    except Exception as e:
        logger.error("Session failed: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting Smart Sharpen example...")
        main()
        logger.info("Smart Sharpen example completed successfully")
    except Exception as e:
        logger.error("Smart Sharpen example failed: %s", str(e))
        raise
