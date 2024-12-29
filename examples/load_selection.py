"""Example of loading and working with selections in Photoshop.

This example demonstrates how to:
1. Create and save selections
2. Load saved selections
3. Modify selection channels
4. Combine multiple selections

Key concepts:
- Selection channels
- Channel operations
- Selection saving/loading
- Selection modification
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # Create initial selection
    doc.selection.select([
        [100, 100],
        [300, 100],
        [300, 300],
        [100, 300]
    ])
    
    # Save selection to channel
    doc.channels.add()
    doc.selection.store(doc.channels[-1])
    
    # Deselect everything
    doc.selection.deselect()
    
    # Create another selection
    doc.selection.select([
        [200, 200],
        [400, 200],
        [400, 400],
        [200, 400]
    ])
    
    # Save to another channel
    doc.channels.add()
    doc.selection.store(doc.channels[-1])
    
    # Load first selection
    doc.selection.load(doc.channels[-2])
    
    # Combine with second selection
    doc.selection.combine(doc.channels[-1], ps.SelectionType.ExtendSelection)
    
    # Clean up - delete added channels
    doc.channels[-1].remove()
    doc.channels[-1].remove()
