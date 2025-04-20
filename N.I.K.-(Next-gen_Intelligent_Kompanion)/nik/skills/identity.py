from .base import BaseSkill

class IdentitySkill(BaseSkill):
    """Skill to handle questions about Nik's identity."""
    
    def __init__(self):
        super().__init__()
        self.name = "Identity Skill"
        self.description = "Handles questions about Nik's identity and creator"
        self.trigger_words = ["name", "who", "created", "made", "identity"]
        
    def can_handle(self, text: str) -> bool:
        """Check if this skill can handle the given text."""
        text = text.lower()
        return any(word in text for word in self.trigger_words) and (
            "nik" in text or 
            "your" in text or 
            "who are you" in text
        )
    
    def handle(self, text: str) -> str:
        """Handle the given text and return a response."""
        text = text.lower()
        
        if "name" in text:
            return "My name is Nik. I was created by my developer to be your personal AI assistant."
        elif "who made you" in text or "who created you" in text:
            return "I was created by my developer to be your helpful AI assistant. I'm here to make your life easier and more productive."
        elif "who are you" in text:
            return "I am Nik, your personal AI assistant. I was created to help you with various tasks, answer your questions, and make your daily life more convenient."
        elif "what can you do" in text:
            return "I can help you with many things! I can tell you the time, date, greet you, and answer questions about myself. I'm constantly learning new skills to assist you better."
        
        return "I'm Nik, your personal AI assistant. How can I help you today?" 