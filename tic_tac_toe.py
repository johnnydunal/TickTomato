# This module will house the tic tac toe game for every break.
import tkinter as tk
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # gets the absolute path of the directory containing this script
LOGO_PATH = BASE_DIR / "assets" / "images" / "logo.png" # path to logo image

'''
This module will contain the logic for playing a simple tic-tac-toe game.
It includes functions to play the game and check for a winner.
'''
'''
current_player = 0
def check_game(button):
    global current_player
    if button["text"] == "":
        if current_player == 0:
            button["text"] = "X"
            current_player = 1
        else:
            button["text"] = "O"
            current_player = 0
    if check_winner():
        print("Winner!")
        start_menu()
    check_tie()
        


# This function will create a button for the tic-tac-toe game. It will set the button's text to an empty string and set its command to the check_game function.
def createButton(gameWindow):
    button_width = 10
    button_height = 5
    button = tk.Button(gameWindow, text="", width=button_width, height=button_height)
    button.config(command=lambda: check_game(button))
    return button

# This function will create a 3x3 grid of buttons for the tic-tac-toe game. It will use the createButton function to create each button and place it in the grid using the grid method.
buttons = []
def bunchaButton(gameWindow):
    rows = 3
    collums = 3
    for i in range(rows):
        for j in range(collums):
            button = createButton(gameWindow)
            button.grid(row=i, column=j)
            buttons.append(button)

def check_winner():
    #check rows
    if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"] != "":
        winner_board(0, 1, 2)
        return True

    if buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"] != "":
        winner_board(3, 4, 5)
        return True

    if buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"] != "":
        winner_board(6, 7, 8)
        return True

    #check columns
    if buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"] != "":
        winner_board(0, 3, 6)
        return True

    if buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"] != "":
        winner_board(1, 4, 7)
        return True

    if buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"] != "":
        winner_board(2, 5, 8)
        return True

    #check diagonals
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != "":
        winner_board(0, 4, 8)
        return True

    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != "":
        winner_board(2, 4, 6)
        return True

    return False

def all_buttons_filled():
    for button in buttons:
        if button["text"] == "":
            return False
    return True

def check_tie():
    if all_buttons_filled() and not check_winner():
        start_menu()
        print("It's a tie!")


def reset_board():
    if all_buttons_filled() or check_winner():
        for button in buttons:
            button.config(text="", bg="SystemButtonFace", state="normal")
        global current_player
        current_player = 0

def reset():
    resetWindow = tk.Tk()
    resetWindow.title("Reset Game")
    yes_button = tk.Button(resetWindow, text="RESET", command=lambda: [reset_board(), resetWindow.destroy()])
    yes_button.pack()

def destroy_window(window):
    window.destroy()

def winner_board(a, b, c):
    buttons[a].config(bg="red")
    buttons[b].config(bg="red")
    buttons[c].config(bg="red")
    stop_game()

def stop_game():
    for button in buttons:
        button.config(state="disabled")

def play_tic_tac_toe_two():
    gameWindow = tk.Tk()
    gameWindow.title("Tic Tac Toe")
    gameWindow.geometry("239x257")
    gameWindow.resizable(False, False)
    bunchaButton(gameWindow)

    gameWindow.mainloop()

def play_tic_tac_toe_one():
    gameWindow = tk.Tk()
    gameWindow.title("Tic Tac Toe")
    gameWindow.geometry("239x257")
    gameWindow.resizable(False, False)
    bunchaButton(gameWindow)

    

    gameWindow.mainloop()

def start_menu():
    menuWindow = tk.Tk()
    menuWindow.title("Start Menu")
    menuWindow.geometry("239x257")
    menuWindow.resizable(False, False)

    start_button = tk.Button(menuWindow, text="Single Player", command=lambda: [menuWindow.destroy(), play_tic_tac_toe_one()])
    start_button.pack()
    start_button2 = tk.Button(menuWindow, text="Two Players", command=lambda: [menuWindow.destroy(), play_tic_tac_toe_two()])
    start_button2.pack()

    menuWindow.mainloop()
start_menu()
'''

