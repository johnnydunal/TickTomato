"""
This module contains functions to manage the tasks.json file. It has the following functions:
    get_tasks(): Retrieve tasks from the json file
    write_tasks(tasks): Write tasks to the json file
"""

import json

FILENAME = "tasks.json"

# Retrieve tasks from json file
def get_tasks():
    with open(FILENAME, "r") as file:
        data = json.load(file)
    return data["tasks"]

# Write tasks to json file
def write_tasks(tasks):
    data = {"tasks": tasks}
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)