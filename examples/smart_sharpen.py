"""Example of applying Smart Sharpen filter in Photoshop.

This example demonstrates how to:
1. Apply Smart Sharpen filter with various settings
2. Configure sharpening parameters
3. Handle different sharpening methods
4. Process multiple layers

Key concepts:
- Smart Sharpen filter
- Filter parameters
- Image enhancement
- Layer processing
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    layer = doc.activeLayer
    
    # Configure Smart Sharpen options
    options = ps.SmartSharpenOptions()
    options.amount = 100.0
    options.radius = 3.0
    options.noiseReduction = 20
    options.removeMotionBlur = False
    options.angle = 0
    options.moreAccurate = True
    
    # Apply Smart Sharpen
    layer.applySmartSharpen(
        amount=options.amount,
        radius=options.radius,
        noiseReduction=options.noiseReduction,
        removeMotionBlur=options.removeMotionBlur,
        angle=options.angle,
        moreAccurate=options.moreAccurate
    )
    
    # Create a copy with different settings
    new_layer = layer.duplicate()
    new_layer.name = "Sharp Copy"
    
    # Apply stronger sharpening
    options.amount = 150.0
    options.radius = 4.0
    new_layer.applySmartSharpen(
        amount=options.amount,
        radius=options.radius,
        noiseReduction=options.noiseReduction,
        removeMotionBlur=options.removeMotionBlur,
        angle=options.angle,
        moreAccurate=options.moreAccurate
    )
