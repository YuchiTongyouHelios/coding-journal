# Week 2: To-Do List App

## What I Built

- **Day 8:** To-do list skeleton with a menu loop (Add/View/Quit) and in-memory task storage using a Python list.

## What I Learned

- Using `while True` for a persistent menu.
- The critical difference between `if` and `elif` to prevent multiple branches from running.
- How to store multiple items in a **list**.
- Appending new items to a list with `.append()`.
- Looping through a list with `for task in tasks` to display items.
- Using a counter variable (`i`) to number tasks starting from 1.
- The difference between the **plural list name** (`tasks`) and the **singular item** (`task`) inside a loop.

## One Thing I Struggled With

- My menu printed "Invalid choice" after every valid option because I used multiple `if` statements instead of chaining them with `elif`.
- Understanding `for i in range(len(tasks)):` was confusing at first.

## One Thing I'm Still Fuzzy On

- File saving (the main goal for the rest of the week).
- Exactly how `range()` works, but I understand the simple loop with a counter.


## My Code (End of Day 8)

```python
tasks = []
while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose 1,2 or 3")
    if choice == "1":
        new_task = input("Enter a task:")
        tasks.append(new_task)
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
