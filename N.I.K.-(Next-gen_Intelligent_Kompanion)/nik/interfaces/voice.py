import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from playsound import playsound
from typing import Optional

from .base import InputInterface, OutputInterface

class VoiceInput(InputInterface):
    """Voice input interface using speech recognition."""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def get_input(self) -> str:
        """Get voice input from the user."""
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source)
                print("Processing...")
                
                # Using Google's speech recognition
                text = self.recognizer.recognize_google(audio)
                return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

class VoiceOutput(OutputInterface):
    """Voice output interface using Google Text-to-Speech."""
    
    def __init__(self, language='en', slow=False):
        """
        Initialize the voice output.
        
        Args:
            language (str): Language code (e.g., 'en' for English, 'es' for Spanish)
            slow (bool): Whether to speak slowly
        """
        self.temp_dir = tempfile.mkdtemp()
        self.language = language
        self.slow = slow
        
        # Voice parameters
        self.speed = 1.0  # Speaking rate (1.0 is normal)
        self.pitch = 0.0  # Pitch adjustment (-1.0 to 1.0)
        self.volume = 1.0  # Volume level (0.0 to 1.0)
        
        # Available voices and their configurations
        self.voices = {
            'default': {'language': 'en', 'slow': False, 'speed': 1.0, 'pitch': 0.0, 'volume': 1.0},
            'slow': {'language': 'en', 'slow': True, 'speed': 0.8, 'pitch': 0.0, 'volume': 1.0},
            'british': {'language': 'en-uk', 'slow': False, 'speed': 1.0, 'pitch': 0.2, 'volume': 1.0},
            'australian': {'language': 'en-au', 'slow': False, 'speed': 1.0, 'pitch': 0.1, 'volume': 1.0},
            'indian': {'language': 'en-in', 'slow': False, 'speed': 1.1, 'pitch': -0.1, 'volume': 1.0},
            'spanish': {'language': 'es', 'slow': False, 'speed': 1.0, 'pitch': 0.0, 'volume': 1.0},
            'french': {'language': 'fr', 'slow': False, 'speed': 1.0, 'pitch': 0.0, 'volume': 1.0},
            'german': {'language': 'de', 'slow': False, 'speed': 1.0, 'pitch': 0.0, 'volume': 1.0},
            'robot': {'language': 'en', 'slow': False, 'speed': 0.9, 'pitch': 0.5, 'volume': 0.8},
            'whisper': {'language': 'en', 'slow': False, 'speed': 0.8, 'pitch': -0.3, 'volume': 0.6},
            'excited': {'language': 'en', 'slow': False, 'speed': 1.2, 'pitch': 0.3, 'volume': 1.0},
            'calm': {'language': 'en', 'slow': False, 'speed': 0.9, 'pitch': -0.2, 'volume': 0.9},
        }
    
    def set_voice(self, voice_name: str) -> None:
        """Set the voice configuration."""
        if voice_name in self.voices:
            config = self.voices[voice_name]
            self.language = config['language']
            self.slow = config['slow']
            self.speed = config['speed']
            self.pitch = config['pitch']
            self.volume = config['volume']
            print(f"Voice set to: {voice_name}")
        else:
            print(f"Voice '{voice_name}' not found. Available voices: {', '.join(self.voices.keys())}")
    
    def set_voice_parameters(self, speed: float = None, pitch: float = None, volume: float = None) -> None:
        """Set individual voice parameters."""
        if speed is not None:
            self.speed = max(0.5, min(2.0, speed))  # Clamp between 0.5 and 2.0
        if pitch is not None:
            self.pitch = max(-1.0, min(1.0, pitch))  # Clamp between -1.0 and 1.0
        if volume is not None:
            self.volume = max(0.0, min(1.0, volume))  # Clamp between 0.0 and 1.0
    
    def _add_emphasis(self, text: str) -> str:
        """Add emphasis to important words in the text."""
        # Words to emphasize
        emphasis_words = {
            'important', 'critical', 'urgent', 'warning', 'error',
            'success', 'great', 'amazing', 'wonderful', 'terrible'
        }
        
        words = text.split()
        for i, word in enumerate(words):
            if word.lower() in emphasis_words:
                words[i] = f"<emphasis level='strong'>{word}</emphasis>"
        
        return ' '.join(words)
    
    def _add_pauses(self, text: str) -> str:
        """Add natural pauses to the text."""
        # Add pauses after punctuation
        text = text.replace('.', '. <break time="500ms"/>')
        text = text.replace('!', '! <break time="500ms"/>')
        text = text.replace('?', '? <break time="500ms"/>')
        text = text.replace(',', ', <break time="300ms"/>')
        
        return text
    
    def output(self, message: str) -> None:
        """Output a message using text-to-speech."""
        print(f"Nik: {message}")
        
        try:
            # Create a temporary file for the audio
            temp_file = os.path.join(self.temp_dir, "response.mp3")
            
            # Add emphasis and pauses
            message = self._add_emphasis(message)
            message = self._add_pauses(message)
            
            # Generate speech with current voice settings
            tts = gTTS(
                text=message,
                lang=self.language,
                slow=self.slow
            )
            tts.save(temp_file)
            
            # Play the audio file using playsound
            playsound(temp_file)
            
            # Clean up the temporary file
            os.remove(temp_file)
        except Exception as e:
            print(f"Error playing audio: {e}") 
            
"""voice_output.set_voice('british')  # Try different voices like 'whisper', 'excited', etc.   """