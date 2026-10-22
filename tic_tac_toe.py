# This module will house the tic tac toe game for every break.
import tkinter as tk

def create_gui_game():
    gameWindow = tk.Tk()
    gameWindow.title("Tic Tac Toe")
    gameWindow.geometry("400x400")

    button1 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button2 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button3 = tk.Button(gameWindow, text="", width = 10, height = 5)

    button4 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button5 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button6 = tk.Button(gameWindow, text="", width = 10, height = 5)

    button7 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button8 = tk.Button(gameWindow, text="", width = 10, height = 5)
    button9 = tk.Button(gameWindow, text="", width = 10, height = 5)

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    gameWindow.mainloop()


create_gui_game()
'''
This module will contain the logic for playing a simple tic-tac-toe game.
It includes functions to play the game and check for a winner.
'''

def play_tic_tac_toe():
    pass

def check_winner():
    pass

def reset_board():
    pass