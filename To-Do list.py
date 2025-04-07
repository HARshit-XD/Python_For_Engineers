def display_menu():
    print("\nChoose an action:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark as completed")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "completed" if task["completed"] else "not completed"
            print(f"{i}. {task['description']} (status = {status})")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def complete_task(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

tasks = []
while True:
    display_menu()
    choice = input("Choice: ").strip()

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        delete_task(tasks)
    elif choice == '4':
        complete_task(tasks)
    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid")