mode = None
current_player = "X"

def game_window():
    root = tk.Tk()
    root.title("Game Window")
    root.geometry("239x257")
    root.resizable(False, False)

    # Setting up logo image
    logo = tk.PhotoImage(file=LOGO_PATH)
    root.iconphoto(True, logo)

    def start_game(selected_mode):
        global mode

        mode = selected_mode
        print(f"Selected mode: {mode}")

        option1.destroy()
        option2.destroy()

        tictactoe_game(root)

    option1 = tk.Button(root,text="Single Player",command=lambda: start_game("single"))
    option1.pack()
    option2 = tk.Button(root,text="Two Players",command=lambda: start_game("two"))
    option2.pack()

    root.mainloop()

def tictactoe_game(root):
    buttons = []

    def check_state():
        if buttons[0]["text"] == buttons[1]["text"] == buttons[2]["text"] != "":
            print(f"Winner: {buttons[0]['text']}")
            stop_game(0, 1, 2)
            return True
        if buttons[3]["text"] == buttons[4]["text"] == buttons[5]["text"] != "":
            print(f"Winner: {buttons[3]['text']}")
            stop_game(3, 4, 5)
            return True
        if buttons[6]["text"] == buttons[7]["text"] == buttons[8]["text"] != "":
            print(f"Winner: {buttons[6]['text']}")
            stop_game(6, 7, 8)
            return True
        if buttons[0]["text"] == buttons[3]["text"] == buttons[6]["text"] != "":
            print(f"Winner: {buttons[0]['text']}")
            stop_game(0, 3, 6)
            return True
        if buttons[1]["text"] == buttons[4]["text"] == buttons[7]["text"] != "":
            print(f"Winner: {buttons[1]['text']}")
            stop_game(1, 4, 7)
            return True
        if buttons[2]["text"] == buttons[5]["text"] == buttons[8]["text"] != "":
            print(f"Winner: {buttons[2]['text']}")
            stop_game(2, 5, 8)
            return True
        if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != "":
            print(f"Winner: {buttons[0]['text']}")
            stop_game(0, 4, 8)
            return True
        if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != "":
            print(f"Winner: {buttons[2]['text']}")
            stop_game(2, 4, 6)
            return True
        if all(button["text"] != "" for button in buttons):
            print("It's a tie!")
            for button in buttons:
                button.config(bg="red")
                button.config(state="disabled")
            back_to_menu()
            return True
        return False

    def stop_game(a, b, c):
        buttons[a].config(bg="green")
        buttons[b].config(bg="green")
        buttons[c].config(bg="green")
        for button in buttons:
                    button.config(state="disabled")
        back_to_menu()

    def back_to_menu():
        def reset_board():
            for button in buttons:
                button.destroy()
        game_window()

    def randomizer_bot():
        available = []

        if buttons[4]["text"] == "":
            buttons[4]["text"] = "O"
            return
        
        for button in buttons:
            if button["text"] == "":
                available.append(button)
        if available:
            random.choice(available)["text"] = "O"

    def button_click(button):
        global current_player
        if button["text"] == "":
            button["text"] = current_player
            if mode == "two":
                if current_player == "X":
                    check_state()
                    current_player = "O"
                else:
                    check_state()
                    current_player = "X"
            elif mode == "single":
                if current_player == "X":
                    player_won = check_state()
                    if not player_won:
                        randomizer_bot()
                        check_state()
            print(f"Current player: {current_player}")

    for row in range(3):
        for column in range(3):
            button = tk.Button(root,text="",width=10,height=5)
            button.config(command=lambda b=button: button_click(b))
            button.grid(row=row, column=column)
            buttons.append(button)

    if mode == "single":
        randomizer_bot()

# game_window()