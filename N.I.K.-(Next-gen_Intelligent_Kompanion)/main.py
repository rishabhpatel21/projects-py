from nik.interfaces.voice import VoiceInput, VoiceOutput
from nik.interfaces.text import TextInput, TextOutput
from nik.interfaces.gui import GUIInterface
from nik.core.controller import NikController
from nik.core.task_manager import TaskManager
from nik.skills.greeting import GreetingSkill
from nik.skills.time import TimeSkill
from nik.skills.identity import IdentitySkill
import threading

def main():
    # Initialize interfaces
    gui_interface = GUIInterface()
    
    # Initialize skills
    greeting_skill = GreetingSkill()
    time_skill = TimeSkill()
    identity_skill = IdentitySkill()
    
    # Initialize task manager with skills
    task_manager = TaskManager()
    task_manager.add_skill(greeting_skill)
    task_manager.add_skill(time_skill)
    task_manager.add_skill(identity_skill)
    
    # Initialize controller
    controller = NikController(gui_interface, gui_interface, task_manager)
    
    # Start controller in a separate thread
    controller_thread = threading.Thread(target=controller.start)
    controller_thread.daemon = True
    controller_thread.start()
    
    # Run the GUI in the main thread
    gui_interface.run()

if __name__ == "__main__":
    main() 