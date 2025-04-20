from typing import Optional
from ..interfaces.base import InputInterface, OutputInterface
from .task_manager import TaskManager

class NikController:
    """Controls the flow of the application."""
    
    def __init__(self, input_interface: InputInterface, output_interface: OutputInterface, task_manager: TaskManager):
        self.input_interface = input_interface
        self.output_interface = output_interface
        self.task_manager = task_manager
        self.running = True
    
    def start(self):
        """Start the controller."""
        # Send initial greeting
        self.output_interface.output("Hello! I'm Nik, your personal AI assistant. How can I help you today?")
        
        try:
            while self.running:
                # Get input from the user
                text = self.input_interface.get_input()
                
                # Check for exit commands
                if text.lower() in ["exit", "quit", "bye", "goodbye"]:
                    self.output_interface.output("Goodbye! Have a great day!")
                    self.running = False
                    break
                
                # Get response from task manager
                response = self.task_manager.get_response(text)
                
                # Output the response
                self.output_interface.output(response)
        except KeyboardInterrupt:
            self.output_interface.output("Goodbye! Have a great day!")
            self.running = False
        finally:
            self.task_manager.stop() 