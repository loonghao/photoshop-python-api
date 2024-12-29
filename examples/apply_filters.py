"""Example of applying various filters to layers in Photoshop.

This example demonstrates how to:
1. Apply different types of Photoshop filters
2. Configure filter parameters
3. Work with filter options
4. Handle filter application to different layer types

Key concepts:
- Filter types and options
- Layer filtering
- Parameter configuration
- Filter effects management
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    layer = doc.activeLayer
    
    # Apply Gaussian Blur filter
    filter_options = ps.GaussianBlurOptions()
    filter_options.radius = 10.0
    layer.applyGaussianBlur(filter_options)
    
    # Create new layer for other filters
    new_layer = doc.artLayers.add()
    
    # Apply Motion Blur
    motion_options = ps.MotionBlurOptions()
    motion_options.angle = 45
    motion_options.distance = 20
    new_layer.applyMotionBlur(motion_options)
    
    # Apply Smart Sharpen
    sharpen_options = ps.SmartSharpenOptions()
    sharpen_options.amount = 100
    sharpen_options.radius = 3.0
    sharpen_options.noiseReduction = 20
    new_layer.applySmartSharpen(sharpen_options)
    
    # Apply Unsharp Mask
    unsharp_options = ps.UnsharpMaskOptions()
    unsharp_options.amount = 50
    unsharp_options.radius = 2.0
    unsharp_options.threshold = 0
    new_layer.applyUnsharpMask(unsharp_options)
