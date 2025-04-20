from typing import Dict, List, Optional, Callable
import threading
import time
from ..skills.base import BaseSkill

class Task:
    """Represents a task that can be scheduled and executed."""
    
    def __init__(self, name: str, func: Callable, args: tuple = (), kwargs: dict = None):
        self.name = name
        self.func = func
        self.args = args
        self.kwargs = kwargs or {}
        self.completed = False
        self.result = None
        self.error = None

class TaskManager:
    """Manages the execution of tasks and background processes."""
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.running = True
        self.thread = threading.Thread(target=self._process_tasks, daemon=True)
        self.thread.start()
        self.skills: List[BaseSkill] = []
    
    def add_task(self, task: Task) -> None:
        """Add a new task to the manager."""
        self.tasks[task.name] = task
    
    def get_task(self, name: str) -> Optional[Task]:
        """Get a task by name."""
        return self.tasks.get(name)
    
    def _process_tasks(self) -> None:
        """Process tasks in the background."""
        while self.running:
            for task in list(self.tasks.values()):
                if not task.completed and not task.error:
                    try:
                        task.result = task.func(*task.args, **task.kwargs)
                        task.completed = True
                    except Exception as e:
                        task.error = str(e)
            time.sleep(0.1)
    
    def stop(self) -> None:
        """Stop the task manager."""
        self.running = False
        self.thread.join()
        self.skills.clear()
    
    def add_skill(self, skill: BaseSkill) -> None:
        """Add a new skill to the task manager."""
        self.skills.append(skill)
    
    def get_response(self, text: str) -> str:
        """Get a response from the appropriate skill."""
        for skill in self.skills:
            if skill.can_handle(text):
                return skill.handle(text)
        return "I'm sorry, I don't understand that. Could you please rephrase?" 