"""Photoshop session management and template processing.

This script demonstrates how to:
1. Manage Photoshop sessions
2. Open and process template files
3. Replace text content dynamically
4. Export files in different formats
5. Handle session errors
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from tempfile import mkdtemp
from typing import Any, Dict, Optional, Union

import examples._psd_files as psd  # Import from examples
import photoshop.api as ps
from photoshop import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class ExportFormat(Enum):
    """Export file formats."""
    JPEG = auto()  # JPEG format
    PNG = auto()   # PNG format
    PSD = auto()   # PSD format
    TIFF = auto()  # TIFF format
    PDF = auto()   # PDF format

@dataclass
class SaveOptions:
    """Save options for different formats."""
    format: ExportFormat  # Export format
    quality: int = 100  # Quality (1-100, for JPEG)
    compression: bool = True  # Use compression
    layers: bool = True  # Preserve layers
    icc_profile: bool = True  # Include ICC profile
    resolution: float = 72.0  # Resolution in DPI

class SessionManager:
    """Class for managing Photoshop sessions and templates."""
    
    def __init__(self, template_path: Optional[str] = None) -> None:
        """Initialize session manager.
        
        Args:
            template_path: Path to template file
        """
        self.template_path = template_path
        self.session: Optional[Session] = None
        self.doc: Optional[ps.Document] = None
    
    def __enter__(self) -> SessionManager:
        """Enter context manager."""
        self.start_session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager."""
        self.close_session()
    
    def start_session(self) -> None:
        """Start Photoshop session."""
        try:
            if self.template_path:
                self.session = Session(
                    self.template_path,
                    action="open",
                    auto_close=True,
                )
            else:
                self.session = Session(action="new_document")
            
            self.session.__enter__()
            self.doc = self.session.active_document
            logger.info("Started Photoshop session")
            
        except Exception as e:
            logger.error(f"Error starting session: {e}")
            raise
    
    def close_session(self) -> None:
        """Close Photoshop session."""
        try:
            if self.session:
                self.session.__exit__(None, None, None)
                logger.info("Closed Photoshop session")
            
        except Exception as e:
            logger.error(f"Error closing session: {e}")
            raise
    
    def get_layer_set(self, name: str) -> Optional[ps.LayerSet]:
        """Get layer set by name.
        
        Args:
            name: Layer set name
            
        Returns:
            Layer set if found, None otherwise
        """
        try:
            if not self.doc:
                return None
            
            return self.doc.layerSets.getByName(name)
            
        except Exception as e:
            logger.error(f"Error getting layer set '{name}': {e}")
            return None
    
    def replace_text_content(self, 
                           layer_set_name: str,
                           data: Dict[str, Any]) -> bool:
        """Replace text content in template.
        
        Args:
            layer_set_name: Layer set name
            data: Replacement data
            
        Returns:
            True if successful
        """
        try:
            layer_set = self.get_layer_set(layer_set_name)
            if not layer_set:
                logger.error(f"Layer set '{layer_set_name}' not found")
                return False
            
            for layer in layer_set.layers:
                if layer.kind == self.session.LayerKind.TextLayer:
                    key = layer.textItem.contents.strip()
                    if key in data:
                        layer.textItem.contents = str(data[key])
            
            logger.info("Replaced text content successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error replacing text content: {e}")
            return False
    
    def save_as_jpeg(self, file_path: Union[str, Path], quality: int = 90) -> bool:
        """Save document as JPEG.
        
        Args:
            file_path: Output file path
            quality: JPEG quality (1-100)
            
        Returns:
            True if successful
        """
        try:
            if not self.doc or not self.session:
                logger.error("No active document or session")
                return False
            
            # Ensure output directory exists
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert path to Photoshop format (forward slashes)
            ps_path = str(file_path).replace("\\", "/")
            
            # Create JavaScript code for export
            js_code = """
            try {
                var doc = app.activeDocument;
                var file = new File("PATH");
                var opts = new ExportOptionsSaveForWeb();
                opts.format = SaveDocumentType.JPEG;
                opts.includeProfile = true;
                opts.quality = QUALITY;
                opts.optimized = true;
                doc.exportDocument(file, ExportType.SAVEFORWEB, opts);
                $.writeln("JPEG exported successfully");
            } catch(e) {
                $.writeln("Error: " + e);
            }
            """
            
            # Replace placeholders
            js_code = js_code.replace("PATH", ps_path)
            js_code = js_code.replace("QUALITY", str(quality))
            
            # Execute JavaScript code
            logger.info(f"Saving JPEG with quality {quality} to: {file_path}")
            result = self.session.app.doJavaScript(js_code)
            logger.info(f"JavaScript result: {result}")
            
            if os.path.exists(file_path):
                logger.info("Save successful")
                return True
            logger.error("Save failed: File not created")
            return False
            
        except Exception as e:
            logger.error(f"Error saving JPEG: {e}")
            return False
    
    def save_as_psd(self, file_path: Union[str, Path]) -> bool:
        """Save document as PSD.
        
        Args:
            file_path: Output file path
            
        Returns:
            True if successful
        """
        try:
            if not self.doc or not self.session:
                logger.error("No active document or session")
                return False
            
            # Ensure output directory exists
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create save options
            save_options = self.session.PhotoshopSaveOptions()
            save_options.alphaChannels = True
            save_options.layers = True
            save_options.spotColors = True
            
            # Save file
            logger.info(f"Saving PSD to: {file_path}")
            self.doc.saveAs(str(file_path), save_options)
            logger.info("Save successful")
            return True
            
        except Exception as e:
            logger.error(f"Error saving PSD: {e}")
            return False

def main() -> None:
    """Template processing example."""
    try:
        # Get template file
        template_path = psd.get_psd_files()["slate_template.psd"]
        
        # Create output directory
        output_dir = Path(mkdtemp("photoshop-python-api"))
        logger.info(f"Created output directory: {output_dir}")
        
        # Prepare replacement data
        data = {
            "project name": "Test Project",
            "datetime": datetime.today().strftime("%Y-%m-%d"),
        }
        
        # Process template
        with SessionManager(template_path) as manager:
            print("\n=== Template Processing ===")
            
            # Replace text content
            print("\nReplacing text content:")
            if manager.replace_text_content("template", data):
                print("Text content replaced successfully")
            
            # Save as JPEG
            print("\nSaving as JPEG:")
            jpg_path = output_dir / "slate.jpg"
            if manager.save_as_jpeg(jpg_path, quality=90):
                print(f"Saved JPEG to: {jpg_path}")
                os.startfile(str(jpg_path))
            
            # Save as PSD
            print("\nSaving as PSD:")
            psd_path = output_dir / "slate.psd"
            if manager.save_as_psd(psd_path):
                print(f"Saved PSD to: {psd_path}")
            
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
