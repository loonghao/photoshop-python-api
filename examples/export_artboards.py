"""Example of how to export artboards from a PSD file.

This script demonstrates how to:
1. Identify artboard layers in a PSD file
2. Export each artboard as a separate image
"""
import os.path
from pathlib import Path
from typing import List, Union

from photoshop import Session
from photoshop.api._artlayer import ArtLayer
from photoshop.api._layerSet import LayerSet
from photoshop.api.enumerations import LayerKind


def is_artboard(layer: Union[ArtLayer, LayerSet], ps) -> bool:
    """Check if a layer is an artboard.
    
    Args:
        layer: Photoshop layer object (ArtLayer or LayerSet)
        ps: Photoshop session object
        
    Returns:
        bool: True if the layer is an artboard, False otherwise
    """
    try:
        # Get the active document
        doc = ps.active_document
        
        # Select the layer
        doc.activeLayer = layer
        
        # Check if it's an artboard by checking its bounds and artboard property
        js_code = """
        var layer = app.activeDocument.activeLayer;
        try {
            var ref = new ActionReference();
            ref.putEnumerated(charIDToTypeID("Lyr "), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
            var desc = executeActionGet(ref);
            var hasArtboard = desc.hasKey(stringIDToTypeID("artboardEnabled"));
            hasArtboard && desc.getBoolean(stringIDToTypeID("artboardEnabled"));
        } catch(e) {
            false;
        }
        """
        result = ps.app.eval_javascript(js_code)
        return result.lower() == "true"
    except Exception as e:
        print(f"Error checking layer {layer.name}: {str(e)}")
        # Fallback to checking layer name
        return "Artboard" in layer.name


def get_all_layers(doc) -> List[Union[ArtLayer, LayerSet]]:
    """Recursively get all layers from document, including nested layers.
    
    Args:
        doc: Photoshop document object
        
    Returns:
        List[Union[ArtLayer, LayerSet]]: List of all layers
    """
    def _get_layers(layer_container) -> List[Union[ArtLayer, LayerSet]]:
        layers = []
        
        # Get art layers
        for layer in layer_container.artLayers:
            layers.append(layer)
            
        # Get layer sets and their children
        for layer_set in layer_container.layerSets:
            layers.append(layer_set)
            layers.extend(_get_layers(layer_set))
            
        return layers
    
    return _get_layers(doc)


def get_artboard_layers(doc, artboard_name: str) -> List[Union[ArtLayer, LayerSet]]:
    """Get all layers that belong to an artboard.
    
    Args:
        doc: Photoshop document object
        artboard_name: Name of the artboard
        
    Returns:
        List[Union[ArtLayer, LayerSet]]: List of layers that belong to this artboard
    """
    try:
        # Get all layers in the document
        all_layers = []
        for layer in doc.artLayers:
            all_layers.append(layer)
        for layer in doc.layerSets:
            all_layers.append(layer)
            
        # Get the artboard layer
        artboard = None
        for layer in all_layers:
            if layer.name == artboard_name:
                artboard = layer
                break
                
        if not artboard:
            return []
            
        # Get all layers that belong to this artboard
        artboard_layers = []
        for layer in all_layers:
            if layer.name != artboard_name:
                try:
                    # Check if layer is visible and within artboard bounds
                    if layer.visible and isinstance(layer, ArtLayer):
                        artboard_layers.append(layer)
                except Exception as e:
                    print(f"Error checking layer {layer.name}: {str(e)}")
                    continue
        
        return artboard_layers
    except Exception as e:
        print(f"Error getting artboard layers: {str(e)}")
        return []


def export_artboards(psd_path: str, output_dir: str) -> None:
    """Export all artboards in a PSD file as separate images.
    
    Args:
        psd_path (str): Path to the PSD file
        output_dir (str): Directory to save the exported images
    """
    with Session() as ps:
        try:
            # Open the PSD file
            ps.app.open(os.path.abspath(psd_path))
            doc = ps.active_document
            
            # Create output directory if it doesn't exist
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            # Get all layers including nested ones
            all_layers = get_all_layers(doc)
            print(f"Found {len(all_layers)} total layers:")
            for layer in all_layers:
                layer_type = "LayerSet" if isinstance(layer, LayerSet) else "ArtLayer"
                is_ab = "Artboard" if is_artboard(layer, ps) else "Regular Layer"
                print(f"Layer: {layer.name} ({layer_type} - {is_ab})")
            
            # Iterate through all layers
            for layer in all_layers:
                if is_artboard(layer, ps):
                    print(f"\nProcessing artboard: {layer.name}")
                    
                    # Export artboard using JavaScript
                    output_path = os.path.abspath(str(Path(output_dir) / f"{layer.name}.png"))
                    # Convert Windows path to JavaScript path format
                    js_path = output_path.replace("\\", "/")
                    
                    js_code = """
                    function exportArtboard(filePath, artboardName) {
                        var doc = app.activeDocument;
                        var artboard = null;
                        
                        // Find the artboard
                        for (var i = 0; i < doc.layers.length; i++) {
                            if (doc.layers[i].name === '%s') {
                                artboard = doc.layers[i];
                                break;
                            }
                        }
                        
                        if (!artboard) return;
                        
                        // Save the current state
                        var docState = doc.activeHistoryState;
                        
                        try {
                            // Hide all layers
                            for (var i = 0; i < doc.layers.length; i++) {
                                doc.layers[i].visible = false;
                            }
                            
                            // Show only the artboard and its contents
                            artboard.visible = true;
                            
                            // Save as PNG
                            var pngFile = new File('%s');
                            var pngOptions = new PNGSaveOptions();
                            pngOptions.interlaced = false;
                            pngOptions.compression = 9;
                            pngOptions.transparency = true;
                            
                            doc.saveAs(pngFile, pngOptions, true, Extension.LOWERCASE);
                            
                            // Restore the document state
                            doc.activeHistoryState = docState;
                        } catch (e) {
                            // Restore the document state in case of error
                            doc.activeHistoryState = docState;
                            throw e;
                        }
                    }
                    
                    exportArtboard('%s', '%s');
                    """ % (layer.name, js_path, js_path, layer.name)
                    
                    ps.app.eval_javascript(js_code)
                    print(f"Exported {layer.name} to {output_path}")
                    
        except Exception as e:
            print(f"Error processing PSD file: {str(e)}")
            raise


if __name__ == "__main__":
    # Example usage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    psd_path = os.path.join(current_dir, "files", "artboard_example.psd")  # Use absolute path
    output_dir = os.path.join(current_dir, "output", "artboards")  # Use absolute path
    export_artboards(psd_path, output_dir)
