from abc import ABC, abstractmethod

class BaseSkill(ABC):
    """Base class for all skills."""
    
    def __init__(self):
        self.trigger_words = []
        self.name = ""
        self.description = ""
    
    @abstractmethod
    def can_handle(self, text: str) -> bool:
        """Check if this skill can handle the given text."""
        pass
    
    @abstractmethod
    def handle(self, text: str) -> str:
        """Handle the given text and return a response."""
        pass 