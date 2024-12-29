"""Example of working with Photoshop tools.

This example demonstrates how to:
1. Get the current active tool
2. Change tools programmatically
3. Configure tool options
4. Work with tool presets

Key concepts:
- Tool selection
- Tool properties
- Tool management
- Active tool state
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Get current tool
    current = ps.app.currentTool
    
    # Print current tool name
    ps.echo(f"Current tool: {current}")
