"""Example of executing JavaScript code in Photoshop.

This example demonstrates how to:
1. Execute JavaScript commands
2. Interact with Photoshop's scripting engine
3. Handle JavaScript results
4. Pass data between Python and JavaScript

Key concepts:
- JavaScript execution
- Script integration
- Data exchange
- Command execution
"""

# Import local modules
from photoshop import Session


with Session() as ps:
    # Execute JavaScript command
    js_code = "app.documents.length"
    result = ps.app.eval_javascript(js_code)
    ps.echo(f"Number of open documents: {result}")
