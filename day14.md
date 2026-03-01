# Day 14: Refactoring – Clean Code

## What I Built
- Broke my to-do list into clean functions:
  - `show_tasks()`
  - `get_task_number()`
  - `add_task()`
  - `remove_task()`
  - `complete_task()`
  - `search_tasks()`
- Main loop is now just a menu calling functions

## What I Learned
- Functions make code reusable and readable
- DRY principle: Don't Repeat Yourself
- Each function should do ONE thing
- Return values let functions communicate

## One Thing I Struggled With
- Indentation errors after moving code into functions
- Remembering to call `save_tasks()` in every function that changes the list

## My Code (End of Day 14)
```python
tasks = []
try:
    with open("tasks.txt","r") as f:
        for line in f:
            text = line.strip()
            tasks.append(text)
    print(f"Loaded {len(tasks)} tasks from the file.")
except FileNotFoundError:
    print("No save tasks found. Starting fresh.")
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
            print(f"{i+1}.{tasks[i]}")
def get_task_number(prompt):
    """Ask user for task number, keep asking until valid"""
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num<= len(tasks):
                return num
            else:
                print(f"Please input a number between 1 - {len(tasks)}")
        except ValueError:
            print("That's not a valid number. Please input a number")
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
        print ("no tasks to remove")
        return
    show_tasks()
    task_num = get_task_number("Enter the number of the tasks to remove.")
    index = int(task_num) - 1
    tasks.pop(index)
    save_tasks()
    print (f"Removed task {task_num}")
def complete_task():
    """Mark a task as complete"""
    if not tasks:
        print ("No tasks to complete")
        return
    show_tasks()
    task_num = get_task_number("Enter the number of tasks to mark complete.")
    index = int(task_num) - 1
    current_task = tasks[index]
    completed_task = current_task + " [DONE]"
    tasks[index] = completed_task
    save_tasks()
    print (f"Task {task_num} marked complete!")
while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3.Remove a task")
    print("4. Mark a task complete")
    print("5. Search tasks")
    print("6. Quit")
    choice = input("Choose 1,2,3,4,5 or 6 ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice =="3":
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
