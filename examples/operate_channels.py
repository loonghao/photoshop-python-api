"""Example of working with channels in Photoshop.

This example demonstrates how to:
1. Access and manipulate color channels
2. Create and modify alpha channels
3. Work with channel visibility
4. Handle channel operations

Key concepts:
- Channel management
- Alpha channels
- Channel visibility
- Color separation
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    doc = ps.active_document
    
    # List all channels
    for channel in doc.channels:
        ps.echo(f"Channel: {channel.name}")
        
    # Create a new alpha channel
    new_channel = doc.channels.add()
    new_channel.name = "Custom Alpha"
    
    # Duplicate a channel
    if len(doc.channels) > 0:
        duplicate = doc.channels[0].duplicate()
        duplicate.name = "Channel Copy"
        
    # Toggle channel visibility
    for channel in doc.channels:
        channel.visible = True
