Project Overview

This is a simple command-line based To-Do List application built using Python.
It allows users to:

Add new tasks
View all saved tasks
Delete tasks by selecting their number
The tasks are stored permanently in a text file (tasks.txt) using file handling.

⚙️ Concepts Used
1️⃣ Functions

The program is divided into three main functions:

add_task() → Adds a new task
view_tasks() → Displays all tasks
delete_task() → Removes a selected task
This follows modular programming.

2️⃣ File Handling

The program uses different file modes:

Mode	Purpose
"a"	Append mode (add new task)
"r"	Read mode (view tasks)
"w"	Write mode (rewrite file after deleting task)

Tasks are stored in tasks.txt.

3️⃣ Exception Handling

The program handles errors using:
FileNotFoundError → If file does not exist
ValueError → If user enters invalid input
This makes the program more stable.

4️⃣ enumerate() Function

Used in view_tasks() to display numbered tasks:
for i, task in enumerate(tasks, start=1):
It automatically numbers the tasks starting from 1.

📂 How It Works

User selects option from menu.

Based on input:
Task is added
Tasks are displayed
Selected task is deleted
Changes are saved permanently in tasks.txt.

🚀 How to Run
python filename.py

Make sure Python is installed on your system.