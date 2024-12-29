"""Manage document view and zoom in Photoshop.

This script demonstrates how to:
1. Fit document on screen
2. View at actual pixels
3. Zoom in and out
4. Handle different view modes
"""

from __future__ import annotations

import enum

from photoshop import Session

class ViewMode(enum.Enum):
    """View modes for document display."""
    FIT_ON_SCREEN = "FtOn"
    ACTUAL_PIXELS = "ActP"
    PRINT_SIZE = "PrnS"
    ZOOM_IN = "ZmIn"
    ZOOM_OUT = "ZmOt"

class ViewManager:
    """Class for managing document view and zoom."""
    
    def __init__(self, ps: Session) -> None:
        """Initialize the view manager.
        
        Args:
            ps: Photoshop session instance
        """
        self.ps = ps
    
    def ensure_document_exists(self) -> bool:
        """Ensure a document exists.
        
        Returns:
            bool: True if document exists
        """
        try:
            if len(self.ps.app.documents) < 1:
                print("Error: No document is open")
                return False
            return True
        except Exception as e:
            print(f"Error checking document: {e}")
            return False
    
    def set_view_mode(self, mode: ViewMode) -> bool:
        """Set the view mode for the current document.
        
        Args:
            mode: View mode to set
            
        Returns:
            bool: True if view mode was set successfully
        """
        try:
            if not self.ensure_document_exists():
                return False
            
            # Set view mode using runMenuItem
            js_code = f"""
            try {{
                app.runMenuItem(app.charIDToTypeID("{mode.value}"));
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            
            if result == "success":
                print(f"Set view mode to: {mode.name}")
                return True
            print(f"Error setting view mode: {result}")
            return False
            
        except Exception as e:
            print(f"Error setting view mode: {e}")
            return False
    
    def zoom_in(self, steps: int = 1) -> bool:
        """Zoom in by a number of steps.
        
        Args:
            steps: Number of zoom in steps
            
        Returns:
            bool: True if zoom was successful
        """
        try:
            for _ in range(steps):
                if not self.set_view_mode(ViewMode.ZOOM_IN):
                    return False
            return True
        except Exception as e:
            print(f"Error zooming in: {e}")
            return False
    
    def zoom_out(self, steps: int = 1) -> bool:
        """Zoom out by a number of steps.
        
        Args:
            steps: Number of zoom out steps
            
        Returns:
            bool: True if zoom was successful
        """
        try:
            for _ in range(steps):
                if not self.set_view_mode(ViewMode.ZOOM_OUT):
                    return False
            return True
        except Exception as e:
            print(f"Error zooming out: {e}")
            return False
    
    def fit_on_screen(self) -> bool:
        """Fit the document on screen.
        
        Returns:
            bool: True if successful
        """
        return self.set_view_mode(ViewMode.FIT_ON_SCREEN)
    
    def actual_pixels(self) -> bool:
        """View document at actual pixels.
        
        Returns:
            bool: True if successful
        """
        return self.set_view_mode(ViewMode.ACTUAL_PIXELS)

def main() -> None:
    """Demonstrate document view management."""
    with Session() as ps:
        try:
            # Create view manager
            print("\nInitializing view manager...")
            manager = ViewManager(ps)
            
            if not manager.ensure_document_exists():
                print("Please open a document first")
                return
            
            # Try different view modes
            print("\nTesting view modes...")
            manager.fit_on_screen()
            manager.actual_pixels()
            
            # Test zoom in/out
            print("\nTesting zoom in/out...")
            manager.zoom_in(2)
            manager.zoom_out(1)
            
            # Return to fit on screen
            print("\nReturning to fit on screen...")
            manager.fit_on_screen()
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
