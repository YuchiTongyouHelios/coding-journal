# Day 12: Search Feature

## What I Built
- Added option 5 to search tasks
- Search is case-insensitive (matches "DOG" and "dog")
- Shows matching tasks with their numbers
- "No matches" message if none found

## What I Learned
- `in` operator checks if a string contains another string
- `.lower()` on both sides makes search case-insensitive
- `found` flag tracks whether anything matched
- `tasks[i]` accesses the task at position i

## One Thing I Struggled With
- Typo: wrote `lens(tasks)` instead of `len(tasks)`
- Forgot capital T in `True`
- `if not found` was inside the loop at first

## One Thing I'm Still Fuzzy On
- Nothing major—search made sense

## My Code (End of Day 12)
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
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
    elif choice =="3":
        if not tasks:
            print ("no tasks to remove ")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
            while True:
                try:
                    task_num = int(input("Enter the number of task to be removed "))
                    if 1 <= task_num<= len(tasks):
                        break
                    else:
                        print(f"Please enter a number between 1 - {len(tasks)}")
                except ValueError:
                    print ("That's not a valid number. PLease enter a number")
            index = int(task_num) - 1
            tasks.pop(index)
            print (f"Removed task {task_num}")
    elif choice == "4":
        if not tasks:
            print ("no tasks to complete")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
            while True:
                try:
                    task_num = int(input("Enter the number of task to be completed "))
                    if 1 <= task_num<= len(tasks):
                        break
                    else:
                        print(f"Please enter a number between 1 - {len(tasks)}")
                except ValueError:
                    print ("That's not a valid number. PLease enter a number")
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
