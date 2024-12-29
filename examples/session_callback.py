"""Example script demonstrating how to use session callbacks in Photoshop.

This script shows how to:
1. Create and use session callbacks
2. Monitor document changes
3. Handle document events
4. Log document operations
"""

# Import built-in modules
from __future__ import annotations

import logging
from typing import Any

# Import local modules
from photoshop import Session
import photoshop.api as ps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def log_document_info(ps_session: Any) -> None:
    """Log information about the current document.

    Args:
        ps_session: Active Photoshop session.
    """
    try:
        doc = ps_session.active_document
        logger.info("Active document: %s", doc.name)
        logger.info("Document size: %dx%d", doc.width, doc.height)
        logger.info("Number of layers: %d", len(doc.layers))
        logger.info("Color mode: %s", doc.mode)
        logger.info("Resolution: %d dpi", doc.resolution)
    except Exception as e:
        logger.error("Failed to log document info: %s", str(e))


def create_test_document(ps_session: Any) -> None:
    """Create a test document with some basic content.

    Args:
        ps_session: Active Photoshop session.
    """
    try:
        app = ps_session.app
        doc = app.documents.add(
            width=800,
            height=600,
            resolution=300,
            name="TestDocument",
        )
        
        # Add a text layer
        text_layer = doc.artLayers.add()
        text_layer.kind = ps.LayerKind.TextLayer
        text_layer.textItem.contents = "Hello Photoshop!"
        text_layer.textItem.position = [100, 100]
        text_layer.textItem.size = 48
        
        logger.info("Created test document with text layer")
        
    except Exception as e:
        logger.error("Failed to create test document: %s", str(e))


def monitor_document_changes(ps_session: Any) -> None:
    """Monitor and log document changes.

    Args:
        ps_session: Active Photoshop session.
    """
    try:
        doc = ps_session.active_document
        logger.info("Document '%s' modified:", doc.name)
        log_document_info(ps_session)
    except Exception as e:
        logger.error("Failed to monitor document changes: %s", str(e))


def session_callback(ps_session: Any) -> None:
    """Main session callback function.

    This function is called when the session is initialized.
    It can be used to set up event handlers and perform initial tasks.

    Args:
        ps_session: Active Photoshop session.
    """
    try:
        # Create a test document
        create_test_document(ps_session)
        
        # Log initial document info
        log_document_info(ps_session)
        
        # Show a message to the user
        ps_session.echo("Session initialized successfully!")
        ps_session.alert("Test document created. Check the console for details.")
        
    except Exception as e:
        logger.error("Session callback failed: %s", str(e))
        ps_session.alert("Error in session callback. Check the console for details.")


def main() -> None:
    """Main function demonstrating session callback usage."""
    try:
        # Initialize session with callback
        with Session(callback=session_callback) as ps:
            # The session_callback will be called automatically
            # Additional operations can be performed here
            monitor_document_changes(ps)
            
    except Exception as e:
        logger.error("Session failed: %s", str(e))
        raise


if __name__ == "__main__":
    try:
        logger.info("Starting session callback example...")
        main()
        logger.info("Session callback example completed successfully")
    except Exception as e:
        logger.error("Session callback example failed: %s", str(e))
        raise
