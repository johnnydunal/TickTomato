# TickTomato main script

'''
Note:
This script implements a simple Pomodoro timer using time, tkinter and threading.
The timer will use time.sleep() to accurately keep track of time.
Also, threading will *eventually* be used to make sure the timer doesn't freeze the window!
'''

# TODO: implement more buttons into timer display and handle their functionality and also call the game apps

import time
import tkinter
from tkinter import ttk
import threading
from enum import Enum
from pathlib import Path

# Import the sound manager
from sound_manager import play_sound

# Import the break games
from color_memory_game import setup_color_memory_game
from tic_tac_toe import game_window
games = ["Tic-Tac-Toe", "Color Memory"] # for the game selection menu

# Define lengths of work/break (in seconds!)
WORK_LENGTH = 25 * 60
BREAK_LENGTH = 5 * 60

LENGTH_OF_SECOND = 1 # should be 1 unless trying to test code by "making time pass faster"
DEBUG = False # Set to true if debugging, will show debug print statements that explain what's happening

# the global reference for the main GUI window
root_window = None

BASE_DIR = Path(__file__).resolve().parent # gets the absolute path of the directory containing this script
LOGO_PATH = BASE_DIR / "assets" / "images" / "logo.png" # path to logo image

# Enum to represent the state of the timer
class Timer(Enum):
    READY = 0 # timer ready to start
    ON = 1 # timer on
    OFF = 2 # timer paused

timer = Timer.READY # keeps track of the timer's state
time_left = WORK_LENGTH # keeps track of time left for the timers

# Window Components
time_label_var = None # Text for time label
pause_button = None # Pause button
reset_button = None # Reset buttons
combo = None # Combobox for selecting a game during break time
game_button = None # Button to start the selected game during break timenevermind too much work

# Starts the program
def main():
    debug("Starting main function...")
    create_gui() # start gui

def start_timer_logic():
    # creates a thread for the timer so it can run at the same time as the gui
    work_thread = threading.Thread(target=work_timer, daemon=True)
    
    debug("Starting timer logic...")
    work_thread.start() # start work timer

# Manages the WORK timer
def work_timer():
    debug("Starting work timer...")
    global timer
    timer = Timer.READY
    pause_button.config(text="Start")
    start_timer(WORK_LENGTH) # begins the 25-minute work timer
    break_timer() # switch to break timer

# Manages the BREAK timer
def break_timer():
    debug("Starting break timer...")
    start_break_gui()
    global timer
    timer = Timer.ON
    pause_button.config(text="Pause")
    start_timer(BREAK_LENGTH) # begins the 5-minute break timer
    end_break_gui()
    work_timer() # switch to work timer

# Calculates time and updates time_left
def start_timer(timer_length):
    # Note: length is in seconds!
    global time_left, time_label_var # make sure the global time_left and time_label_var variables are used
    time_left = timer_length # set the time to the given time
    debug(f"Starting {format_time()} Timer...")
    while True:
        debug(format_time())
        time_label_var.set(format_time()) # update the GUI time label
        time.sleep(LENGTH_OF_SECOND)
        if timer == Timer.ON: # only counts down if timer is on
            time_left = time_left - 1

        if time_left < 0:
            play_sound("assets/sounds/orchestra_win_song.mp3")
            break

# Creates the gui for the timer
def create_gui():
    debug("Creating GUI...")

    # Set up the window
    global root_window
    root_window = tkinter.Tk()
    root_window.title("TickTomato")
    # root_window.geometry("256x128") # Old size for just text by itself
    root_window.geometry("240x160")
    root_window.resizable(False, False)
    root_window.configure(bg="#B22222")

    # Setting up logo image
    logo = tkinter.PhotoImage(file=LOGO_PATH)
    root_window.iconphoto(True, logo)

    # This line keeps the window on top of all other applications
    root_window.attributes('-topmost', True) # NOTE: Put ability to toggle this feature in settings later

    # Set up the time display label
    global time_left, time_label_var
    time_label_var = tkinter.StringVar() # the time variable used in tkinter labels to let it auto-update
    time_label_var.set(format_time())
    time_label = tkinter.Label(root_window, textvariable=time_label_var, bg="#B22222", font=("Arial", 48, "bold"))
    time_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=35, pady=10)

    # Set up the buttons
    global pause_button, reset_button
    pause_button = tkinter.Button(root_window, text="Start", bg='white', font=("Arial", 12), command=pause)
    reset_button = tkinter.Button(root_window, text="Reset", bg='white', font=("Arial", 12), command=reset)
    
    pause_button.grid(row=1, column=0, padx=10, pady=10)
    reset_button.grid(row=1, column=1, padx=10, pady=10)

    start_timer_logic() # start the timer logic in the main thread

    root_window.mainloop()

# Pauses the game timer
def pause():
    debug("Pausing/Resuming timer...")
    global timer
    if timer == Timer.ON:
        timer = Timer.OFF
        pause_button.config(text="Resume")
        debug("Timer paused.")
    else:
        play_sound("assets/sounds/start.mp3")
        timer = Timer.ON
        pause_button.config(text="Pause")
        debug("Timer resumed.")

# Resets the game timer
def reset():
    debug("Resetting timer...")
    global timer, time_left
    time_left = WORK_LENGTH
    timer = Timer.OFF
    pause_button.config(text="Start")
    try:
        end_break_gui()
    except Exception as e:
        debug(f"Error while ending break GUI: {e}")
    debug("Timer reset.")

# Switches between the setup for the work/break timers
def start_break_gui():
    # SWITCH TO BREAK MENU
    global root_window, combo, game_button
    root_window.geometry("240x200")
    combo = ttk.Combobox(root_window, values=games, state="readonly")
    combo.set("Choose a game!")  # Set placeholder text
    combo.grid(row=2, column=0, padx=10, pady=10)

    game_button = tkinter.Button(root_window, text="Select", bg='white', font=("Arial", 12), command=lambda: start_game(games.index(combo.get())))
    game_button.grid(row=2, column=1, padx=10, pady=10)

def end_break_gui():
    # SWITCH BACK TO WORK MENU
    global combo, game_button, root_window
    combo.destroy()
    game_button.destroy()
    root_window.geometry("240x160")

# formats time_left into proper time format (MM:SS)
def format_time():
    global time_left
    minutes, seconds = divmod(time_left, 60) # divmod returns the quotient and remainder of the division
    return f"{minutes:02}:{seconds:02}"

# This function starts the break games
def start_game(game_number):
    if game_number == 0: # Tic-Tac-Toe game
        debug("Starting Tic-Tac-Toe game...")
        game_thread = threading.Thread(target=game_window, daemon=True)
        game_thread.start()
        debug("Tic-Tac-Toe game thread started.")
    elif game_number == 1: # Color Memory game
        debug("Starting Color Memory game...")
        game_thread = threading.Thread(target=setup_color_memory_game, daemon=True)
        game_thread.start()
        debug("Color Memory game thread started.")

# Prints debug messages, but only if DEBUG is True
def debug(message):
    if DEBUG:
        print(message)

if __name__ == "__main__":
    main()