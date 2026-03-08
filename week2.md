# Week 2: To-Do List App

## What I Built

- **Day 8:** To-do list skeleton with menu loop (Add/View/Quit) and in-memory task storage.
- **Day 9:** Added remove and mark-complete features.
- **Day 10:** Permanent file storage (tasks save to `tasks.txt`, load on start).
- **Day 11:** Error handling with input validation (prevents crashes from letters or out-of-range numbers).
- **Day 12:** Search feature (case-insensitive keyword search).
- **Day 13-14:** Refactored everything into clean, reusable functions (`show_tasks`, `get_task_number`, `add_task`, etc.).

## What I Learned

- **Lists** store and manage multiple items.
- **Index vs. Number:** User sees tasks starting at 1, but Python lists start at 0 (`index = task_num - 1`).
- **File I/O:** Saving a list to a file with `open("w")` and loading it back with `open("r")` and `.strip()`.
- **Error handling:** Using `try/except` to catch `ValueError` (bad input) and `FileNotFoundError` (first run).
- **Validation loops:** The `while True` pattern to ask for input until it's valid.
- **Functions:** Creating reusable blocks with `def`, using parameters, and `return` to send values back.
- **DRY Principle:** Don't Repeat Yourself – writing code once and calling it many times.
- **String methods:** `.lower()` for case-insensitive search, `.strip()` to clean up lines from a file.

## One Thing I Struggled With

- Indentation errors (still a constant battle!).
- Understanding when to use `return` vs. `print` in functions.
- Forgetting to call `save_tasks()` after modifying the list.
- Putting the range check (`if 1 <= num <= len(tasks)`) in the wrong place (inside the `except` block).
- Copying code from one part and forgetting to change all the variable names.

## One Thing I'm Still Fuzzy On

- The exact difference between `return` and `print`, and how data moves through functions.
- What `len()` actually gives me (the count, not the last index).
- When exactly Python modifies a list "in place" vs. giving you a new one.

## My Code (End of Week 2)

```python
tasks = []
try:
    with open("tasks.txt","r") as f:
        for line in f:
            text = line.strip()
            tasks.append(text)
    print(f"Loaded {len(tasks)} tasks from the file.")
except FileNotFoundError:
    print("No saved tasks found. Starting fresh.")

def save_tasks():
    with open("tasks.txt","w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks():
    """Display all tasks with their numbers"""
    if not tasks:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def get_task_number(prompt):
    """Ask user for task number, keep asking until valid"""
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= len(tasks):
                return num
            else:
                print(f"Please enter a number between 1 and {len(tasks)}")
        except ValueError:
            print("That's not a valid number. Please enter a number.")

def add_task():
    """Add a new task."""
    new_task = input("Enter a task: ")
    tasks.append(new_task)
    save_tasks()
    print("Task added!")

def search_tasks():
    """Search for tasks containing a word."""
    search_term = input("Enter search term: ").lower()
    found = False
    for i in range(len(tasks)):
        if search_term in tasks[i].lower():
            print(f"{i+1}. {tasks[i]}")
            found = True
    if not found:
        print("No tasks match your search.")

def remove_task():
    """Remove a task by number"""
    if not tasks:
        print("No tasks to remove.")
        return
    show_tasks()
    task_num = get_task_number("Enter the number of the task to remove: ")
    index = task_num - 1
    tasks.pop(index)
    save_tasks()
    print(f"Removed task {task_num}")

def complete_task():
    """Mark a task as complete"""
    if not tasks:
        print("No tasks to complete.")
        return
    show_tasks()
    task_num = get_task_number("Enter the number of the task to mark complete: ")
    index = task_num - 1
    tasks[index] = tasks[index] + " [DONE]"
    save_tasks()
    print(f"Task {task_num} marked complete!")

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark a task complete")
    print("5. Search tasks")
    print("6. Quit")
    choice = input("Choose 1-6: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        search_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
