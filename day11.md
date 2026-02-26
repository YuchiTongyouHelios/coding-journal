# Day 11: Error Handling

## What I Built
- Added validation loops to prevent crashes from bad input
- Remove and complete now handle:
  - Letters instead of numbers
  - Numbers out of range
  - Empty task list

## What I Learned
- `try/except` catches errors without crashing
- `while True` with `break` creates an input validation loop
- Always validate:
  1. Is it a number? (`try/except`)
  2. Is it in range? (`if 1 <= num <= len(list)`)

## One Thing I Struggled With
- Putting the range check inside the `except` block (caused NameError)
- Forgetting to update the prompt text when copying from remove to complete
- Asking for input twice in complete block

## One Thing I'm Still Fuzzy On
- What other errors could happen? (file corrupted? disk full?)
- How to handle them

## My Code (End of Day 11)
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
    print("5. Quit")
    choice = input("Choose 1,2,3,4 or 5 ")
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        
