"""Example of enabling and managing Photoshop Generator features.

This script demonstrates how to:
1. Enable Generator functionality
2. Configure Generator settings
3. Handle Generator-related errors
"""

from __future__ import annotations


from photoshop import Session

def enable_generator(ps: Session, plugin_name: str = "generator-assets") -> bool:
    """Enable Generator functionality with specified plugin.
    
    Args:
        ps: Photoshop session instance
        plugin_name: Name of the Generator plugin to enable
        
    Returns:
        bool: True if Generator was enabled successfully, False otherwise
    """
    try:
        # Create Generator descriptor
        generator_desc = ps.ActionDescriptor
        generator_desc.putString(ps.app.stringIDToTypeID("name"), plugin_name)
        
        # Execute Generator action
        ps.app.executeAction(ps.app.stringIDToTypeID("generateAssets"), generator_desc)
        print(f"Successfully enabled Generator with plugin: {plugin_name}")
        return True
    except Exception as e:
        print(f"Error enabling Generator: {e}")
        return False

def configure_generator_settings(ps: Session) -> bool:
    """Configure Generator settings using JavaScript.
    
    Args:
        ps: Photoshop session instance
        
    Returns:
        bool: True if settings were configured successfully, False otherwise
    """
    try:
        js_code = """
        try {
            // Configure Generator settings using JavaScript
            app.preferences.rulerUnits = Units.PIXELS;
            app.preferences.typeUnits = TypeUnits.PIXELS;
            app.preferences.exportClipboard = true;
            
            // Configure Generator-specific preferences
            var desc = new ActionDescriptor();
            desc.putBoolean(stringIDToTypeID("svg-enabled"), true);
            desc.putInteger(stringIDToTypeID("jpg-quality"), 90);
            desc.putBoolean(stringIDToTypeID("png-interlaced"), false);
            desc.putBoolean(stringIDToTypeID("use-smart-scaling"), true);
            desc.putBoolean(stringIDToTypeID("include-ancestor-masks"), true);
            app.putCustomOptions("generator-assets-configuration", desc);
            
            "success"
        } catch(e) {
            e.message
        }
        """
        result = ps.app.doJavaScript(js_code)
        if result == "success":
            print("Successfully configured Generator settings")
            return True
        print(f"Error configuring Generator settings: {result}")
        return False
    except Exception as e:
        print(f"Error configuring Generator settings: {e}")
        return False

def main() -> None:
    """Enable and configure Generator functionality.
    
    This function demonstrates how to:
    1. Enable Generator
    2. Configure Generator settings
    """
    with Session() as ps:
        try:
            # Enable Generator
            if enable_generator(ps):
                print("Generator enabled successfully")
                
                # Configure Generator settings
                if configure_generator_settings(ps):
                    print("Generator settings configured successfully")
                else:
                    print("Failed to configure Generator settings")
            else:
                print("Failed to enable Generator")
        
        except Exception as e:
            print(f"Error in Generator management: {e}")

if __name__ == "__main__":
    main()
