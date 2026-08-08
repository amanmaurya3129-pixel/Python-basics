def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{course}\n")

    print("Student added successfully.")


def view_students():
    print("\nStudent Records:")
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

            if not students:
                print("No records found.")
            else:
                for i, student in enumerate(students, start=1):
                    roll, name, course = student.strip().split(",")
                    print(f"{i}. Roll: {roll}, Name: {name}, Course: {course}")

    except FileNotFoundError:
        print("Student file not found.")


def delete_student():
    view_students()
    try:
        roll_no = input("\nEnter roll number to delete: ")

        with open("students.txt", "r") as file:
            students = file.readlines()

        new_list = []
        found = False

        for student in students:
            roll, name, course = student.strip().split(",")
            if roll != roll_no:
                new_list.append(student)
            else:
                found = True

        with open("students.txt", "w") as file:
            file.writelines(new_list)

        if found:
            print("Student deleted successfully.")
        else:
            print("Roll number not found.")

    except FileNotFoundError:
        print("Student file not found.")


while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
