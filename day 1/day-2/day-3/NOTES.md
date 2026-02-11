Student Management System – Notes
🔹 Project Overview

This is a simple Student Management System built using Python.
It stores student records in a text file (students.txt) using basic file handling operations.

The system allows the user to:

Add a student
View all students
Delete a student
Exit the program

🔹 Concepts Used
1️⃣ Functions

add_student()
view_students()
delete_student()

Functions are used to make the code modular and organized.

2️⃣ File Handling

The program uses:
"a" mode → Append data
"r" mode → Read data
"w" mode → Rewrite file after deletion

Data is stored in this format:

roll,name,course
Example:

101,Aman,Python
102,Rahul,Java

3️⃣ Exception Handling

Used:
FileNotFoundError

This prevents the program from crashing if the file does not exist.

4️⃣ Loop Control

A while True loop is used to create a menu-driven system.


🔹 How the Program Works

User selects an option (1-4).
Based on choice:
Student is added to file
Student records are displayed
Student is deleted by roll number
Program runs continuously until user selects Exit.

🔹 Limitations

Duplicate roll numbers are allowed.
Data is stored in plain text (not encrypted).
No update student feature yet.
No database used.

🔹 Future Improvements

Add update student feature
Prevent duplicate roll numbers
Use CSV module
Convert to GUI using Tkinter
Upgrade to database (SQLite/MySQL)

🔹 Learning Outcome

From this project, I learned:
Python file handling
Working with text files
Functions and modular programming
Basic CRUD operations
Menu-driven program logic