import tkinter as tk

def taskWindow():
    root = tk.Tk()
    
    add_task_button = tk.Button(
        root, 
        text = "Add Task",
        command = lambda: add_task()
        )

    def add_task():
        add_task_entry = tk.Entry()
        add_task_entry.pack()

        def remove_task():
            add_task_entry.destroy()

    def save_task():
        
    add_task_button.pack()
    root.mainloop()

taskWindow()