# Nik - Personal AI Assistant

Nik is a JARVIS-style AI assistant built in Python, designed to be modular, extensible, and capable of both text and voice interaction.

## Features

- Voice input (speech-to-text)
- Text input/output
- Text-to-speech for responses
- Command parsing
- Modular plugin system
- Extensible architecture

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the assistant:
```bash
python main.py
```

## Project Structure

```
nik/
├── core/           # Core functionality
├── interfaces/     # Input/Output interfaces
├── skills/        # Pluggable skills/commands
├── utils/         # Utility functions
└── config/        # Configuration files
```

## Extending Nik

New skills can be added by creating a new class in the `skills` directory that inherits from the `BaseSkill` class.

## License

MIT License 