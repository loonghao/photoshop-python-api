"""Example of executing JavaScript code in Photoshop.

This script demonstrates how to:
1. Execute JavaScript code in Photoshop
2. Handle JavaScript execution results
3. Work with Photoshop objects through JavaScript
4. Handle errors in JavaScript execution
"""

from __future__ import annotations

import os
from typing import Any, Optional

from photoshop import Session

def execute_javascript(ps: Session, js_code: str) -> Optional[Any]:
    """Execute JavaScript code in Photoshop.
    
    Args:
        ps: Photoshop session instance
        js_code: JavaScript code to execute
        
    Returns:
        Optional[Any]: Result of JavaScript execution if successful, None otherwise
    """
    try:
        # Add error handling wrapper
        wrapped_code = f"""
        try {{
            {js_code}
        }} catch(e) {{
            "Error: " + e.message
        }}
        """
        result = ps.app.doJavaScript(wrapped_code)
        
        # Check if result is an error message
        if isinstance(result, str) and result.startswith("Error: "):
            print(f"JavaScript execution error: {result[7:]}")
            return None
            
        return result
    except Exception as e:
        print(f"Error executing JavaScript: {e}")
        return None

def get_document_info(ps: Session) -> Optional[dict[str, Any]]:
    """Get information about the active document.
    
    Args:
        ps: Photoshop session instance
        
    Returns:
        Optional[dict[str, Any]]: Document information if successful, None otherwise
    """
    js_code = """
    // Get active document info
    var doc = app.activeDocument;
    var info = {};
    info.name = doc.name;
    info.width = doc.width.value;
    info.height = doc.height.value;
    info.resolution = doc.resolution;
    info.mode = doc.mode.toString();
    info.layerCount = doc.layers.length;
    info.saved = doc.saved;
    
    if (doc.saved && doc.fullName) {
        info.path = doc.fullName.fsName;
    }
    
    // Convert info object to string
    var result = "";
    for (var key in info) {
        if (info.hasOwnProperty(key)) {
            result += key + ":" + info[key] + "\\n";
        }
    }
    result
    """
    result = execute_javascript(ps, js_code)
    if result:
        try:
            # Parse the result string into a dictionary
            info = {}
            for line in result.strip().split("\n"):
                key, value = line.split(":", 1)
                info[key] = value
            return info
        except Exception as e:
            print(f"Error parsing document info: {e}")
    return None

def modify_document(ps: Session, new_name: Optional[str] = None) -> bool:
    """Modify the active document.
    
    Args:
        ps: Photoshop session instance
        new_name: New name for the document (optional)
        
    Returns:
        bool: True if modification was successful, False otherwise
    """
    if new_name:
        js_code = f"""
        // Modify document
        var doc = app.activeDocument;
        doc.name = "{new_name}";
        "success"
        """
        result = execute_javascript(ps, js_code)
        return result == "success"
    return False

def create_text_layer(ps: Session, text: str, font_size: int = 72) -> bool:
    """Create a text layer in the active document.
    
    Args:
        ps: Photoshop session instance
        text: Text content
        font_size: Font size in points
        
    Returns:
        bool: True if text layer was created successfully, False otherwise
    """
    js_code = f"""
    // Create text layer
    var doc = app.activeDocument;
    var layer = doc.artLayers.add();
    layer.kind = LayerKind.TEXT;
    var textItem = layer.textItem;
    textItem.contents = "{text}";
    textItem.size = {font_size};
    textItem.position = [doc.width.value/2, doc.height.value/2];
    textItem.justification = Justification.CENTER;
    layer.name = "Python Text Layer";
    "success"
    """
    result = execute_javascript(ps, js_code)
    return result == "success"

def save_document(ps: Session, file_path: str) -> bool:
    """Save the active document.
    
    Args:
        ps: Photoshop session instance
        file_path: Path to save the document
        
    Returns:
        bool: True if document was saved successfully, False otherwise
    """
    js_code = f"""
    try {{
        var doc = app.activeDocument;
        var file = new File("{file_path}");
        var opts = new PhotoshopSaveOptions();
        doc.saveAs(file, opts, true);
        "success"
    }} catch(e) {{
        e.message
    }}
    """
    result = execute_javascript(ps, js_code)
    return result == "success"

def main() -> None:
    """Demonstrate JavaScript execution in Photoshop.
    
    This function shows how to:
    1. Get document information
    2. Modify document properties
    3. Create text layers
    4. Save documents
    5. Handle errors
    """
    with Session() as ps:
        try:
            # Create a new document if none exists
            js_code = """
            if (!app.documents.length) {
                app.documents.add(800, 600, 72, "JavaScript Demo");
            }
            "success"
            """
            if execute_javascript(ps, js_code) != "success":
                print("Failed to create or verify document")
                return
            
            # Get initial document info
            print("\nInitial Document Information:")
            doc_info = get_document_info(ps)
            if doc_info:
                for key, value in doc_info.items():
                    print(f"{key}: {value}")
            
            # Modify document
            if modify_document(ps, "Modified Document"):
                print("\nDocument renamed successfully")
            
            # Create text layer
            if create_text_layer(ps, "Hello from Python!", 72):
                print("Text layer created successfully")
            
            # Save document
            temp_dir = os.path.join(os.environ.get("TEMP", ""), "photoshop_demo")
            os.makedirs(temp_dir, exist_ok=True)
            file_path = os.path.join(temp_dir, "javascript_demo.psd")
            
            if save_document(ps, file_path.replace("\\", "/")):
                print(f"\nDocument saved to: {file_path}")
                
                # Get final document info
                print("\nFinal Document Information:")
                doc_info = get_document_info(ps)
                if doc_info:
                    for key, value in doc_info.items():
                        print(f"{key}: {value}")
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
