"""Layer movement management in Photoshop.

This script demonstrates how to:
1. Move layers between groups
2. Reorder layers within groups
3. Move layers to top/bottom of stack
4. Get layer position information
"""

from __future__ import annotations

from enum import Enum, auto

import photoshop.api as ps

class MoveTarget(Enum):
    """Layer movement targets."""
    TOP = auto()  # Move to top of document/group
    BOTTOM = auto()  # Move to bottom of document/group
    ABOVE = auto()  # Move above target layer
    BELOW = auto()  # Move below target layer
    INTO = auto()  # Move into target group

def main() -> None:
    """Layer movement example."""
    try:
        # Initialize Photoshop
        app = ps.Application()
        
        print("\n=== Creating Document ===")
        # Create test document
        doc = app.documents.add(name="Layer Movement Example")
        print("Created document:", doc.name)
        
        print("\n=== Creating Layers ===")
        # Create group
        group = doc.layerSets.add()
        group.name = "Test Group"
        print("Created group:", group.name)
        
        # Create layers
        layer1 = group.artLayers.add()
        layer1.name = "Layer 1"
        print("Created layer:", layer1.name)
        
        layer2 = doc.artLayers.add()
        layer2.name = "Layer 2"
        print("Created layer:", layer2.name)
        
        layer3 = doc.artLayers.add()
        layer3.name = "Layer 3"
        print("Created layer:", layer3.name)
        
        # Move layers
        print("\n=== Moving Layers ===")
        
        # Move Layer 2 into group
        print("\nMoving Layer 2 into group:")
        layer2.moveToEnd(group)
        print("Successfully moved Layer 2 into Test Group")
        
        # Move Layer 3 above Layer 1
        print("\nMoving Layer 3 above Layer 1:")
        layer3.move(layer1, ps.ElementPlacement.PlaceAfter)
        print("Successfully moved Layer 3 above Layer 1")
        
        # Move Layer 2 to bottom of group
        print("\nMoving Layer 2 to bottom of group:")
        layer2.moveToEnd(group)
        print("Successfully moved Layer 2 to bottom")
        
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
