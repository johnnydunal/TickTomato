# This module manages the custom sound effects and plays them as well

# IMPORTANT NOTE: Run the terminal command "pip install playsound==1.2.2" to install the playsound library first!

import time

from playsound import playsound # type: ignore
import threading

def play_sound(file_path):
    # plays the sound on a new thread so main thread isn't blocked
    threading.Thread(target=playsound, args=(file_path,), daemon=True).start()