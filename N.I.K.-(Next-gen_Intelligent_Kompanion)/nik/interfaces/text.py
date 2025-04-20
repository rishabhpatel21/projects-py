from .base import InputInterface, OutputInterface

class TextInput(InputInterface):
    """Text input interface using command line."""
    
    def get_input(self) -> str:
        """Get text input from the user."""
        return input("You: ").lower()

class TextOutput(OutputInterface):
    """Text output interface using command line."""
    
    def output(self, message: str) -> None:
        """Output a message to the command line."""
        print(f"Nik: {message}") 