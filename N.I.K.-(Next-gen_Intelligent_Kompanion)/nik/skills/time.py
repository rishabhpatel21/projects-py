from .base import BaseSkill
from datetime import datetime

class TimeSkill(BaseSkill):
    """Skill to handle time and date related queries."""
    
    def __init__(self):
        super().__init__()
        self.name = "Time Skill"
        self.description = "Handles time and date related queries"
        self.trigger_words = ["time", "date", "day", "today", "now"]
        
    def can_handle(self, text: str) -> bool:
        """Check if this skill can handle the given text."""
        text = text.lower()
        return any(word in text for word in self.trigger_words)
    
    def handle(self, text: str) -> str:
        """Handle the given text and return a response."""
        text = text.lower()
        now = datetime.now()
        
        if "time" in text:
            return f"The current time is {now.strftime('%I:%M %p')}."
        elif "date" in text:
            return f"Today's date is {now.strftime('%B %d, %Y')}."
        elif "day" in text:
            return f"Today is {now.strftime('%A')}."
        elif "today" in text:
            return f"Today is {now.strftime('%A, %B %d, %Y')} and the time is {now.strftime('%I:%M %p')}."
        
        return f"The current time is {now.strftime('%I:%M %p')} and today is {now.strftime('%A, %B %d, %Y')}." 