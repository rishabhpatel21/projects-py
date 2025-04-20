import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Optional
import threading
import speech_recognition as sr
import time
import queue
from gtts import gTTS
import os
import tempfile
from playsound import playsound
from .base import InputInterface, OutputInterface

class GUIInterface(InputInterface, OutputInterface):
    """GUI interface for Nik using tkinter."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nik - Your AI Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")
        
        # Initialize exit flag
        self._should_exit = False
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000  # Adjust for better sensitivity
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8  # Shorter pause threshold
        
        try:
            self.microphone = sr.Microphone()
            # Adjust for ambient noise
            with self.microphone as source:
                print("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Ambient noise adjustment complete")
        except Exception as e:
            print(f"Microphone initialization error: {e}")
            self.microphone = None
        
        # Create temporary directory for audio files
        self.temp_dir = tempfile.mkdtemp()
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.style.configure("TFrame", background="#f5f5f5")
        self.style.configure("TButton", 
                           padding=10,
                           background="#2196F3",
                           foreground="white",
                           font=("Arial", 10))
        self.style.map("TButton",
                      background=[("active", "#1976D2")])
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        
        # Create title
        self.title_label = ttk.Label(
            self.header_frame,
            text="Nik AI Assistant",
            font=("Arial", 24, "bold"),
            background="#f5f5f5"
        )
        self.title_label.grid(row=0, column=0, sticky=tk.W)
        
        # Create status label
        self.status_label = ttk.Label(
            self.header_frame,
            text="Voice Input Active",
            font=("Arial", 10),
            foreground="#4CAF50",
            background="#f5f5f5"
        )
        self.status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Create chat display with modern styling
        self.chat_display = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=70,
            height=25,
            font=("Arial", 11),
            bg="white",
            relief="flat",
            padx=15,
            pady=10
        )
        self.chat_display.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        self.chat_display.config(state=tk.DISABLED)
        
        # Create input frame with modern styling
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        # Create input field with modern styling
        self.input_field = ttk.Entry(
            self.input_frame,
            width=60,
            font=("Arial", 11)
        )
        self.input_field.grid(row=0, column=0, padx=(0, 10), sticky=(tk.W, tk.E))
        self.input_field.bind("<Return>", lambda e: self._send_message())
        
        # Create send button with modern styling
        self.send_button = ttk.Button(
            self.input_frame,
            text="Send",
            command=self._send_message
        )
        self.send_button.grid(row=0, column=1, padx=(0, 10))
        
        # Create voice button with modern styling
        self.voice_button = ttk.Button(
            self.input_frame,
            text="🎤",
            command=self._toggle_voice_input
        )
        self.voice_button.grid(row=0, column=2)
        
        # Voice input state
        self.voice_input_active = True
        self.voice_thread = None
        self.listening = False
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.input_frame.columnconfigure(0, weight=1)
        
        # Message queue for communication between threads
        self.message_queue = []
        self.input_queue = []
        self.gui_update_queue = queue.Queue()
        
        # Start voice input by default
        self._toggle_voice_input()
        
        # Start checking for GUI updates
        self._check_gui_updates()
    
    def _check_gui_updates(self):
        """Check for GUI updates from other threads."""
        try:
            while True:
                update = self.gui_update_queue.get_nowait()
                if update[0] == 'status':
                    self.status_label.config(text=update[1], foreground=update[2])
                elif update[0] == 'message':
                    self._add_message(update[1], update[2])
                    if update[1] == "Nik":
                        # Start voice output in a separate thread after a short delay
                        threading.Thread(target=self._delayed_speak, args=(update[2],)).start()
                elif update[0] == 'voice_button':
                    self.voice_button.config(text=update[1])
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self._check_gui_updates)
    
    def _delayed_speak(self, message: str):
        """Delayed voice output to ensure GUI update happens first."""
        time.sleep(0.5)  # Short delay to ensure GUI update is visible
        self._speak_message(message)
    
    def _speak_message(self, message: str):
        """Convert text to speech and play it."""
        try:
            # Create a unique filename for this message
            temp_file = os.path.join(self.temp_dir, f"response_{time.time()}.mp3")
            
            # Generate speech
            tts = gTTS(text=message, lang='en', slow=False)
            tts.save(temp_file)
            
            # Play the audio
            playsound(temp_file)
            
            # Clean up the temporary file
            os.remove(temp_file)
        except Exception as e:
            print(f"Error in speech synthesis: {e}")
    
    def _send_message(self):
        """Send the message from the input field."""
        message = self.input_field.get()
        if message:
            self.input_queue.append(message)
            self._add_message("You", message)
            self.input_field.delete(0, tk.END)
    
    def _toggle_voice_input(self):
        """Toggle voice input mode."""
        if self.microphone is None:
            self.gui_update_queue.put(('status', "No microphone detected", "#F44336"))
            return
            
        self.voice_input_active = not self.voice_input_active
        if self.voice_input_active:
            self.gui_update_queue.put(('voice_button', "🔴"))
            self.gui_update_queue.put(('status', "Voice Input Active - Listening...", "#4CAF50"))
            # Start voice input thread
            self.voice_thread = threading.Thread(target=self._voice_input_loop)
            self.voice_thread.daemon = True
            self.voice_thread.start()
        else:
            self.gui_update_queue.put(('voice_button', "🎤"))
            self.gui_update_queue.put(('status', "Voice Input Inactive", "#F44336"))
            self.listening = False
    
    def _voice_input_loop(self):
        """Handle voice input in a separate thread."""
        if self.microphone is None:
            self.gui_update_queue.put(('status', "No microphone detected", "#F44336"))
            return
            
        self.listening = True
        while self.voice_input_active and self.listening:
            try:
                with self.microphone as source:
                    print("Listening...")
                    self.gui_update_queue.put(('status', "Voice Input Active - Listening...", "#4CAF50"))
                    
                    try:
                        audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        print("Audio captured, processing...")
                        self.gui_update_queue.put(('status', "Voice Input Active - Processing...", "#FF9800"))
                        
                        try:
                            text = self.recognizer.recognize_google(audio)
                            print(f"Recognized text: {text}")
                            if text:
                                self.input_queue.append(text.lower())
                                self.gui_update_queue.put(('message', "You", text))
                                self.gui_update_queue.put(('status', "Voice Input Active - Listening...", "#4CAF50"))
                        except sr.UnknownValueError:
                            print("Could not understand audio")
                            self.gui_update_queue.put(('status', "Voice Input Active - Could not understand", "#F44336"))
                        except sr.RequestError as e:
                            print(f"Request error: {e}")
                            self.gui_update_queue.put(('status', "Voice Input Active - Service error", "#F44336"))
                    except Exception as e:
                        print(f"Error during listening: {e}")
                        self.gui_update_queue.put(('status', f"Voice Input Error: {str(e)}", "#F44336"))
                        time.sleep(1)  # Wait before trying again
            except Exception as e:
                print(f"General error: {e}")
                self.gui_update_queue.put(('status', f"Voice Input Error: {str(e)}", "#F44336"))
                break
    
    def _add_message(self, sender: str, message: str):
        """Add a message to the chat display."""
        self.chat_display.config(state=tk.NORMAL)
        
        # Add timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M")
        
        # Configure tags for different message types
        self.chat_display.tag_configure("user", foreground="#2196F3")
        self.chat_display.tag_configure("nik", foreground="#4CAF50")
        self.chat_display.tag_configure("timestamp", foreground="#757575")
        
        # Insert message with styling
        if sender == "You":
            self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"{sender}: ", "user")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
            self.chat_display.insert(tk.END, f"{sender}: ", "nik")
        
        self.chat_display.insert(tk.END, f"{message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def get_input(self) -> str:
        """Get input from the user."""
        while not self.input_queue and not self._should_exit:
            self.root.update()
        if self._should_exit:
            return "exit"
        return self.input_queue.pop(0)
    
    def output(self, message: str) -> None:
        """Output a message to the GUI."""
        if message.lower() in ["goodbye! have a great day!", "goodbye!"]:
            self._should_exit = True
            self.root.after(1000, self.root.destroy)  # Close window after 1 second
        self.message_queue.append(message)
        self.gui_update_queue.put(('message', "Nik", message))
    
    def run(self):
        """Run the GUI main loop."""
        self._should_exit = False
        self.root.mainloop() 