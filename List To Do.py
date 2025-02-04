tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def main():
    while True:
        print("\n1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()