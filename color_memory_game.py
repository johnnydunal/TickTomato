
# A simple color memory game that users can play during their break

'''
TODO:
- Make the guide label work correctly
- Add the full game with actual sequence
- Add Sounds
'''

from operator import le
import random
import time
import tkinter as tk
import threading

COLORS = ["red", "green", "yellow", "blue"]

sequence = []

guide = None # this will tell users what to do
red = None
green = None
blue = None
yellow = None

def setup_color_memory_game():
    root = tk.Tk()
    root.title("Color Memory Game")
    root.resizable(False, False) 
    root.geometry("334x368")
    root.configure(bg='white')

    pixel_dir = tk.PhotoImage(width=1, height=1) # forces width and height to be set in pixels for the buttons later

    # configure the guide label
    guide = tk.StringVar()
    guide.set("Setting up game...")
    guide_label = tk.Label(root, textvariable=guide, font=("Arial", 12, "bold"))

    time.sleep(1)

    # configure the four 80x80 pixel gameplay buttons
    red = tk.Button(root, image=pixel_dir, compound="center", width=150, height=150, bg="red", fg="red", command=red_pressed)
    green = tk.Button(root, image=pixel_dir, compound="center", width=150, height=150, bg="green", fg="green", command=green_pressed)
    blue = tk.Button(root, image=pixel_dir, compound="center", width=150, height=150, bg="blue", fg="blue", command=blue_pressed)
    yellow = tk.Button(root, image=pixel_dir, compound="center", width=150, height=150, bg="yellow", fg="yellow", command=yellow_pressed)

    guide_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=5)
    red.grid(row=1, column=0, padx=5, pady=5)
    green.grid(row=1, column=1, padx=5, pady=5)
    blue.grid(row=2, column=0, padx=5, pady=5)
    yellow.grid(row=2, column=1, padx=5, pady=5)

    # seperate thread for the background logic
    game_thread = threading.Thread(target=run_game, daemon=True)
    game_thread.start()

    root.mainloop()

def run_game():
    # this runs the actual game, showing the color sequences and waiting for user input
    pass

def show_sequence():
    if len(sequence) == 0:
        return

    for color in sequence:
        pass # TODO: Finish later

def red_pressed():
    guide.set("RED")

def green_pressed():
    guide.set("GREEN")

def blue_pressed():
    guide.set("BLUE")

def yellow_pressed():
    guide.set("YELLOW")

def disable_buttons():
    red.config(state="disabled")
    green.config(state="disabled")
    yellow.config(state="disabled")
    blue.config(state="disabled")

def enable_buttons():
    red.config(state="normal")
    green.config(state="normal")
    yellow.config(state="normal")
    blue.config(state="normal")

# adds a random color index to the sequence
def add_to_color_sequence():
    global sequence
    sequence.append(random.randint(0, 3))


setup_color_memory_game()