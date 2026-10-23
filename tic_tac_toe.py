# This module will house the tic tac toe game for every break.
import tkinter as tk

'''
This module will contain the logic for playing a simple tic-tac-toe game.
It includes functions to play the game and check for a winner.
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