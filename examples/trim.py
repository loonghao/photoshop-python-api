"""Demonstrate how to trim a Photoshop document.

This script shows how to use the trim operation in Photoshop, which removes
transparent or solid-colored pixels from the edges of an image. This is
equivalent to using Image > Trim in Photoshop.

The trim operation can remove:
    - Transparent pixels
    - Top-left pixel color
    - Bottom-right pixel color

Example:
    Run this script directly to trim the example PSD file:
        $ python trim.py
"""

# Import built-in modules
from __future__ import annotations
import logging
from typing import NoReturn

# Import third-party modules
import examples._psd_files as psd

# Import local modules
from photoshop import Session

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def trim_document(psd_file: str) -> NoReturn:
    """Trim the transparent pixels from edges of the document.

    This function opens a PSD file and trims transparent pixels from all edges
    (top, left, bottom, right) using the top-left pixel as the base color.

    Args:
        psd_file: Path to the PSD file to trim.

    Raises:
        Exception: If there's an error during the trim operation.
    """
    try:
        with Session(psd_file, action="open") as ps:
            # Trim transparent pixels from all edges using top-left pixel color
            ps.active_document.trim(
                ps.TrimType.TopLeftPixel,  # Use top-left pixel color as base
                True,  # Trim top
                True,  # Trim left
                True,  # Trim bottom
                True,  # Trim right
            )
            logger.info("Successfully trimmed document: %s", psd_file)
    except Exception as e:
        logger.error("Failed to trim document: %s", str(e))
        raise


def main() -> NoReturn:
    """Main function to demonstrate the trim operation."""
    try:
        psd_files = psd.get_psd_files()
        example_file = psd_files["trim.psd"]
        trim_document(example_file)
    except Exception as e:
        logger.error("Failed to process file: %s", str(e))
        raise


if __name__ == "__main__":
    main()
