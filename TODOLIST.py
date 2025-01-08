#To-Do List Application
tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['name']} [{status}]")

def add_task():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"name": task_name, "done": False})
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty!")

def update_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Enter the new task name: ").strip()
            if new_name:
                tasks[task_num - 1]["name"] = new_name
                print(f"Task {task_num} updated.")
            else:
                print("Task name cannot be empty!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program loop
while True:
    display_menu()
    choice = input("\nEnter your choice (1-6): ").strip()
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_task_done()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
