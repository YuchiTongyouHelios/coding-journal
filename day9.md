# Day 9: Remove and Complete

## What I Built
- Added option 3: Remove a task by number
- Added option 4: Mark task complete with [DONE]

## What I Learned
- Removing requires converting user input (1-based) to list index (0-based)
- To modify a task: grab it, change it, put it back
- Indentation errors are invisible but deadly—every space matters

## One Thing I Struggled With
- Variable names with spaces (`completed task`) caused syntax errors
- Forgot to rename `task` back to `tasks` after modifying

## One Thing I'm Still Fuzzy On
- Still file saving (tomorrow's target)
- What happens if user enters text instead of numbers? (crashes)

## My Code (End of Day 9)
```python
tasks = []
while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3.Remove a task")
    print("4. Mark a task complete")
    print("5. Quit")
    choice = input("Choose 1,2,3,4 or 5 ")
    if choice == "1":
        new_task = input("Enter a task: ")
        tasks.append(new_task)
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
            task_num = int(input("Enter the number of task to be removed "))
            index = int(task_num) - 1
            tasks.pop(index)
            print (f"Removed task {task_num}")
    elif choice == "4":
        if not tasks:
            print ("no tasks to complete")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
            task_num = int(input("Enter the number of task to mark compete: "))
            index = int(task_num) - 1
            current_task = tasks[index]
            completed_task = current_task + " [DONE]"
            tasks[index] = completed_task
            print (f"Task {task_num} marked complete!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
