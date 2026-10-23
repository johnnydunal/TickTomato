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

# Define lengths of work/break (in seconds!)
WORK_LENGTH = 25 * 60
BREAK_LENGTH = 5 * 60

LENGTH_OF_SECOND = 0.005 # should be 1 unless trying to test code by "making time pass faster"

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
    print("Welcome to TickTomato!")

    # creates a thread for the gui so it can run at the same time as the timer
    gui_thread = threading.Thread(target=create_gui)

    gui_thread.start() # start GUI
    time.sleep(1) # Give GUI a moment to set up
    work_timer() # start timer

    gui_thread.join() # wait for the GUI thread to finish before exiting the program

# Manages the WORK timer
def work_timer():
    print("Starting work timer...")
    start_timer(WORK_LENGTH) # begins the 25-minute work timer
    break_timer() # switch to break timer

# Manages the BREAK timer
def break_timer():
    print("Starting break timer...")
    start_timer(BREAK_LENGTH) # begins the 5-minute break timer
    work_timer() # switch to work timer

# Calculates time and updates time_left
def start_timer(timer_length):
    # Note: length is in seconds!
    global time_left, time_label_var # make sure the global time_left and time_label_var variables are used
    time_left = timer_length # set the time to the given time
    print(f"Starting {format_time()} Timer...")
    while True:
        # print(format_time()) # currently only prints for testing purposes
        time_label_var.set(format_time()) # update the GUI time label
        time.sleep(LENGTH_OF_SECOND)
        time_left = time_left - 1

        if time_left < 0:
            break

# Creates the gui for the timer
def create_gui():
    # Set up the window
    root = tkinter.Tk()
    root.title("TickTomato")
    root.geometry("256x128")
    root.configure(bg='red')

    # Set up the time display label
    global time_left, time_label_var
    time_label_var = tkinter.StringVar() # the time variable used in tkinter labels to let it auto-update
    time_label_var.set(format_time())
    time_label = tkinter.Label(root, textvariable=time_label_var, bg='red', font=("Arial", 48, "bold"))
    time_label.pack(pady = 40)

    root.mainloop()

# formats time_left into proper time format (MM:SS)
def format_time():
    global time_left
    minutes, seconds = divmod(time_left, 60) # divmod returns the quotient and remainder of the division
    return f"{minutes:02}:{seconds:02}"

def start_game():
    # This will eventually call the start function of the tic tac toe game (and prob run the game on a seperate thread)
    pass

if __name__ == "__main__":
    main()