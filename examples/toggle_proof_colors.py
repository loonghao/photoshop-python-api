"""Toggle the proof color in Photoshop.

This script demonstrates how to toggle the proof colors in Photoshop,
which is equivalent to using the menu option View > Proof Colors (Ctrl + Y).

The proof colors feature allows you to preview how your document will look
when output on different devices or in different color spaces.

Example:
    Run this script directly to toggle proof colors:
        $ python toggle_proof_colors.py
"""

# Import built-in modules
from __future__ import annotations
import logging
from typing import NoReturn

# Import local modules
from photoshop import Session

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def toggle_proof_colors() -> NoReturn:
    """Toggle the proof colors in Photoshop.

    This function uses the Photoshop COM interface to toggle the proof colors view,
    which is equivalent to pressing Ctrl+Y in Photoshop.

    Raises:
        Exception: If there's an error toggling the proof colors.
    """
    try:
        with Session() as ps:
            ps.app.runMenuItem(ps.app.stringIDToTypeID("toggleProofColors"))
            logger.info("Successfully toggled proof colors")
    except Exception as e:
        logger.error("Failed to toggle proof colors: %s", str(e))
        raise


if __name__ == "__main__":
    toggle_proof_colors()
