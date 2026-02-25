# Day 10: File Saving

## What I Built
- Tasks now save to `tasks.txt` automatically
- Load tasks when program starts
- Save after add, remove, complete

## What I Learned
- File saving isn't one thing—it's two things: load and save
- Load = read file line by line, clean with `.strip()`, add to list
- Save = loop through list, write each task + newline
- The shape of data determines the code (one number vs list of strings)
- You don't memorize code—you understand patterns

## One Thing I Struggled With
- Mixed up number guesser code with to-do list code
- Wrote `tasks.append(task)` instead of `tasks.append(text)`
- Forgot space before [DONE]

## One Thing I'm Still Fuzzy On
- Error handling (what happens if user enters letters?)
- What if the save file gets corrupted?

## My Code (End of Day 10)
```python
tasks = []
try:
    with open("tasks.txt", "r") as f:
        for line in f:
            text = line.strip()
            tasks.append(text) 
    print(f"Loaded {len(tasks)} tasks from file.")
except FileNotFoundError:
    print("No saved tasks found. Starting fresh.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

while True:
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark a task complete")
    print("5. Quit")
    choice = input("Choose 1,2,3,4 or 5: ")

    if choice == "1":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
        save_tasks()
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}") 
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_num = int(input("Enter the number of the task to remove: "))
            index = task_num - 1
            tasks.pop(index)
            save_tasks()
            print(f"Removed task {task_num}")
    elif choice == "4":
        if not tasks:
            print("No tasks to complete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_num = int(input("Enter the number of the task to mark complete: "))
            index = task_num - 1
            current_task = tasks[index]
            tasks[index] = current_task + " [DONE]" 
            save_tasks()
            print(f"Task {task_num} marked complete!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
