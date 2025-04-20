from abc import ABC, abstractmethod
from typing import Optional

class InputInterface(ABC):
    """Base class for all input interfaces."""
    
    @abstractmethod
    def get_input(self) -> str:
        """Get input from the user."""
        pass

class OutputInterface(ABC):
    """Base class for all output interfaces."""
    
    @abstractmethod
    def output(self, message: str) -> None:
        """Output a message to the user."""
        pass 