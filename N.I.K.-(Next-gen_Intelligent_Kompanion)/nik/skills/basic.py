import random
import datetime
from typing import List

from .base import BaseSkill

class GreetingSkill(BaseSkill):
    """Skill for handling greetings."""
    
    @property
    def name(self) -> str:
        return "Greeting"
    
    @property
    def keywords(self) -> List[str]:
        return ["hello", "hi", "hey", "greetings"]
    
    def can_handle(self, command: str) -> bool:
        return any(keyword in command.lower() for keyword in self.keywords)
    
    def handle(self, command: str) -> str:
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! I'm here to help.",
            "Greetings! How may I assist you?"
        ]
        return random.choice(responses)

class TimeSkill(BaseSkill):
    """Skill for handling time-related queries."""
    
    @property
    def name(self) -> str:
        return "Time"
    
    @property
    def keywords(self) -> List[str]:
        return ["time", "date", "day"]
    
    def can_handle(self, command: str) -> bool:
        return any(keyword in command.lower() for keyword in self.keywords)
    
    def handle(self, command: str) -> str:
        now = datetime.datetime.now()
        if "time" in command.lower():
            return f"The current time is {now.strftime('%I:%M %p')}"
        elif "date" in command.lower():
            return f"Today's date is {now.strftime('%B %d, %Y')}"
        elif "day" in command.lower():
            return f"Today is {now.strftime('%A')}"
        return "I'm not sure what time-related information you're looking for." 