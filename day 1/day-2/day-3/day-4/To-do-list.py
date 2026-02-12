def add_task():
    task=input("Enter the new task: ")
    with open("tasks.txt", "a")as file:
       file.write(task + "\n")
    print("the task added successfuly")

def view_tasks():
    print("Your Tasks:")

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("No tasks file found.")


def delete_task():
    view_tasks()
    try:
      task_no=int(input("Enter the task number to delete: "))
      with open("tasks.txt","r")as file:
         tasks=file.readlines()
         if 1<=task_no <=len(tasks):
            tasks.pop(task_no -1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfuly.")
         else:
            print("Invild task number.")
    except ValueError:
       print("plese enter  vaild number.")    

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")     
                   
