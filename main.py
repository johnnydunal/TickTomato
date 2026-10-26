# TickTomato main script

'''
Note:
This script implements a simple Pomodoro timer using time, tkinter and threading.
The timer will use time.sleep() to accurately keep track of time.
Also, threading will *eventually* be used to make sure the timer doesn't freeze the window!
'''

# Note: Print statements are used for debugging purposes only and will eventuall be removed.

import time
import tkinter
import threading
from enum import Enum

# Import the break games
from color_memory_game import setup_color_memory_game
from tic_tac_toe import game_window


# Define lengths of work/break (in seconds!)
WORK_LENGTH = 25 * 60
BREAK_LENGTH = 5 * 60

LENGTH_OF_SECOND = 1 # should be 1 unless trying to test code by "making time pass faster"
DEBUG = False # Set to true if debugging, will show debug print statements that explain what's happening

# the global reference for the main GUI window
root_window = None

# Enum to represent the state of the timer
class Timer(Enum):
    READY = 0 # timer ready to start
    POMODORO_ON = 1 # 25 min timer on
    POMODORO_OFF = 2 # 25 min timer but paused
    BREAK_ON = 3 # 5 min break timer on
    BREAK_OFF = 4 # 5 min break timer but paused

timer = Timer.READY
time_left = 25*60 # keeps track of time left for the timers
time_label_var = None

# Starts the program
def main():

    # Prints debug statements
    debug("Starting main function...")

    # creates a thread for the timer so it can run at the same time as the gui
    work_thread = threading.Thread(target=start_timer_logic, daemon=True)

    work_thread.start() # start work timer
    create_gui() # start timer

def start_timer_logic():
    time.sleep(0.5) # Give GUI a moment to set up
    debug("Starting timer logic...")
    work_timer()

# Manages the WORK timer
def work_timer():
    debug("Starting work timer...")
    start_timer(WORK_LENGTH) # begins the 25-minute work timer
    break_timer() # switch to break timer

# Manages the BREAK timer
def break_timer():
    debug("Starting break timer...")
    start_timer(BREAK_LENGTH) # begins the 5-minute break timer
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
        time_left = time_left - 1

        if time_left < 0:
            break

# Creates the gui for the timer
def create_gui():
    debug("Creating GUI...")

    # Set up the window
    global root_window
    root_window = tkinter.Tk()
    root_window.title("TickTomato")
    root_window.geometry("256x128")
    root_window.configure(bg='red')

    # Set up the time display label
    global time_left, time_label_var
    time_label_var = tkinter.StringVar() # the time variable used in tkinter labels to let it auto-update
    time_label_var.set(format_time())
    time_label = tkinter.Label(root_window, textvariable=time_label_var, bg='red', font=("Arial", 48, "bold"))
    time_label.pack(pady = 40)
    # time_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=40)

    root_window.mainloop()

def toggle_break_gui():
    # Switches between the setup for the work/break timers
    pass

# formats time_left into proper time format (MM:SS)
def format_time():
    global time_left
    minutes, seconds = divmod(time_left, 60) # divmod returns the quotient and remainder of the division
    return f"{minutes:02}:{seconds:02}"

# This function starts the break games
def start_game(game_number):
    if game_number == 1: # Color Memory game
        debug("Starting Color Memory game...")
        game_thread = threading.Thread(target=setup_color_memory_game, daemon=True)
        game_thread.start()
    elif game_number == 2: # Tic-Tac-Toe game
        debug("Starting Tic-Tac-Toe game...")
        game_thread = threading.Thread(target=game_window, daemon=True)
        game_thread.start()

# Prints debug messages, but only if DEBUG is True
def debug(message):
    if DEBUG:
        print(message)

if __name__ == "__main__":
    main()