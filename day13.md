# Day 13: Functions

## What I Built
- Created `show_tasks()` to display all tasks
- Created `get_task_number()` to handle input validation
- Simplified remove and complete blocks

## What I Learned
- Functions = reusable code blocks
- `def function_name():` defines a function
- `return` sends a value back
- DRY principle: Don't Repeat Yourself

## One Thing I Struggled With
- Understanding that functions need to be defined BEFORE they're used
- Remembering to call functions with parentheses: `show_tasks()` not `show_tasks`

## One Thing I'm Still Fuzzy On      
- Nothing major – functions make sense now

## My Code (End of Day 13)
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
while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3.Remove a task")
    print("4. Mark a task complete")
    print("5. Search tasks")
    print("6. Quit")
    choice = input("Choose 1,2,3,4,5 or 6 ")
    if choice == "1":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
        save_tasks()
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            show_tasks()
    elif choice =="3":
        if not tasks:
            print ("no tasks to remove ")
        else:
            show_tasks()
            task_num = get_task_number("Enter the number of tasks to remove.")
            index = int(task_num) - 1
            tasks.pop(index)
            print (f"Removed task {task_num}")
    elif choice == "4":
        if not tasks:
            print ("no tasks to complete")
        else:
            show_tasks()
            task_num = get_task_number("Enter the number of tasks to mark complete.")
            index = int(task_num) - 1
            current_task = tasks[index]
            completed_task = current_task + " [DONE]"
            tasks[index] = completed_task
            save_tasks()
            print (f"Task {task_num} marked complete!")
    elif choice == "5":
        search_term = input("Enter search term: ").lower()
        found = False
        for i in range(len(tasks)):
            if search_term in tasks[i].lower():
                print(f"{i+1}. {tasks[i]}")
                found = True
        if not found:
                print("No tasks match your search.")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        
