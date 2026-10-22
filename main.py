# TickTomato main script

# Currently just a base script to test python's tkinter windows and their functionalities.

import time
import tkinter

def main():
    print("Welcome to TickTomato!")

def start_timer():
    print("Starting the timer...")
    time.sleep(5)
    print("Timer finished!")

# Many functions to manage timers
def check_timer():
    pass

def pause_timer():
    pass

def resume_timer():
    pass

def reset_timer():
    pass

def start_break_timer():
    pass

def check_break_timer():
    pass

def pause_break_timer():
    pass

def resume_break_timer():
    pass

def reset_break_timer():
    pass

def create_gui():
    root = tkinter.Tk()
    root.title("TickTomato")
    label = tkinter.Label(root, text="Welcome to TickTomato!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
    create_gui()