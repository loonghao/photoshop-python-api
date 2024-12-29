"""This example demonstrates how to roll back history."""

# Import local modules
from __future__ import annotations

from photoshop import Session

with Session() as ps:
    doc = ps.active_document
    old_state = doc.activeHistoryState
    print(old_state.name)
    doc.artLayers.add()
    last_state = doc.activeHistoryState
    print(last_state.name)
    doc.activeHistoryState = old_state
    print(doc.activeHistoryState.name)
