# TickTomato main script

import time
import tkinter

def main():
    print("Welcome to TickTomato!")

def start_timer():
    print("Starting the timer...")
    time.sleep(5)
    print("Timer finished!")

def create_gui():
    root = tkinter.Tk()
    root.title("TickTomato")
    label = tkinter.Label(root, text="Welcome to TickTomato!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
    create_gui()