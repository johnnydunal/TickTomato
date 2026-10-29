# This module creates the task management system and todo list

import tkinter as tk
import json_manager as jam
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # gets the absolute path of the directory containing this script
LOGO_PATH = BASE_DIR / "assets" / "images" / "logo.png" # path to logo image

def task_manager_program():
    tasks_list = jam.get_tasks()
    print(tasks_list)

    window = tk.Tk()
    window.title("Task Manager")
    window.geometry("500x200")

    # Setting up logo image
    logo = tk.PhotoImage(file=LOGO_PATH, master=window)
    window.iconphoto(True, logo)
    

    def grid_design():
        global task_listbox
        global input_frame

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        list_frame = tk.Frame(window)
        list_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)

        task_listbox = tk.Listbox(list_frame, font=("Arial", 12))
        task_listbox.grid(row=0, column=0, sticky="nsew")

        scrollbar = tk.Scrollbar(list_frame,orient="vertical",command=task_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        task_listbox.config(yscrollcommand=scrollbar.set)

        input_frame = tk.Frame(window)
        input_frame.grid(row=1,column=0,sticky="ew",padx=10,pady=(0, 10))

        input_frame.grid_columnconfigure(0, weight=1)
    
    grid_design()

    # box to type tasks (remove and add)
    task_entry = tk.Entry(input_frame)
    task_entry.grid(row=0, column=0, sticky="ew")

    def update_tasks():
        task_listbox.delete(0, tk.END)

        for task in jam.get_tasks():
            task_listbox.insert(tk.END, f"  -   {task}")

    def add_task():
        task = task_entry.get().strip()

        if task:
            jam.add_tasks([task])

            task_entry.delete(0, tk.END)

            update_tasks()

    def remove_task():
        task = task_entry.get().strip()

        if task:
            jam.remove_tasks(task)

            task_entry.delete(0, tk.END)

            update_tasks()

    # add tasks
    add_task_button = tk.Button(input_frame,text="ADD",command=add_task)
    add_task_button.grid(row=0, column=1, padx=(10, 0))

    # remove tasks
    remove_task_button = tk.Button(input_frame, text="DELETE",command=remove_task)
    remove_task_button.grid(row=0, column=2, padx = (10  ,0))
    update_tasks()

    def reset_tasks():
        if task_listbox.size() > 0:
            jam.reset_tasks()
            update_tasks()
    reset_tasks_button = tk.Button(input_frame, text = "RESET", command=reset_tasks)
    reset_tasks_button.grid(row=0, column=3, padx = (10  ,0))

    """
    #check box
    box = tk.Button(text = "[  ]", command=lambda: check_box_logic())
    box.grid()

    state = False
    def check_box_logic():
        nonlocal state
        if state == False:
            box.config(text="[ X ]")
            state = True
        else:
            box.config(text="[   ]")
            state = False
    """

    window.mainloop()

# task_manager_program()