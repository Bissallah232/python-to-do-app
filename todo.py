import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
        return
    print("\nYour Tasks:")
    for idx, t in enumerate(tasks, start=1):
        status = "x" if t.get("done") else " "
        print(f"{idx}. [{status}] {t.get('title')}")
    print()

def add_task(tasks):
    title = input("Enter a new task: ").strip()
    if not title:
        print("Empty task not added.\n")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter the number of the task to delete: "))
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n - 1)
            save_tasks(tasks)
            print(f"Task '{removed.get('title')}' deleted.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def toggle_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter the number to toggle complete/incomplete: "))
        if 1 <= n <= len(tasks):
            tasks[n - 1]["done"] = not tasks[n - 1].get("done", False)
            save_tasks(tasks)
            state = "completed" if tasks[n - 1]["done"] else "not completed"
            print(f"Task '{tasks[n - 1]['title']}' marked {state}.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter the number of the task to edit: "))
        if 1 <= n <= len(tasks):
            new = input("Enter the new text (leave blank to cancel): ").strip()
            if new:
                tasks[n - 1]["title"] = new
                save_tasks(tasks)
                print("Task updated.\n")
            else:
                print("Edit cancelled.\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def clear_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t.get("done")]
    if len(tasks) < before:
        save_tasks(tasks)
        print("Completed tasks cleared.\n")
    else:
        print("No completed tasks to clear.\n")

def main():
    tasks = load_tasks()
    while True:
        print("=== TO-DO LIST ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Toggle complete")
        print("5. Delete task")
        print("6. Clear completed")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            toggle_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            clear_completed(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()