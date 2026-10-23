
# A simple color memory game that users can play during their break

# TODO: Add Sounds!!

from operator import le
import random
import time
import tkinter as tk
import threading

COLORS = ["red", "green", "blue", "yellow"]

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
    global guide
    guide = tk.StringVar()
    guide.set("Setting up game")
    guide_label = tk.Label(root, textvariable=guide, font=("Arial", 12, "bold"))

    # configure the four 80x80 pixel gameplay buttons
    global red, green, blue, yellow
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

# this function runs the actual game logic: showing the color sequences and waiting for user input
def run_game():

    loading_animation()

    while True:
        # Show sequence:
        disable_buttons()
        guide.set("Remember the sequence!")
        add_to_color_sequence()
        show_sequence()
        time.sleep(1)

        # Take and verify user input:
        enable_buttons()
        guide.set("Now enter the sequence!")
        time.sleep(2)
        
        # show sequence
        # verify user input

def show_sequence():
    if len(sequence) == 0:
        return # quit if sequence is empty

    for color in sequence:
        if color == 0:
            flash_red()
        elif color == 1:
            flash_green()
        elif color == 2:
            flash_blue()
        elif color == 3:
            flash_yellow()
        time.sleep(0.5) # 0.5 second delay between flashes

def red_pressed():
    pass

def green_pressed():
    pass

def blue_pressed():
    pass

def yellow_pressed():
    pass

def flash_red():
    red.config(bg="white")
    time.sleep(0.2)
    red.config(bg="red")

def flash_green():
    green.config(bg="white")
    time.sleep(0.2)
    green.config(bg="green")

def flash_blue():
    blue.config(bg="white")
    time.sleep(0.2)
    blue.config(bg="blue")

def flash_yellow():
    yellow.config(bg="white")
    time.sleep(0.2)
    yellow.config(bg="yellow")

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

def loading_animation():
    # Plays the loading animation, resting for 0.5 seconds between each update
    guide.set("Setting up game.")
    time.sleep(0.25)
    guide.set("Setting up game..")
    time.sleep(0.25)
    guide.set("Setting up game...")
    time.sleep(0.25)
    guide.set("Setting up game....")
    time.sleep(0.25)
    guide.set("READY?")
    time.sleep(1.5)
    guide.set("GO!")
    time.sleep(1)


setup_color_memory_game()