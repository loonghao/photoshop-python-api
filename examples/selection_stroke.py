"""Example script demonstrating how to create and stroke selections in Photoshop.

This script shows how to:
1. Create a selection in a document
2. Apply a stroke with custom color and width
3. Handle different stroke locations and blend modes

References:
    https://github.com/lohriialo/photoshop-scripting-python/blob/master/SelectionStroke.py
"""

# Import built-in modules
from __future__ import annotations

import logging
from typing import Any, List, Tuple

# Import local modules
from photoshop import Session
import photoshop.api as ps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_selection(
    doc: Any,
    offset: int = 10,
) -> Tuple[List[Tuple[int, int]], Any]:
    """Create a rectangular selection in the document.

    Args:
        doc: Active Photoshop document.
        offset: Offset from document edges in pixels.

    Returns:
        Tuple containing:
            - List of selection bounds points
            - Selection object reference
    """
    # Calculate selection bounds
    bounds = [
        (offset, offset),
        (doc.width - offset, offset),
        (doc.width - offset, doc.height - offset),
        (offset, doc.height - offset),
    ]

    # Create selection
    selection = doc.selection
    selection.select(bounds)
    
    return bounds, selection


def create_stroke_color(
    cyan: float = 58.0,
    magenta: float = 0.0,
    yellow: float = 70.0,
    black: float = 0.0,
) -> Any:
    """Create a CMYK color for the stroke.

    Args:
        cyan: Cyan component (0-100).
        magenta: Magenta component (0-100).
        yellow: Yellow component (0-100).
        black: Black component (0-100).

    Returns:
        SolidColor object with specified CMYK values.
    """
    color = ps.SolidColor()
    color.cmyk.cyan = cyan
    color.cmyk.magenta = magenta
    color.cmyk.yellow = yellow
    color.cmyk.black = black
    return color


def apply_selection_stroke(
    selection: Any,
    color: Any,
    width: int = 2,
    location: Any = ps.StrokeLocation.OutsideStroke,
    opacity: int = 75,
) -> None:
    """Apply a stroke to the current selection.

    Args:
        selection: Selection object to stroke.
        color: Color to use for the stroke.
        width: Width of the stroke in pixels.
        location: Location of the stroke (inside, center, or outside).
        opacity: Opacity of the stroke (0-100).
    """
    selection.selectBorder(width)
    selection.stroke(
        color,
        width,
        location,
        ps.ColorBlendMode.ColorBlendMode,
        opacity,
        True,
    )


def main() -> None:
    """Main function to demonstrate selection stroking."""
    try:
        with Session(action="new_document") as ps:
            app = ps.app

            # Check if we're on background layer
            doc = ps.active_document
            if doc.activeLayer.isBackgroundLayer:
                logger.error("Cannot perform operation on background layer")
                return

            # Store original ruler units
            start_ruler_units = app.preferences.rulerUnits
            app.preferences.rulerUnits = ps.Units.Pixels

            try:
                # Create selection
                bounds, selection = create_selection(doc)
                logger.info("Created selection at bounds: %s", bounds)

                # Create stroke color (lime green in CMYK)
                stroke_color = create_stroke_color(58, 0, 70, 0)

                # Disable dialogs for automation
                app.displayDialogs = ps.DialogModes.DisplayNoDialogs

                # Apply stroke
                apply_selection_stroke(
                    selection,
                    stroke_color,
                    width=2,
                    location=ps.StrokeLocation.OutsideStroke,
                    opacity=75,
                )
                logger.info("Applied stroke to selection")

            finally:
                # Restore ruler units
                app.preferences.rulerUnits = start_ruler_units
                logger.info("Restored original ruler units")

    except Exception as e:
        logger.error("Failed to stroke selection: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting selection stroke example...")
        main()
        logger.info("Selection stroke example completed successfully")
    except Exception as e:
        logger.error("Selection stroke example failed: %s", str(e))
        raise
