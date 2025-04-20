from .base import BaseSkill

class GreetingSkill(BaseSkill):
    """Skill to handle greetings and basic conversation."""
    
    def __init__(self):
        super().__init__()
        self.name = "Greeting Skill"
        self.description = "Handles greetings and basic conversation"
        self.trigger_words = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        
    def can_handle(self, text: str) -> bool:
        """Check if this skill can handle the given text."""
        text = text.lower()
        return any(word in text for word in self.trigger_words)
    
    def handle(self, text: str) -> str:
        """Handle the given text and return a response."""
        text = text.lower()
        
        if "good morning" in text:
            return "Good morning! How can I help you today?"
        elif "good afternoon" in text:
            return "Good afternoon! What can I do for you?"
        elif "good evening" in text:
            return "Good evening! How may I assist you?"
        elif any(word in text for word in ["hello", "hi", "hey", "greetings"]):
            return "Hello! I'm Nik, your personal AI assistant. How can I help you today?"
        
        return "Hello! How can I assist you?" 