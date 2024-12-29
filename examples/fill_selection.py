"""Fill selections in a Photoshop document with various colors and blend modes.

This script demonstrates how to:
1. Create and manage document selections
2. Fill selections with colors
3. Use different blend modes
4. Handle document and layer states
5. Handle errors and exceptions
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Tuple, Union

from photoshop import Session

class ColorPreset(Enum):
    """Predefined color presets."""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

@dataclass
class DocumentSettings:
    """Settings for creating new documents."""
    width: int = 800
    height: int = 600
    resolution: float = 72.0
    name: Optional[str] = None
    mode: Optional[str] = None
    initial_fill: Optional[str] = None
    color_profile: Optional[str] = None
    bit_depth: Optional[int] = None
    pixel_aspect: Optional[float] = None

class SelectionFiller:
    """Class for filling selections in Photoshop documents."""
    
    def __init__(self, ps: Session) -> None:
        """Initialize the selection filler.
        
        Args:
            ps: Photoshop session instance
        """
        self.ps = ps
        self._original_ruler_units = ps.app.preferences.rulerUnits
        self._layer_count = 0
    
    def _set_ruler_units(self, units: Any) -> None:
        """Set ruler units temporarily.
        
        Args:
            units: Ruler units to set
        """
        self.ps.app.preferences.rulerUnits = units
    
    def _restore_ruler_units(self) -> None:
        """Restore original ruler units."""
        self.ps.app.preferences.rulerUnits = self._original_ruler_units
    
    def create_new_layer(self, name: Optional[str] = None) -> bool:
        """Create a new layer.
        
        Args:
            name: Name for the new layer
            
        Returns:
            bool: True if layer was created successfully
        """
        try:
            # Create layer name if not provided
            if not name:
                self._layer_count += 1
                name = f"Fill Layer {self._layer_count}"
            
            # Create layer using JavaScript
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                var layer = doc.artLayers.add();
                layer.name = "{name}";
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            
            if result == "success":
                print(f"Created new layer: {name}")
                return True
            print(f"Error creating layer: {result}")
            return False
            
        except Exception as e:
            print(f"Error creating layer: {e}")
            return False
    
    def ensure_document_exists(self, settings: Optional[DocumentSettings] = None) -> None:
        """Ensure a document exists, create one if needed.
        
        Args:
            settings: Document settings to use when creating new document
        """
        if len(self.ps.app.documents) < 1:
            if not settings:
                settings = DocumentSettings()
            
            # Set units to pixels temporarily
            original_units = self.ps.app.preferences.rulerUnits
            self._set_ruler_units(self.ps.Units.Pixels)
            
            try:
                # Create new document
                doc = self.ps.app.documents.add(
                    settings.width,
                    settings.height,
                    settings.resolution,
                    settings.name,
                    self.ps.NewDocumentMode.NewRGB,
                    self.ps.DocumentFill.White,
                )
                
                # Create initial selection
                self.create_initial_selection()
                
            finally:
                # Restore original units
                self._restore_ruler_units()
    
    def create_initial_selection(self) -> None:
        """Create an initial rectangular selection in the document."""
        try:
            doc = self.ps.active_document
            
            # Get document dimensions
            width = doc.width
            height = doc.height
            
            # Create selection array (25% margin from edges)
            left = int(width * 0.25)
            top = int(height * 0.25)
            right = int(width * 0.75)
            bottom = int(height * 0.75)
            
            # Create selection using JavaScript
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                var region = [
                    [{left}, {top}],
                    [{right}, {top}],
                    [{right}, {bottom}],
                    [{left}, {bottom}]
                ];
                doc.selection.select(region);
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            
            if result == "success":
                print(f"Created selection: ({left}, {top}, {right}, {bottom})")
            else:
                print(f"Warning: Error creating selection: {result}")
            
        except Exception as e:
            print(f"Warning: Error creating initial selection: {e}")
    
    def create_solid_color(self, color: Union[ColorPreset, Tuple[int, int, int]]) -> Any:
        """Create a solid color object.
        
        Args:
            color: Color preset or RGB tuple
            
        Returns:
            SolidColor object
        """
        if isinstance(color, ColorPreset):
            rgb = color.value
        else:
            rgb = color
            
        fill_color = self.ps.SolidColor()
        fill_color.rgb.red = rgb[0]
        fill_color.rgb.green = rgb[1]
        fill_color.rgb.blue = rgb[2]
        return fill_color
    
    def ensure_selection_exists(self) -> bool:
        """Ensure a selection exists, create one if needed.
        
        Returns:
            bool: True if selection exists or was created
        """
        try:
            # Check selection using JavaScript
            js_code = """
            try {
                var doc = app.activeDocument;
                var bounds = doc.selection.bounds;
                bounds[0] + "," + bounds[1] + "," + bounds[2] + "," + bounds[3]
            } catch(e) {
                "no_selection"
            }
            """
            result = self.ps.app.doJavaScript(js_code)
            
            if result == "no_selection":
                print("No existing selection found, creating new one...")
                self.create_initial_selection()
                return True
            print(f"Found existing selection: {result}")
            return True
            
        except Exception as e:
            print(f"Error checking selection: {e}")
            return False
    
    def fill_selection(self, 
                      color: Union[ColorPreset, Tuple[int, int, int]], 
                      blend_mode: Optional[Any] = None,
                      opacity: float = 100.0,
                      preserve_transparency: bool = False) -> bool:
        """Fill the current selection with a color.
        
        Args:
            color: Color to fill with (preset or RGB tuple)
            blend_mode: Blend mode to use
            opacity: Fill opacity (0-100)
            preserve_transparency: Whether to preserve transparency
            
        Returns:
            bool: True if fill was successful
        """
        try:
            doc = self.ps.active_document
            
            # Create new layer for fill
            if not self.create_new_layer():
                print("Error: Could not create new layer")
                return False
            
            # Ensure we have a selection
            if not self.ensure_selection_exists():
                print("Error: Could not create or find selection")
                return False
            
            # Create fill color
            fill_color = self.create_solid_color(color)
            
            # Fill selection using JavaScript
            js_code = f"""
            try {{
                var doc = app.activeDocument;
                var color = new SolidColor();
                color.rgb.red = {fill_color.rgb.red};
                color.rgb.green = {fill_color.rgb.green};
                color.rgb.blue = {fill_color.rgb.blue};
                
                // Create action for fill
                var idFl = charIDToTypeID("Fl  ");
                var desc = new ActionDescriptor();
                var idUsng = charIDToTypeID("Usng");
                var idFlCn = charIDToTypeID("FlCn");
                var idClr = charIDToTypeID("Clr ");
                desc.putEnumerated(idUsng, idFlCn, idClr);
                
                var idClr = charIDToTypeID("Clr ");
                var desc2 = new ActionDescriptor();
                var idRd = charIDToTypeID("Rd  ");
                var idPrct = charIDToTypeID("#Prc");
                desc2.putDouble(idRd, {fill_color.rgb.red});
                var idGrn = charIDToTypeID("Grn ");
                desc2.putDouble(idGrn, {fill_color.rgb.green});
                var idBl = charIDToTypeID("Bl  ");
                desc2.putDouble(idBl, {fill_color.rgb.blue});
                var idRGBC = charIDToTypeID("RGBC");
                desc.putObject(idClr, idRGBC, desc2);
                
                var idOpct = charIDToTypeID("Opct");
                var idPrc = charIDToTypeID("#Prc");
                desc.putUnitDouble(idOpct, idPrc, {opacity});
                
                var idMd = charIDToTypeID("Md  ");
                var idBlnM = charIDToTypeID("BlnM");
                var idNrml = charIDToTypeID("Nrml");
                desc.putEnumerated(idMd, idBlnM, idNrml);
                
                executeAction(idFl, desc, DialogModes.NO);
                "success"
            }} catch(e) {{
                e.message
            }}
            """
            result = self.ps.app.doJavaScript(js_code)
            
            if result == "success":
                print(f"Successfully filled selection with color RGB({fill_color.rgb.red}, {fill_color.rgb.green}, {fill_color.rgb.blue})")
                return True
            print(f"Error during fill operation: {result}")
            return False
            
        except Exception as e:
            print(f"Error filling selection: {e}")
            return False
    
    def fill_with_preset(self, 
                        preset: ColorPreset,
                        blend_mode: Optional[Any] = None,
                        opacity: float = 100.0) -> bool:
        """Fill the current selection with a preset color.
        
        Args:
            preset: Color preset to use
            blend_mode: Blend mode to use
            opacity: Fill opacity (0-100)
            
        Returns:
            bool: True if fill was successful
        """
        return self.fill_selection(preset, blend_mode, opacity)

def main() -> None:
    """Fill selections in a Photoshop document."""
    with Session() as ps:
        try:
            # Create filler and ensure document exists
            print("\nInitializing...")
            filler = SelectionFiller(ps)
            filler.ensure_document_exists()
            
            # Fill selection with different colors and blend modes
            print("\nFilling with preset colors...")
            filler.fill_with_preset(ColorPreset.RED, ps.ColorBlendMode.NormalBlendColor, 50)
            
            print("\nFilling with custom colors...")
            custom_color = (128, 64, 255)  # Purple
            filler.fill_selection(
                custom_color,
                ps.ColorBlendMode.MultiplyBlend,
                75,
            )
            
        except Exception as e:
            print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
