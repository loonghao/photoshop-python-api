"""Photoshop history state management.

This script demonstrates how to:
1. Manage document history states
2. Save and restore document states
3. Track history state changes
4. Handle history state errors
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List, Optional

import photoshop.api as ps
from photoshop import Session

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

@dataclass
class HistoryState:
    """History state information."""
    name: str
    state: ps.HistoryState
    
    @classmethod
    def from_state(cls, state: ps.HistoryState) -> HistoryState:
        """Create HistoryState from Photoshop history state.
        
        Args:
            state: Photoshop history state
            
        Returns:
            HistoryState object
        """
        return cls(state.name, state)

class HistoryManager:
    """Class for managing Photoshop document history."""
    
    def __init__(self, session: Session) -> None:
        """Initialize history manager.
        
        Args:
            session: Photoshop session
        """
        self.session = session
        self.doc = session.active_document
    
    def get_current_state(self) -> Optional[HistoryState]:
        """Get current history state.
        
        Returns:
            Current history state if exists, None otherwise
        """
        try:
            state = self.doc.activeHistoryState
            return HistoryState.from_state(state)
            
        except Exception as e:
            logger.error(f"Error getting current state: {e}")
            return None
    
    def get_all_states(self) -> List[HistoryState]:
        """Get all history states.
        
        Returns:
            List of history states
        """
        try:
            states = []
            for state in self.doc.historyStates:
                states.append(HistoryState.from_state(state))
            return states
            
        except Exception as e:
            logger.error(f"Error getting history states: {e}")
            return []
    
    def restore_state(self, state: HistoryState) -> bool:
        """Restore to specified history state.
        
        Args:
            state: History state to restore to
            
        Returns:
            True if successful
        """
        try:
            self.doc.activeHistoryState = state.state
            logger.info(f"Restored to state: {state.name}")
            return True
            
        except Exception as e:
            logger.error(f"Error restoring state: {e}")
            return False
    
    def add_layer(self) -> bool:
        """Add new layer and return success.
        
        Returns:
            True if successful
        """
        try:
            self.doc.artLayers.add()
            logger.info("Added new layer")
            return True
            
        except Exception as e:
            logger.error(f"Error adding layer: {e}")
            return False

def main() -> None:
    """History management example."""
    try:
        # Create new document
        with Session(action="new_document") as pss:
            print("\n=== History Management ===")
            
            # Create history manager
            manager = HistoryManager(pss)
            
            # Get initial state
            initial_state = manager.get_current_state()
            if initial_state:
                print(f"\nInitial state: {initial_state.name}")
            
            # Add new layer
            if manager.add_layer():
                print("\nAdded new layer")
            
            # Get current state
            current_state = manager.get_current_state()
            if current_state:
                print(f"Current state: {current_state.name}")
            
            # List all states
            print("\nAll history states:")
            for state in manager.get_all_states():
                print(f"- {state.name}")
            
            # Restore to initial state
            if initial_state and manager.restore_state(initial_state):
                print(f"\nRestored to initial state: {initial_state.name}")
                
                # Verify current state
                final_state = manager.get_current_state()
                if final_state:
                    print(f"Final state: {final_state.name}")
            
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
